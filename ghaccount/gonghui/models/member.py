from datetime import datetime
from gonghui import db
from gonghui.models.member_info import Member_info

class Member(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    member_id = db.Column(db.Integer)
    date_year = db.Column(db.Integer,index=True)                #会籍年份
    date_half_year = db.Column(db.String(6),index=True)         #上下半年   
    name = db.Column(db.String(64),index=True)                  #姓名
    ID_num = db.Column(db.String(20))                           #身份证号
    salary = db.Column(db.Float)                                #月基本工资
    membership_fee = db.Column(db.Float)                        #会费
    personnel_type =  db.Column(db.String(10),index=True)       #职工类型 

    def __repr__(self):
        return "id={},date_year={},date_half_year={}, name={},ID_num={}, salary={}, menbership_fee={},personnel_type={}".format(
            self.id,self.date_year,self.date_half_year,self.name,self.ID_num,self.salary,self.membership_fee,self.personnel_type
        )