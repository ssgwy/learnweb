from threading import Thread

from flask import current_app
from flask_mail import Message
from twittor import mail


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject,recipients,text_body,html_body):
    msg = Message(
        subject=subject,               #邮件主题
        recipients=recipients,         #接收者
        reply_to='550557063@qq.com'    #需回复的地址
    )
    msg.body = text_body             #普通文本
    msg.html = html_body
    Thread(
        target=send_async_email,
        args=(current_app._get_current_object(),msg)).start()