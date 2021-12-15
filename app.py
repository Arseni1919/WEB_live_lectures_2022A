from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session

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


if __name__ == '__main__':
    app.run(debug=True)
