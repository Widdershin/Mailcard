from __init__ import db, MailManager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    smtp_password = db.Column(db.String(120))
    threads = db.relationship("Thread", backref='user')
    last_checked = db.Column(db.DateTime)

    def __init__(self, email, smtp_password):
        self.email = email
        self.smtp_password = smtp_password

    def __repr__(self):
        return '<User %r>' % self.email

    def check_emails(self):
        mail = MailManager('imap.gmail.com',
                      username=self.email,
                      password=self.smtp_password)

        print mail.list_folders()

        # for n, (uuid, data) in enumerate(inbox.messages()):
        #     if n > 5:
        #         print "Breaking"
        #         break

        #     message = Message(uuid, data)

        #     print n, message
        #     db.session.add(message)

        # db.session.commit()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    json = db.Column(db.PickleType)

    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))

    def __init__(self, uuid, json):
        self.uuid = uuid
        self.json = json

    def __repr__(self):
        return "<Message {}>".format(self.uuid)


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.relationship("Message", backref='thread')

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
