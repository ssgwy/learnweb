from flask_restful import Resource, reqparse

from restdemo import db
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

class Login(Resource):

    parser = reqparse.RequestParser()      #1、引入对象
    parser.add_argument(
        'username', type=str, required=True, help='required username'
    )       
    parser.add_argument(
        'password', type=min_length_str(5), required=True, 
        help='{error_msg}'
    )

    def post(self):
        ''' 验证用户名和密码 '''  
        #print(request.get_json())  
        data = Login.parser.parse_args()    #3、引用检查
        user = db.session.query(UserModel).filter(
            UserModel.username == data['username']  #验证用户
        ).first()
        if user:
            if not user.check_password(data['password']):   #验证密码
                return {
                    "message":"login faild, please input the right username or password"
                }
            return {
                "message": "login success",
                "token": user.generate_token()
            }
        else:
            {
                "message":"login faild, please input the right username or password"
            }