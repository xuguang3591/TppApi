import os
from flask_migrate import MigrateCommand
from flask_script import Manager
from App import creat_app
from App.models import *


env = os.environ.get("FLASK_ENV") or "default"
app = creat_app(env)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()