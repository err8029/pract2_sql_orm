from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_user')
def insert_user():
    return render_template('insert_user.html')

@app.route('/show_users')
def show_users():
    return render_template('show_users.html')

@app.route('/login')
def login_form():
    return render_template('login_form.html')


if __name__=="__main__":
    app.run('0.0.0.0')
