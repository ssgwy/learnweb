from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,validators,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError,Length

from twittor.models.user import User

class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    username = StringField("用户名",validators=[DataRequired('用户名不能为空！')])
    password = PasswordField("密码",validators=[DataRequired('密码不能为空！')])
    remember_me = BooleanField("记住密码")
    submit = SubmitField("登入")


class RegisterForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired()])
    email = StringField("电子邮箱地址", validators=[DataRequired(), Email('Email地址不正确！')])
    password = PasswordField("设置密码",validators=[DataRequired()])
    password2 = PasswordField(
        "重复密码",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("注册")


    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名已存在！')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱地址已存在！')

class EditProfileForm(FlaskForm):
    about_me = TextAreaField('个人简介',validators=[Length(min=0,max=120)])
    submit_ok = SubmitField('保存')
    submit_not = SubmitField('取消')

class TweetForm(FlaskForm):
    tweet = TextAreaField('我想说：',validators=[DataRequired(),Length(min=0,max=140)])
    submit = SubmitField('发表')

class PasswdResetRequestForm(FlaskForm):
    email = StringField("请输入注册电子邮箱地址",validators=[DataRequired(),Email()])
    submit = SubmitField('重置密码')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('邮箱地址不正确，请重输！')

class PasswdResetForm(FlaskForm):
    password = PasswordField("密码",validators=[DataRequired('密码不能为空！')])
    password2 = PasswordField(
        "重复密码",validators=[DataRequired('密码不能为空！'),EqualTo('password')])
    submit = SubmitField('提交')




