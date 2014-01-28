from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from imap import MailManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

import models
