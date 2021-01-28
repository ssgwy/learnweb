import unittest
import json
from restdemo import create_app, db
from restdemo.tests.base import TestBase

class TestTweet(TestBase):

    def test_tweet(self):
        #1、创建用户
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data = self.user_data
        )
        #2、用户登录
        url = '/auth/login'
        res = self.client().post(
            url,
            data=json.dumps({'username': 'test1', 'password': 'test1'}),
            headers={'Content-Type': 'application/json'}
        )        
        #3、获取token
        res_data = json.loads(res.get_data(as_text=True))
        access_token = '{} {}'.format(
            self.app.config['JWT_AUTH_HEADER_PREFIX'],
            res_data['access_token']
        )
        #4、post tweet
        url = '/tweet/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data={'body': 'hello world'},
            headers={'Authorization': access_token}
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data, {'message': 'post success'})
        #5、get tweet
        url = '/tweet/{}'.format(self.user_data['username'])
        res = self.client().get(
            url,
            headers={'Authorization': access_token}
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res_data), 1)