from flask_script import Manager
from flask_migrate import MigrateCommand           #使用数据库
from twittor import create_app

app = create_app()
manager = Manager(app)
manager.add_command('db',MigrateCommand)           #使用数据库

if __name__ == "__main__":
    manager.run()
