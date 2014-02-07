from flask.ext.script import Manager
from mailcard import app, db, models, migrate, MigrateCommand

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def nuke():
    """Recreates all tables"""
    db.drop_all()
    db.create_all()

@manager.command
def list_messages():
    """List all instances of Message"""
    return models.Message.query.all()

if __name__ == '__main__':
    manager.run()