import unittest
import json
from restdemo import create_app, db
from restdemo.tests.base import TestBase

class TestLogin(TestBase):
#------------------开始测试---------------------------
    def test_login(self):
        #第1步：创建用户：
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data = self.user_data
        )
        #第2步：设置登录的url和账号密码，并返回结果：
        url = '/auth/login'
        res = self.client().post(
            url,
            data=json.dumps({
                'username': 'test1',
                'password': 'test1'
            }),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertIn('access_token',res_data)

    def test_login_failed(self):
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data = self.user_data
        )
        url = '/auth/login'
        res = self.client().post(
            url,
            data=json.dumps({
                'username': 'test1',
                'password': 'wrongpass'
            }),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(res.status_code, 401)
        res_data = json.loads(res.get_data(as_text=True))
        data = {
            "description": "Invalid credentials",
            "error": "Bad Request",
            "status_code": 401
        }
        self.assertEqual(res_data, data)       

