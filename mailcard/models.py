from __init__ import db


#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(120), unique=True)
#    password = db.Column(db.String(120))
#    smtp_password = db.Column(db.String(120))
#
#    def __init__(self, username, email):
#        self.username = username
#        self.email = email
#
#    def __repr__(self):
#        return '<User %r>' % self.username

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(120), unique=True)
    subject = db.Column(db.String(80))
    message = db.Column(db.PickleType())

    def __init__(self, message_id, subject, message):
        self.message_id = message_id
        self.subject = subject
        self.message = message

    def __repr__(self):
        return "<Message [{}] {}".format(self.message_id, self.subject)
