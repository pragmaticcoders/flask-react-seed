import sys

from flask_script import Manager
from flask_migrate import MigrateCommand


from src.config import SRC_ROOT
sys.path.append(SRC_ROOT)


if __name__ == '__main__':
    from src.wsgi import app

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    manager.run()
