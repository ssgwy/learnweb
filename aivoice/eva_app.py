from flask import render_template,request,Blueprint
import websocket
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import json
from xml.dom.minidom import parseString
STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识
APPID='5f963369'
APISecret='81d0d8da0ece83dc167e63ea5378b22d'
APIKey='bc3e4c061f8a285de33124da9024f2c7'
b_eva = Blueprint("eva",__name__,static_folder="static",template_folder="templates")

@b_eva.route("/",methods=["GET","POST"])
def eva():
    if request.method=='GET':
        return render_template("audio_evaluation.html")
    else:#post
        #获取文件
        file = request.files.get("file")
        result = json.loads(request.form['result'])
        category = result[0]["category"]#评测类型
        text = result[0]["text"]#评测文本内容
        if not file:
            return render_template("audio_evaluation.html")
        #获取文件名
        filepath="static/"+file.filename
        #将文件写入到服务器
        file.save(filepath)
        #调用讯飞的语音评测接口，实现语音评测功能
        wsParam = Ws_Param(APPID=APPID, APISecret=APISecret,
                           APIKey=APIKey,
                           AudioFile=filepath,
                           Category=category,
                           Text=text)
        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()#鉴权

        info_list=[]#存储结果
        # 收到websocket消息的处理
        def on_message(ws, message):
            try:
                code = json.loads(message)["code"]
                sid = json.loads(message)["sid"]
                status = json.loads(message)["data"]["status"]
                if code != 0:
                    errMsg = json.loads(message)["message"]
                    print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))

                else:#获取返回的结果
                    if status == 2:
                        #数据的获取
                        result = str(base64.b64decode(json.loads(message)["data"]["data"]),"UTF-8")
                        print(result)
                        doc = parseString(result)
                        collection = doc.documentElement#获取xml文档对象
                        if collection.getElementsByTagName("read_sentence") != []:#语句评测
                            node = collection.getElementsByTagName("read_sentence")[1]
                            flag = 0
                        elif collection.getElementsByTagName("read_chapter") != []:#篇章
                            node = collection.getElementsByTagName("read_chapter")[1]
                            flag = 0
                        elif collection.getElementsByTagName("read_syllable") != []:#字
                            node = collection.getElementsByTagName("read_syllable")[1]
                            flag = 1
                        else:
                            node = collection.getElementsByTagName("read_word")[1]
                            flag = 1
                        if flag == 0:
                            info_list.append({"准确度":node.getAttribute("accuracy_score")})#准确度
                            info_list.append({"整体印象分":node.getAttribute("emotion_score")})#整体印象分
                            info_list.append({"流畅度分":node.getAttribute("fluency_score")})#流畅度分
                            info_list.append({"完整度分":node.getAttribute("integrity_score")})#完整度分
                        info_list.append({"声韵分":node.getAttribute("phone_score")})#声韵分
                        info_list.append({"调型分":node.getAttribute("tone_score")})#调型分
                        info_list.append({"总分":node.getAttribute("total_score")})#声韵分
                        info_list.insert(0,{"时长":node.getAttribute("time_len")})#时长
                        #字：read_syllable
                        #词：read_word
                        #句子：read_sentence
            except Exception as e:
                print("receive msg,but parse exception:", e)

        ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)

        # 收到websocket连接建立的处理--连接到服务器之后触发open事件
        def on_open(ws):
            def run(*args):
                frameSize = 8000  # 每一帧的音频大小
                intervel = 0.04  # 发送音频间隔(单位:s)
                status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧

                #参数上传阶段
                d = {"common": wsParam.CommonArgs,
                     "business": wsParam.BusinessArgs,
                     "data": {"status": 0,
                              "data":""}}
                d = json.dumps(d)#转换为json字符串
                ws.send(d)
                #音频上传阶段
                with open(wsParam.AudioFile, "rb") as fp:#读取音频文件，上传到语音评测的接口
                    while True:
                        buf = fp.read(frameSize)
                        # 文件结束
                        if not buf:
                            status = STATUS_LAST_FRAME
                        # 第一帧处理
                        # 发送第一帧音频，带business参数
                        if status == STATUS_FIRST_FRAME:
                            d = {
                                 "business": {
                                     "cmd": "auw",
                                     "aus":1,
                                     "aue":"lame"

                                 },
                                 "data": {"status": 1,
                                          "data":str(base64.b64encode(buf), 'utf-8')}}
                            d = json.dumps(d)
                            ws.send(d)
                            status = STATUS_CONTINUE_FRAME
                        # 中间帧处理
                        elif status == STATUS_CONTINUE_FRAME:
                            d = {
                                 "business": {
                                     "cmd": "auw",
                                     "aus":2,
                                     "aue":"lame"

                                 },
                                 "data": {"status": 1,
                                          "data":str(base64.b64encode(buf), 'utf-8')}}

                            ws.send(json.dumps(d))
                        # 最后一帧处理
                        elif status == STATUS_LAST_FRAME:
                            d = {
                                 "business": {
                                     "cmd": "auw",
                                     "aus":4,
                                     "aue":"lame"

                                 },
                                 "data": {"status": 2,
                                          "data":str(base64.b64encode(buf), 'utf-8')}}
                            ws.send(json.dumps(d))
                            time.sleep(1)
                            break
                        # 模拟音频采样间隔
                        time.sleep(intervel)
                ws.close()

            thread.start_new_thread(run, ())

        ws.on_open = on_open
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

        return render_template("eva_result.html",result=info_list)


class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, AudioFile,Category,Text):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.AudioFile = AudioFile
        self.Category = Category
        self.Text = Text

        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，更多个性化参数可在官网查看
        self.BusinessArgs = {"sub": "ise", #服务类型
                             "ent": "cn_vip",
                             "category":self.Category,
                             "aus":1,
                             "cmd":"ssb",
                             "text":'\uFEFF'+self.Text,
                             "tte":"utf-8",
                             "ttp_skip":True,
                             "aue":"lame",
                             "rstcd":"utf8",
                             "group":"pupil"}
    # 生成url
    def create_url(self):
        url = 'wss://ise-api.xfyun.cn/v2/open-ise'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ise-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/open-ise " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ise-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        # print("date: ",date)
        # print("v: ",v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        # print('websocket url :', url)
        return url

# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws):
    print("### closed ###")


