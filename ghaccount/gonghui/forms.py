from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,BooleanField,SubmitField,DateField,FloatField,SelectField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length,InputRequired
from datetime import datetime
from wtforms.fields.html5 import DateField    #让DateFiled显示为日期控件

from gonghui.models.user import User
from gonghui.models.member import Member
from gonghui.models.member_info import Member_info

class LoginForm(FlaskForm): 
    class Meta:
        csrf = False
    username = StringField("用户名",validators=[DataRequired()])
    password = PasswordField("密码",validators=[DataRequired()])
    remember_me = BooleanField("记住密码")
    submit = SubmitField("登入")

class RegisterForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired()])
    email = StringField("电子邮箱地址",validators=[DataRequired(),Email()])
    password = PasswordField("设置密码",validators=[DataRequired()])
    password2 = PasswordField("重复密码",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("增加用户")
    #检查username、email不能与数据库中重复
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名已存在！')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱地址已存在！')

class PasswdResetRequestForm(FlaskForm):
    email = StringField("请输入注册电子邮箱地址",validators=[DataRequired(),Email()])
    submit = SubmitField('发送邮件')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('邮箱地址不正确，请重输！')

class PasswdResetForm(FlaskForm):
    password = PasswordField("密码",validators=[DataRequired('密码不能为空！')])
    password2 = PasswordField(
        "重复密码",validators=[DataRequired('密码不能为空！'),EqualTo('password')])
    submit = SubmitField('提交')

