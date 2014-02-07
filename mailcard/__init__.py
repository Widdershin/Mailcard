import contextio
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.login import LoginManager
import os
import sys

context_io = contextio.ContextIO(
    consumer_key=os.environ["CONTEXT_CONSUMER_KEY"],
    consumer_secret=os.environ["CONTEXT_SECRET_KEY"])

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://mailcard-admin:test@localhost/mailcard'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

sys.path.append("..\\")

import models
import forms
from views import *
