from flask import Flask
import os

app = Flask(__name__)
from app import views

app.secret_key = os.urandom(12)
app.config["DEBUG"] = True