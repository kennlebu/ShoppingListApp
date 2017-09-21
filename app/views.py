from flask import render_template, session, redirect, request, url_for
from .user import User
from app import app

users = []

@app.route('/')
@app.route('/index')
def index():
    """ The homepage showing the user dashboard """

    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ The signup page """

    # Get form content and sign up user
    if request.method == 'POST':

        # If submit button has been clicked
        if request.form['signup']:
            username = request.form['username']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            firstname = request.form['firstname']
            lastname = request.form['lastname']

            # Ensure there are no blank fields
            if (not firstname or not lastname or not username or not password or
                    not confirm_password):
                return render_template('signup.html', error_msg='All fields are required')

            # Ensure passwords match
            if not password == confirm_password:
                return render_template('signup.html', error_msg='Passwords should match')

            # Check whether username has already been taken
            for user in users:
                if user.username == username:
                    return render_template('signup.html',
                                           error_msg='That username is already in use')

            # Create and save the user
            user = User(username, password, firstname, lastname)
            users.append(user)

            # Redirect the new user to login page
            return redirect(url_for('login'))

    return render_template('signup.html')

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Logins in a user to the app """

    if request.method == 'POST':

        # Login button clicked?
        if request.form['login']:
            username = request.form['username']
            password = request.form['password']

        # Check credentials
        for user in users:
            if user.username == username and user.password == password:
                session['logged_in'] = True
                session['name'] = '{0} {1}'.format(user.firstname, user.lastname)
                return redirect(url_for('index'))

        return render_template('login.html', error_msg='Invalid username or password')

    return render_template('login.html')
