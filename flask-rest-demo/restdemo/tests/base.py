import unittest
from restdemo import create_app, db


class TestBase(unittest.TestCase):

    def setUp(self):
        '''测试环境的搭建'''
        self.app = create_app(config_name='testing')    #需要一个app
        self.client = self.app.test_client      #需要一个client，发起app的请求
        #设置一个测试用户
        self.user_data = {
            'username': 'test1',
            'password': 'test1',
            'email': 'test1@test.com'
        }
        #初始化数据库的结构
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        '''用于清理数据，把数据库清理掉'''
        with self.app.app_context():
            db.session.remove()
            db.drop_all()