from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager    #引用login
from flask_mail import Mail             #发送邮件的引用
from gonghui.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()          #login关联
login_manager.login_view = 'login'      #强制登录的重定向设置
mail = Mail()             #关联发送邮件

from gonghui.route import index,login,logout,manageruser,register,password_reset_request,\
password_reset,account_add,account_query,condolence,condolence_add,test,page_not_found,member_manager,\
    membership_list,membership_roster,buju,accounts

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)    
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)          #login与app关联
    mail.init_app(app)                #login与app关联  
    app.add_url_rule('/index','index',index)
    app.add_url_rule('/','index',index)
    app.add_url_rule('/login','login',login,methods=['GET','POST'])
    app.add_url_rule('/logout','logout',logout)
    app.add_url_rule('/manageruser','manageruser',manageruser)    
    app.add_url_rule('/register','register',register,methods=['GET','POST'])
    app.add_url_rule('/password_reset_request','password_reset_request',password_reset_request,methods=['GET','POST'])
    app.add_url_rule(
        '/password_reset/<token>',
        'password_reset',
        password_reset,
        methods=['GET','POST']
    )
    app.add_url_rule('/account_query','account_query',account_query,methods=['GET','POST'])
    app.add_url_rule('/account_add','account_add',account_add,methods=['GET','POST'])
    app.add_url_rule('/condolence','condolence',condolence,methods=['GET','POST'])
    app.add_url_rule('/condolence_add','condolence_add',condolence_add,methods=['GET','POST'])
    app.add_url_rule('/member_manager','member_manager',member_manager,methods=['GET','POST'])
    app.add_url_rule('/membership_list','membership_list',membership_list,methods=['GET','POST'])
    app.add_url_rule('/membership_roster','membership_roster',membership_roster,methods=['GET','POST'])
    app.add_url_rule('/test','test',test,methods=['GET','POST'])
    app.add_url_rule('/buju','buju',buju,methods=['GET','POST'])
    app.add_url_rule('/accounts','accounts',accounts,methods=['GET','POST'])
    app.register_error_handler(404,page_not_found)
    return app
