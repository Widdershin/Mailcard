import contextio
from flask import Flask
import os

context_io = contextio.ContextIO(
    consumer_key=os.environ["CONTEXT_CONSUMER_KEY"],
    consumer_secret=os.environ["CONTEXT_SECRET_KEY"])

app = Flask(__name__)
