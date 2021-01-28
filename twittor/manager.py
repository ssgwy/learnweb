from flask_script import Manager
from flask_migrate import MigrateCommand
from twittor import create_app
#from flask.ext.script import Manage, Server

app = create_app()
manager = Manager(app)
#manager.add_command("runserver", Server(host = '0.0.0.0'))
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()                      #host='0.0.0.0', port=8080