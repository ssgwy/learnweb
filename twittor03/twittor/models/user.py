from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from twittor import db
class User(db.Model):
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


