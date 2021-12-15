from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


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



if __name__ == '__main__':
    app.run(debug=True)
