from flask import render_template,redirect, url_for
from twittor.forms import LoginForm
from twittor.models import User,Tweet
def index():
    name = {'username':'=GWY='}
    posts = [
        {
            'author':{'username':'张三'},
            'body':"你好，我是张三！"
        }, 
        {
            'author':{'username':'机器人'},
            'body':"你好，我是机器人！"
        },
         {
            'author':{'username':'张三'},
            'body':"机器人，你好！"
        },
    ]
    return render_template('index.html',title="首页",name=name,posts=posts)

def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        msg = "username={},password={},remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data
        )
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html',title="登录",form=form)