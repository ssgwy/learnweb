from datetime import datetime
from gonghui import db

class Condolence(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    c_date = db.Column(db.Date)
    c_year = db.Column(db.Integer)
    c_quarter = db.Column(db.Integer)
    c_name = db.Column(db.String(10))
    c_type = db.Column(db.String(10))
    c_count = db.Column(db.Float(20,2))
    remark = db.Column(db.String(50))
    in_account = db.Column(db.String(5))

    def __repr__(self):
        return "id={}, c_date={}, c_name={}, c_type={},c_count={},remark={},in_account={}".format(
            self.id,self.c_date,self.c_name,self.c_type,self.c_count,self.remark,self.in_account
        )
