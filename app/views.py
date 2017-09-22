from flask import render_template, session, redirect, request, url_for
from .user import User
from .shopping_list import ShoppingList
from app import app

users = []

@app.route('/')
@app.route('/index')
def index():
    """ The homepage showing the user dashboard """

    # Redirect to login page if user is not logged in yet
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('index.html', user=get_current_user(), name=session['name'])

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
                return render_template('signup.html', error_msg='All fields are required',
                                       page='signup')

            # Ensure passwords match
            if not password == confirm_password:
                return render_template('signup.html', error_msg='Passwords should match',
                                       page='signup')

            # Check whether username has already been taken
            for user in users:
                if user.username == username:
                    return render_template('signup.html',
                                           error_msg='That username is already in use',
                                           page='signup')

            # Create and save the user
            user = User(username, password, firstname, lastname)
            users.append(user)

            # Redirect the new user to login page
            return redirect(url_for('login'))

    return render_template('signup.html', page='signup')


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
                session['username'] = username
                return redirect(url_for('index'))

        return render_template('login.html', error_msg='Invalid username or password')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """ Logs out a user """

    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/create_shopping_list', methods=['POST', 'GET'])
def create_shopping_list():
    """ Creates a new shopping list """

    if request.method == 'POST':
        if request.form['add_item']:
            shopping_list_name = request.form['name']
            due_date = request.form['due_date']

            print(shopping_list_name)

            user = get_current_user()

            # Create the shopping list
            my_shopping_list = ShoppingList(shopping_list_name, due_date, user.username)

            # Add the list to the user's shopping lists
            user.shopping_lists.append(my_shopping_list)

            return redirect(url_for('index'))


@app.route('/shopping-list', methods=['GET'])
def shopping_list():
    """ Shows a shopping list """

    list_name = request.args.get('shoppinglist')

    return render_template('shopping-list.html',
                           shopping_list=get_shopping_list(list_name),
                           edit=False)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    """ Adds an item to a shopping list """

    list_name = request.args.get('shoppinglist')
    item_name = request.args.get('item')

    # Add item to the shopping list
    get_shopping_list(list_name).add_item(item_name)

    return render_template('shopping-list.html',
                           shopping_list=get_shopping_list(list_name),
                           edit=False)


@app.route('/delete_shopping_list')
def delete_shopping_list():
    """ Deletes a shopping list """

    list_name = request.args.get('shoppinglist')

    # Remove the shopping list from the user's shopping lists
    get_current_user().shopping_lists.remove(get_shopping_list(list_name))

    return redirect(url_for('index'))

def get_current_user():
    """ Returns the user that is currently logged in """

    for user in users:
        if user.username == session['username']:
            return user

def get_shopping_list(name):
    """ Returns a shopping list given the name """

    for each in get_current_user().shopping_lists:
            if each.shopping_list_name == name:
                return each
