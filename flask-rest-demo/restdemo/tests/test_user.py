import unittest
import json
from restdemo import create_app, db
from restdemo.tests.base import TestBase

class TestUser(TestBase):

    def test_user_create(self):
        #用于调用用户创建的API
        #post模拟API的请求的POST方法，模拟用户创建
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data = self.user_data
        )
        self.assertEqual(res.status_code, 201)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('username'), self.user_data['username'])
        self.assertEqual(res_data.get('email'), self.user_data['email'])

        #模拟再创建一次相同用户名或email
        res = self.client().post(
            url,
            data = self.user_data
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('message'), 'user already exist')

    def test_user_get(self):
        #模拟用户创建：
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data = self.user_data
        )
        #模拟获取用户，并验证用户名和密码是否相同：
        res = self.client().get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('username'), self.user_data['username'])
        self.assertEqual(res_data.get('email'), self.user_data['email'])

    def test_user_get_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'}) 

    def test_user_delete(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data = self.user_data
        )
        res = self.client().delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data, {'message': 'user deleted'})

    def test_user_delete_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})

    def test_user_update(self):
        #创建一人用户：
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data = self.user_data
        )
        #更新用户的密码和地址：
        res = self.client().put(
            url,
            data={
                'password': 'newpassword',
                'email': 'newemail@new.com'
            }
        )
        res_data = json.loads(res.get_data(as_text=True))
        #检查返回的结果
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['email'], 'newemail@new.com') 

    def test_user_update_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().put(
            url,
            data={
                'password': 'newpassword',
                'email': 'newemail@new.com'
            }
        )
        res_data = json.loads(res.get_data(as_text=True))
        #检查返回的结果
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})