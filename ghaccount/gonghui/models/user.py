from hashlib import md5
import time
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask import current_app
import jwt
from gonghui import db,login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'id={},username={},email={},password_hash={}'.format(
            self.id,self.username,self.email,self.password_hash
        )

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password) 

    def get_jwt(self,expire=7200):                #生成token expire为超时时间
        return jwt.encode(
            {
                'email':self.email,              #当前用户email地址
                'exp':time.time() + expire        #超时时间
            },
            current_app.config['SECRET_KEY'],      #加密方法
            algorithm='HS256'
        ).decode('utf-8')

    @staticmethod               #静态方法
    def verify_jwt(token):      #验证
        try:
            email = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )
            email = email['email']
        except:
            return
        return User.query.filter_by(email=email).first()

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
