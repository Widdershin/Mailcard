import contextio
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

context_io = contextio.ContextIO(
    consumer_key=os.environ["CONTEXT_CONSUMER_KEY"],
    consumer_secret=os.environ["CONTEXT_SECRET_KEY"])

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

import models