from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
import mailcard

manager = Manager(mailcard.app)

manager.add_command('db', MigrateCommand)


@manager.command
def nuke():
    """Recreates all tables"""
    mailcard.db.drop_all()
    mailcard.db.create_all()


@manager.command
def list_messages():
    """List all instances of Message"""
    return mailcard.models.Message.query.all()


@manager.command
def run(debug=True):
    mailcard.app.run(debug)

if __name__ == '__main__':
    manager.run()
