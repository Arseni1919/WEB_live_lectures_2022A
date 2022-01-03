from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session
import requests
import random
from interact_with_DB import *

app = Flask(__name__)
app.secret_key = '12345'


@app.route('/hello/world')
def hello_world():  # put application's code here
    return 'Hello World 2!'


@app.route('/about')
def about_func():
    # DO SOMETHING WITH DB
    return render_template('about.html',
                           profile={'name': 'Arseni',  'second_name': 'Perchik'},
                           university='BGU',
                           degrees=['BSc', 'MSc'],
                           hobbies=('art', 'music'))


@app.route('/catalog')
def catalog_func():
    if 'user_inside' in session:
        if session['user_inside']:
            print('user inside')
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html', p_name=product, p_size=size)
    return render_template('catalog.html')


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
    # DB
    found = True
    if found:
        return render_template('index.html', name='Arseni')
    else:
        return render_template('index.html')


@app.route('/logout')
def logout_func():

    session['username'] = ''
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # DB
        found = True
        if found:
            session['username'] = username
            session['user_inside'] = True
            return redirect(url_for('home_func'))
        else:
            return render_template('login.html')

# ------------------------------------------------- #
# -------------------- USERS ---------------------- #
# ------------------------------------------------- #


@app.route('/users')
def users_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)
# @app.route('/users')
# def users_func():
#     query = "select * from users"
#     query_result = interact_db(query=query, query_type='fetch')
#     return render_template('pages/users/templates/users.html', users=query_result)
# ------------------------------------------------- #
# ------------------------------------------------- #


# @app.route('/hide_users')
# def hide_users_func():
#     session['users'] = ''
#     return redirect(url_for('users_func'))


# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #
# @app.route('/select_users')
# def select_users_func():
#     query = "select * from users"
#     query_result = interact_db(query=query, query_type='fetch')
#     session['users'] = query_result
#     return redirect(url_for('users_func'))


# ------------------------------------------------- #
# ------------------------------------------------- #

@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    # get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # insert to db
    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s');" % (name, email, password)
    interact_db(query=query, query_type='commit')

    # come back to users
    return redirect('/users')

# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #

# @app.route('/insert_user', methods=['POST'])
# def insert_user_func():
#     name = request.form['name']
#     email = request.form['email']
#     password = request.form['password']
#
#     query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
#     interact_db(query=query, query_type='commit')
#     return redirect('/users')


# @app.route('/insert_user', methods=['GET', 'POST'])
# def insert_user():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         # recheck
#         query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
#         interact_db(query=query, query_type='commit')
#     return redirect(url_for('select_users_func'))


# ------------------------------------------------- #
# ------------------------------------------------- #

@app.route('/delete_user', methods = ['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/users')

# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
# @app.route('/delete_user', methods=['POST'])
# def delete_user_func():
#     user_id = request.form['id']
#     query = "DELETE FROM users WHERE id='%s';" % user_id
#     interact_db(query, query_type='commit')
#     return redirect('/users')

# @app.route('/delete_user', methods=['POST'])
# def delete_user():
#     user_id = request.form['id']
#     query = "DELETE FROM users WHERE id='%s';" % user_id
#     interact_db(query, query_type='commit')
#     return redirect(url_for('select_users_func'))


# ------------------------------------------------- #
# ------------------------------------------------- #

@app.route('/req_frontend')
def req_frontend_func():
    return render_template('req_frontend.html')


# def get_pockemons(num=3):
#     pockemons = []
#     for i in range(num):
#         random_n = random.randint(1, 100)
#         res = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{random_n}')
#         res = res.json()
#         pockemons.append(res)
#     return pockemons

def get_pockemons(num):
    pokemons = []
    for i in range(num):
        random_n = random.randint(1, 100)
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_n}')
        # res = requests.get('https://pokeapi.co/api/v2/pokemon/%s' % random_n)
        res = res.json()
        pokemons.append(res)
    return pokemons


@app.route('/req_backend')
def req_backend_func():
    num = 3
    if "number" in request.args:
        num = int(request.args['number'])
    pockemons = get_pockemons(num)
    return render_template('req_backend.html', pockemons=pockemons)


if __name__ == '__main__':
    app.run(debug=True)
