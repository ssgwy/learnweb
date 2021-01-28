from datetime import datetime
from gonghui import db

class Member_info(db.Model):
    id = db.Column(db.Integer,primary_key=True)  
    ID_num = db.Column(db.String(20),unique=True)               #身份证号
    date_birth = db.Column(db.Date)                             #出生日期
    gender = db.Column(db.String(2))                            #性别
    nation = db.Column(db.String(20))                            #民族
    political_status = db.Column(db.String(20))                 #政治面貌
    native_place = db.Column(db.String(60))                     #籍贯
    education = db.Column(db.String(20))                        #学历
    phone = db.Column(db.String(20))                            #联系电话
    email = db.Column(db.String(64))                            #电子邮箱
    remark = db.Column(db.String(60))                           #备注

    def __repr__(self):
        return "id={}, ID_num={}, date_birth={},gender={}, nation={},political_status={},native_place={},education={},phone={},email={},remark={}".format(
            self.id,self.ID_num,self.date_birth,self.gender,self.nation,self.political_status,self.native_place,self.education,self.phone,self.email,self.remark
        )
    def check_IDnum_exist(self):
        if Member_info.query.filter_by(ID_num=self).first():
            return True
        else:
            return False