class AccountAddForm(FlaskForm):
    a_date = DateField('记账日期', format='%Y-%m-%d',validators=[DataRequired()])   #,default=datetime.now()
    matters = StringField("摘要",validators=[DataRequired()])
    a_type = SelectField(label="类别",validators=[DataRequired()],
        render_kw={'class':'form-control'},
        choices=[
            ('0.1 会费收入','0.1 会费收入'),
            ('0.2 拨缴经费收入','0.2 拨缴经费收入'),
            ('0.3 上级工会补助收入','0.3 上级工会补助收入'),
            ('0.4 行政补助收入','0.4 行政补助收入'),
            ('0.5 事业收入','0.5 事业收入'),
            ('0.6 投资收益','0.6 投资收益'),
            ('0.7 其他收入','0.7 其他收入'),
            ('1.1 职工教育支出','1.1 职工教育支出'),
            ('1.2 文体活动支出','1.2 文体活动支出'),
            ('1.3 宣传活动支出','1.3 宣传活动支出'),
            ('1.4 职工集体福利支出','1.4 职工集体福利支出'),
            ('1.5 其他活动支出','1.5 其他活动支出'),
            ('2.1 劳动关系协调费','2.1 劳动关系协调费'),
            ('2.2 劳动保护费','2.2 劳动保护费'),
            ('2.3 法律援助费','2.3 法律援助费'),
            ('2.4 困难职工帮扶费','2.4 困难职工帮扶费'),
            ('2.5 送温暖费','2.5 送温暖费'),
            ('2.6 其他维权支出','2.6 其他维权支出'),
            ('3.1 培训费','3.1 培训费'),
            ('3.2 会议费','3.2 会议费'),
            ('3.3 专项业务费','3.3 专项业务费'),
            ('3.4 其他业务支出','3.4 其他业务支出'),
            ('4.0 资本性支出','4.0 资本性支出'),
            ('5.0 事业支出','5.0 事业支出'),
            ('6.0 其他支出','6.0 其他支出')],
            )     #default='职工活动支出'
    a_count = FloatField("金额",validators=[DataRequired()])
    remark = TextAreaField("备注", validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')

class AccountQueryForm(FlaskForm):
    date_begin = DateField('开始日期',format='%Y-%m-%d')
    date_end = DateField('结束日期',format='%Y-%m-%d')
    matters = StringField("摘要事项")
    a_type = SelectField(label="会计科目",
        render_kw={'class':'form-control'},
        choices=[
            ('',''),
            
            ('0.1 会费收入','0.1 会费收入'),
            ('0.2 拨缴经费收入','0.2 拨缴经费收入'),
            ('0.3 上级工会补助收入','0.3 上级工会补助收入'),
            ('0.4 行政补助收入','0.4 行政补助收入'),
            ('0.5 事业收入','0.5 事业收入'),
            ('0.6 投资收益','0.6 投资收益'),
            ('0.7 其他收入','0.7 其他收入'),
            ('1.1 职工教育支出','1.1 职工教育支出'),
            ('1.2 文体活动支出','1.2 文体活动支出'),
            ('1.3 宣传活动支出','1.3 宣传活动支出'),
            ('1.4 职工集体福利支出','1.4 职工集体福利支出'),
            ('1.5 其他活动支出','1.5 其他活动支出'),
            ('2.1 劳动关系协调费','2.1 劳动关系协调费'),
            ('2.2 劳动保护费','2.2 劳动保护费'),
            ('2.3 法律援助费','2.3 法律援助费'),
            ('2.4 困难职工帮扶费','2.4 困难职工帮扶费'),
            ('2.5 送温暖费','2.5 送温暖费'),
            ('2.6 其他维权支出','2.6 其他维权支出'),
            ('3.1 培训费','3.1 培训费'),
            ('3.2 会议费','3.2 会议费'),
            ('3.3 专项业务费','3.3 专项业务费'),
            ('3.4 其他业务支出','3.4 其他业务支出'),
            ('4.0 资本性支出','4.0 资本性支出'),
            ('5.0 事业支出','5.0 事业支出'),
            ('6.0 其他支出','6.0 其他支出')
            ],default='')
    in_out = SelectField(label="收支类别",choices=[('',''),('收入','收入'),('支出','支出')],default='')
    input_ok =  StringField("删除确认")     
    submit = SubmitField('查询')

class CondolenceAddForm(FlaskForm):
    c_date = DateField('慰问日期', format='%Y-%m-%d',validators=[DataRequired()])   #,default=datetime.now()
    c_name = StringField("被慰问人",validators=[DataRequired()]) 
    c_type = SelectField(label="慰问类别",validators=[DataRequired()],
        render_kw={'class':'form-control'},
        choices=[('结婚慰问','结婚慰问'),('生育慰问','生育慰问'),('住院慰问','住院慰问'),
            ('大病慰问','大病慰问'),('丧事慰问','丧事慰问'),('生日慰问','生日慰问'),
            ('退休慰问','退休慰问'),('节日慰问','节日慰问')],default='住院慰问')
    c_count = FloatField("慰问金额",validators=[DataRequired()])
    remark = TextAreaField("备注", validators=[Length(min=0, max=140)]) 
    submit = SubmitField('提交')

class CondolenceForm(FlaskForm):
    date_begin = DateField('开始日期',format='%Y-%m-%d')
    date_end = DateField('结束日期',format='%Y-%m-%d')
    c_name = StringField("被慰问人")
    c_type = SelectField(label="慰问类型",
        render_kw={'class':'form-control'},
        choices=[('',''),('结婚慰问','结婚慰问'),('生育慰问','生育慰问'),('住院慰问','住院慰问'),
            ('大病慰问','大病慰问'),('丧事慰问','丧事慰问'),('生日慰问','生日慰问'),
            ('退休慰问','退休慰问'),('节日慰问','节日慰问')],default='')
    remark = TextAreaField("备注", validators=[Length(min=0, max=140)])
    is_ok =  StringField("删除确认") 
    in_account = SelectField(label="是否入账",
        render_kw={'class':'form-control'},
        choices=[('',''),('已入账','已入账'),('未入账','未入账')],default='')
    submit = SubmitField('查询')

class MemberForm(FlaskForm):
    name = StringField("会员姓名",validators=[DataRequired()])
    date_year = IntegerField('会籍年份',validators=[DataRequired()])
    date_half_year = SelectField(label="半年份别",
        render_kw={'class':'form-control'},
        choices=[('上半年','上半年'),('下半年','下半年')],default='上半年')
    gender = StringField("性别",validators=[DataRequired()])
    nation = StringField("民族")
    political_status = StringField("政治面貌")
    native_place = StringField("籍贯")
    date_birth = DateField('出生日期',format='%Y-%m-%d')
    education = StringField("学历")
    ID_num = StringField("身份证号码")
    phone = StringField("联系电话")
    email = StringField("电子邮箱地址",validators=[Email()])
    personnel_type = StringField("职工类型",validators=[DataRequired()])
    salary = FloatField("月基本工资",validators=[DataRequired()])
    remark = StringField("备注")
    submit = SubmitField("增加会员")

class TestForm(FlaskForm):
    date_year = IntegerField('会籍年份')
    date_half_year = StringField("半年区间")

class MemberListForm(FlaskForm):
    date_year = IntegerField('会籍年份',validators=[DataRequired()])
    date_half_year = SelectField(label="半年份别",
        render_kw={'class':'form-control'},
        choices=[('上半年','上半年'),('下半年','下半年')],default='上半年')
    name = StringField("会员姓名",validators=[DataRequired()])
    personnel_type = SelectField(label="职工类别",
        render_kw={'class':'form-control'},
        choices=[('',''),('在编','在编'),('合同','合同'),('职员','职员'),('其他','其他')],default='')
    input_ok =  StringField("删除确认")
    submit = SubmitField("查询")

class MemberInfoForm(FlaskForm):
    date_year = IntegerField('会籍年份',validators=[DataRequired()])
    date_half_year = SelectField(label="半年份别",
        render_kw={'class':'form-control'},
        choices=[('上半年','上半年'),('下半年','下半年')],default='上半年')
    name = StringField("会员姓名",validators=[DataRequired()])
    gender =SelectField(label="性别",
        render_kw={'class':'form-control'},
        choices=[('',''),('男','男'),('女','女')],default='')
    nation = StringField("民族")
    political_status = SelectField(label="政治面貌",
        render_kw={'class':'form-control'},
        choices=[('',''),('中共党员','中共党员'),('共青团员','共青团员'),('群众','群众'),
            ('民革党员','民革党员'),('民盟党员','民盟党员'),('民建党员','民建党员'),('农工党员','农工党员'),('致公党员','致公党员'),('九三学社','九三学社'),('台盟党员','台盟党员')],default='')
    native_place = StringField("籍贯")
    date_birth = DateField('出生日期',format='%Y-%m-%d')
    education = StringField("学历")
    ID_num = StringField("身份证号码")
    phone = StringField("联系电话")
    email = StringField("电子邮箱地址",validators=[Email()])
    personnel_type = SelectField(label="职工类别",
        render_kw={'class':'form-control'},
        choices=[('',''),('在编','在编'),('合同','合同'),('职员','职员'),('其他','其他')],default='')
    remark = StringField("备注")
    submit = SubmitField("查询")