from flask import render_template,redirect,url_for,request,abort,current_app,flash
from flask_login import login_user,current_user,logout_user,login_required

from twittor.forms import LoginForm,RegisterForm,EditProfileForm,TweetForm,PasswdResetRequestForm,PasswdResetForm
from twittor.models.user import User
from twittor.models.tweet import Tweet
from twittor import db
from twittor.email import send_email

@login_required
def index():
    form = TweetForm()
    if form.validate_on_submit():
        t = Tweet(body=form.tweet.data,author=current_user)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    page_num = int(request.args.get('page') or 1)
    tweets = current_user.own_and_followed_tweets().paginate(
        page=page_num,per_page=current_app.config['TWEET_PER_PAGE'],error_out=False)
    next_url = url_for('index',page=tweets.next_num) if tweets.has_next else None
    prev_url = url_for('index',page=tweets.prev_num) if tweets.has_prev else None
    return render_template('index.html',title="首页",tweets=tweets.items,form=form,next_url=next_url,prev_url=prev_url)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('invalid username or password')
            return redirect(url_for('login'))
        login_user(u,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html',title="登录",form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))


def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='用户注册', form=form)

@login_required
def user(username):
    u = User.query.filter_by(username=username).first()
    if u is None:
        abort(404)
    page_num = int(request.args.get('page') or 1)
    tweets = u.tweets.order_by(Tweet.create_time.desc()).paginate(
        page=page_num,
        per_page=current_app.config['TWEET_PER_PAGE'],
        error_out=False)

    next_url = url_for(
        'profile',
        page=tweets.next_num,
        username=username) if tweets.has_next else None
    prev_url = url_for( 
        'profile',
        page=tweets.prev_num,
        username=username) if tweets.has_prev else None
    if request.method == 'POST':
        if request.form['request_button'] == '关注':
            current_user.follow(u)
            db.session.commit()
        elif request.form['request_button'] == '取消关注':
            current_user.unfollow(u)
            db.session.commit()
        else:
            flash("已发送电子邮件到您的电子邮箱地址，请检查！！！！")
            send_email_for_user_activate(current_user)
    return render_template(
        'user.html',
        title="个人主页",
        tweets=tweets.items,
        user=u,
        next_url=next_url,
        prev_url=prev_url
        )

def send_email_for_user_activate(user):
    token = user.get_jwt()
    url_user_activate = url_for(
        'user_activate',
        token=token,
        _external=True
    )
    send_email(
        subject=current_app.config['MAIN_SUBJECT_USER_ACTIVATE'],
        recipients=[user.email],
        text_body= render_template(
            'email/user_activate.txt',
            username=user.username,
            url_user_activate=url_user_activate
        ),
        html_body=render_template(
            'email/user_activate.html',
            username=user.username,
            url_user_activate=url_user_activate
        )
    )

def user_activate(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_jwt(token)
    if not user:
        msg = "令牌失效，请重新发送邮件！"
    else:
        user.is_activated = True
        db.session.commit()
        msg = '用户账号已激活！'
    return render_template(
        'user_activate.html', msg=msg
    )

def page_not_found(e):
    return render_template('404.html',title="404"),404

@login_required
def edit_profile():
    form = EditProfileForm()
    #如果存在信息，则显示出来
    if request.method == 'GET':
        form.about_me.data = current_user.about_me
    #保存信息
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
    #跳转到个人简介页面,url_for()里面填写页面别名
        return redirect(url_for('profile',username=current_user.username))
    return render_template('edit_profile.html',title="编辑个人简介",form=form)

def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PasswdResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash(
                "您将收到一封允许您重置密码的电子邮件。如果找不到这封邮件，请务必检查您的垃圾邮件！"
            )
            token = user.get_jwt()
            url_password_reset = url_for(
                'password_reset',
                token=token,
                _external=True                    #发送的链接是完整的http链接
            )
            url_password_reset_request = url_for(
                'reset_password_request',
                _external=True
            )
            send_email(
               subject=current_app.config['MAIL_SUBJECT_RESET_PASSWORD'],                    #主题
               recipients=[user.email],                             #接收者
               text_body=render_template(
                   'email/passwd_reset.txt',
                   url_password_reset=url_password_reset,
                   url_password_reset_request=url_password_reset_request
               ),
               html_body=render_template(
                   'email/passwd_reset.html',
                   url_password_reset=url_password_reset,
                   url_password_reset_request=url_password_reset_request
               )
            )
        return redirect(url_for('login'))
    return render_template('password_reset_request.html',title="重置密码",form=form)

def password_reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_jwt(token)
    if not user:
        return redirect(url_for('login'))
    form = PasswdResetForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template(
        'password_reset.html',title='密码重置',form=form
    )

@login_required
def explore():
    # get all user and sort by followers
    page_num = int(request.args.get('page') or 1)
    tweets = Tweet.query.order_by(Tweet.create_time.desc()).paginate(
        page=page_num, per_page=current_app.config['TWEET_PER_PAGE'], error_out=False)

    next_url = url_for('index', page=tweets.next_num) if tweets.has_next else None
    prev_url = url_for('index', page=tweets.prev_num) if tweets.has_prev else None
    return render_template(
        'explore.html',title="圈圈大厅", tweets=tweets.items, next_url=next_url, prev_url=prev_url
    )