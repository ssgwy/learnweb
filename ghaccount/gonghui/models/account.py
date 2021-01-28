from datetime import datetime
from gonghui import db

class Account(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    a_date = db.Column(db.Date,index=True)
    matters = db.Column(db.String(50))
    a_type = db.Column(db.String(60),index=True)
    a_count = db.Column(db.Float)
    in_out = db.Column(db.String(2),index=True)
    remark = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "id={}, a_date={}, matters={}, a_type={},a_count={},in_out={},remark={},create_time={}".format(
            self.id,self.a_date,self.matters,self.a_type,self.a_count,self.in_out,self.remark,self.create_time
        )
