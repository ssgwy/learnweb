# -*- coding:utf-8 -*-
#
#   author: iflytek
#
#  本demo测试时运行的环境为：Windows + Python3.7
#  本demo测试成功运行时所安装的第三方库及其版本如下：
#   cffi==1.12.3
#   gevent==1.4.0
#   greenlet==0.4.15
#   pycparser==2.19
#   six==1.12.0
#   websocket==0.2.1
#   websocket-client==0.56.0
#   合成小语种需要传输小语种文本、使用小语种发音人vcn、tte=unicode以及修改文本编码方式
#  错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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
import os

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识
APPID='5f963369'
APISecret='81d0d8da0ece83dc167e63ea5378b22d'
APIKey='bc3e4c061f8a285de33124da9024f2c7'

b_tts = Blueprint("tts",__name__,static_folder="static",template_folder="templates")

@b_tts.route('/',methods=["GET","POST"])
def get_tts_html():
    if request.method == "GET":
        default_text = """
女士们,先生们,欢迎您选乘东方航空公司CA101航班前往三亚。
非常感谢各位旅客长期以来对东方航空的支持与信赖。
机门已经关闭,请您关闭手机等电子设备,并系好安全带。
现在为您播放安全须知录像,请留意收看。
我们全体机组成员将竭诚为您服务,祝您旅途愉快,谢谢!"""
        content = {
            "msg": default_text,
            "voice_name": "aisjiuxu",  # 发音人
            "speed": 40,  # 语速
            "volume": 55,  # 音量
            "pitch": 60,  # 音高
            "bgs": "1"  # 背景乐打开
        }
        return render_template("tts.html",content=content)
    else:#post请求
        text = request.form["TEXT"]
        voice_name = request.form["voice_name"]#发音人
        speed = request.form["speed"]#语速
        volume = request.form["volume"]#音量
        pitch = request.form["pitch"]#音高
        bgs = request.form["bgs"]#背景音乐
        content = {
            "msg": text,
            "voice_name": voice_name,  # 发音人
            "speed": speed,  # 语速
            "volume": volume,  # 音量
            "pitch": pitch,  # 音高
            "bgs": bgs  # 背景乐打开
        }
        #语音合成---科大讯飞语音接口
        #生成文本socket的参数类的对象
        wsParam = Ws_Param(APPID=APPID, APISecret=APISecret,
                           APIKey=APIKey,
                           Text=text,
                           voice_name=voice_name,
                           speed=speed,
                           volume=volume,
                           pitch=pitch,
                           bgs=bgs)
        websocket.enableTrace(False)#调试关闭
        nowtime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        tts_file = "./static/"+nowtime+r'tts.mp3'
        tts_file_post = nowtime+r'tts.mp3'
        wsUrl = wsParam.create_url()#获取握手地址

        def on_message(ws, message):
            try:
                message = json.loads(message)
                code = message["code"]
                sid = message["sid"]
                audio = message["data"]["audio"]
                audio = base64.b64decode(audio)
                status = message["data"]["status"]
                print(message)
                if status == 2:
                    print("ws is closed")
                    ws.close()
                if code != 0:
                    errMsg = message["message"]
                    print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
                else:

                    with open(tts_file, 'ab') as f:
                        f.write(audio)
            except Exception as e:
                print("receive msg,but parse exception:", e)
        ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)

        # 收到websocket连接建立的处理----连接到服务器之后就会触发on_open事件
        def on_open(ws):
            def run(*args):
                d = {"common": wsParam.CommonArgs,
                     "business": wsParam.BusinessArgs,
                     "data": wsParam.Data,
                     }
                d = json.dumps(d)
                print("------>开始发送文本数据")
                ws.send(d)
                if os.path.exists(tts_file):
                    os.remove(tts_file)

            thread.start_new_thread(run, ())

        ws.on_open = on_open
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

        return render_template("tts.html",content=content,file_name = tts_file_post)

class Ws_Param(object):#websocket参数类
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, Text,voice_name,speed,volume,pitch,bgs):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.Text = Text

        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，更多个性化参数可在官网查看
        self.BusinessArgs = {"aue": "lame",
                             "auf": "audio/L16;rate=16000",
                             "vcn": voice_name,#发音人
                             "speed":int(speed),#语速
                             "volume":int(volume),#音量
                             "pitch":int(pitch),#音高
                             "bgs":int(bgs),
                             "tte": "utf8"}
        self.Data = {"status": 2, "text": str(base64.b64encode(self.Text.encode('utf-8')), "UTF8")}
        #使用小语种须使用以下方式，此处的unicode指的是 utf16小端的编码方式，即"UTF-16LE"”
        #self.Data = {"status": 2, "text": str(base64.b64encode(self.Text.encode('utf-16')), "UTF8")}

    # 生成url
    def create_url(self):
        url = 'wss://tts-api.xfyun.cn/v2/tts'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/tts " + "HTTP/1.1"
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
            "host": "ws-api.xfyun.cn"
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
