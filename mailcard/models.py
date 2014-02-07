from __init__ import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(350), unique=True)
    password_hash = db.Column(db.String(120))
    mail_accounts = db.relationship('MailAccount', backref='user',
                                    lazy='dynamic')

    def __init__(self, email, password):
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.email


class MailAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(350), unique=True)
    is_authorized = db.Column(db.Boolean())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    messages = db.relationship('Message', backref='mail_account',
                               lazy='dynamic')

    def __init__(self, email, password):
        self.email = email


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(120), unique=True)
    subject = db.Column(db.String(80))
    message = db.Column(db.PickleType())

    mail_account_id = db.Column(db.Integer, db.ForeignKey('mail_account.id'))

    def __init__(self, message_id, subject, message):
        self.message_id = message_id
        self.subject = subject
        self.message = message

    def __repr__(self):
        return "<Message [{}] {}".format(self.message_id, self.subject)
