from flask_migrate import MigrateCommand
from flask_script import Manager


from bbs import create_app

from apps.cms import models as cms_models

app = create_app()

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()