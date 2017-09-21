from flask import render_template, session, redirect
from .user import User
from app import app

users = []

@app.route('/')
@app.route('/index')
def index():
    """ The homepage showing the user dashboard """

    return render_template('index.html')
