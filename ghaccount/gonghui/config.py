import os
config_path = os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","mysql+pymysql://root:root@localhost:3306/gonghui")
    #"mysql+pymysql://root:root@localhost:3306/twittor"
    #"sqlite:///" + os.path.join(config_path,'gonghui.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'abc123'

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER','550557063@qq.com')
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.qq.com')               #电子邮件服务器主机名或IP地址                         
    MAIL_PORT = os.environ.get('MAIL_PORT',587 )                          #电子邮件服务器的端口
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS',1)                          #启用传输安全层协议
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','550557063')               #邮件账户的用户名
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','jirofeqnfhwdbbgi')        #邮件账户的授权码jirofeqnfhwdbbgi
    MAIL_SUBJECT_PASSWORD_RESET = '[工会财管系统]请重新设置您的密码'       #邮件标题