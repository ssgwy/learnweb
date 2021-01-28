from flask import render_template , redirect, url_for
from twittor.forms import LoginForm
from twittor.models.user import User
from twittor.models.tweet import Tweet

def index():
    return render_template('index.html',name=name,posts=posts)

def login():
    return render_template('login.html',title="登录",form=form)

