from flask import Flask, redirect, url_for, request
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_user')
def insert_user():
    return render_template('insert_user.html')

@app.route('/user_register', methods=['POST'])
def user_register():
    conn = sqlite3.connect('mydatabase.db')
    username = request.form.get('username')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    cursor=conn.execute("insert into users (username,fullname,email,password) values (?, ?, ?, ?)",
                       (username,
                        fullname,
                        email,
                        password))
    conn.commit()
    conn.close()
    return render_template('user_inserted.html',
                           username=username,
                           fullname=fullname,
                           email=email,
                           password=password)

@app.route('/show_users')
def show_users():
    conn = sqlite3.connect('mydatabase.db')
    cursor=conn.execute("select username,fullname,email,password from users")
    data=[row for row in cursor]
    conn.close()
    return render_template('show_users.html',
                           data=data)

@app.route('/login')
def login_form():
    return render_template('login_form.html')

@app.route('/user_login',  methods=['POST'])
def user_login():
    conn = sqlite3.connect('mydatabase.db')
    username = request.form.get('username')
    password = request.form.get('password')
    cursor = conn.execute("select username,password,email,fullname from users")
    acces = [row for row in cursor]
    enter = None 
    for userdata in acces:
        (dbuser,dbpass,dbemail,dbfullname) = userdata
        if (dbuser == username and dbpass == password):
            enter=True
            break
    conn.close()
    return render_template('login.html',
                           enter=enter,
                           username = dbuser,
                           password = dbpass,
                           email = dbemail,
                           fullname = dbfullname)


if __name__=="__main__":
    app.run('0.0.0.0')
