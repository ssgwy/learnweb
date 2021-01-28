from flask_restful import Resource, reqparse
from flask import request, current_app
from flask_jwt import jwt_required

from restdemo.model.user import User as UserModel


def min_length_str(min_length):
    def validate(s):
        #print(type(s))
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int,str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i characters long" % min_length)
    return validate

class User(Resource):
    parser = reqparse.RequestParser()      #1、引入对象
    parser.add_argument(
        'password', type=min_length_str(5), required=True, 
        help='{error_msg}'
    )
    parser.add_argument(
        'email', type=str, required=True, help='required email'
    )                                           #2、定义方法

    def get(self,username):
        ''' 获取用户详细信息 '''
        user = UserModel.get_by_username(username)
        if user:
            return user.as_dict()
        return {'message': 'user not found'}, 404     #否则返回错误信息
    
    def post(self,username):
        ''' 创建用户 '''  
        #print(request.get_json())  
        data = User.parser.parse_args()    #3、引用检查
        user = UserModel.get_by_username(username)
        if user:
            return {'message': 'user already exist'}
        user = UserModel(
            username=username,
            email=data['email']
        )
        user.set_password(data['password'])
        user.add()  #引用add方法
        return user.as_dict(), 201   #, 201表示状态

    def delete(self, username):
        ''' 删除用户 '''
        user = UserModel.get_by_username(username)
        if user:
            user.delete()   #引用delete方法
            return {'message': 'user deleted'}
        else:
            return {'message': 'user not found'}, 404  #204表示没找到对应内容

    def put(self, username):
        ''' 更新用户 '''
        user = UserModel.get_by_username(username)
        if user:
            data = User.parser.parse_args()    #3、引用检查
            #user.password_hash = data['password']
            user.email = data['email']
            user.set_password(data['password'])
            user.update()   #引用update方法
            return user.as_dict()
        else:
            return {'message': 'user not found'}, 404

class UserList(Resource):
    
    @jwt_required()
    def get(self):
        users = UserModel.get_user_list()
        return [u.as_dict() for u in users]