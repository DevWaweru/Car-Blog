from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Blog, Email

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server(port=4500))

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db=db, User = User, Blog = Blog, Email = Email)

if __name__=='__main__':
    manager.run()