from datetime import timedelta
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)  #超时时间300秒
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_AUTH_HEADER_PREFIX = os.environ.get('JWT_AUTH_HEADER_PREFIX', 'FLASK')  #从环境变量中查找，如果找到，则取环境变量中的值，否则取值为FLASK
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask123')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')    #命令行中设置：set DATABASE_URL=mysql+pymysql://root:root@localhost:3306/demo

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass  

app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'projection': ProductionConfig
}

