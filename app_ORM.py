import sys
from flask import Flask, request
from flask import render_template
from ORMmethods import ORM

app = Flask(__name__)
# HOME PAGE.
@app.route('/')
def index():
    return render_template('index.html')

#Insert user page
@app.route('/insert_user')
def insert_user():
    return render_template('insert_user.html')

#returns user inserted page if insert succesful
@app.route('/user_register', methods=['POST'])
def user_register():
    username = request.form.get('username')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    new_insert = ORM()
    exist = new_insert.insert_userORM(""+username,""+fullname,""+email,""+password)
    print exist
    return render_template('user_inserted.html',
                           username=username,
                           fullname=fullname,
                           email=email,
                           password=password,
                           exist=exist)

@app.route('/show_users', methods=['POST','GET'])
# Delete doesnt work with ORM
def show_users():
    if request.method=='GET':
        show_users = ORM()
    if request.method=='POST':
        delete = request.form.get('delete')
        if delete=="True":
            return render_template('index.html')
    data = show_users.show_usersORM()
    return render_template('show_users.html',
                           data=data)

@app.route('/login')
def login_form():
    return render_template('login_form.html')

@app.route('/user_login',  methods=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    new_login = ORM()
    (enter,dbuser,dbpass,dbemail,dbfullname) = new_login.loginORM(""+username,""+password)
    return render_template('login.html',
                           enter=enter,
                           username = dbuser,
                           password = dbpass,
                           email = dbemail,
                           fullname = dbfullname)


if __name__=="__main__":
    app.run('0.0.0.0')
