from flask import Flask, redirect, url_for, request
from flask import render_template
import sqlite3
from ORMmethods import ORM


app = Flask(__name__)

#---------------SQL functions in order to select and insert------------------------

# This function select the differents parameters within our database in line users.
def get_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("select username,password,email,fullname from users")
    acces = [row for row in cursor]
    conn.close()
    return acces

# This function insert the different values in our databases.
def set_data(username,fullname,email,password):
    conn = sqlite3.connect('mydatabase.db')
    cursor=conn.execute("insert into users (username,fullname,email,password) values (?, ?, ?, ?)",
                       (username,
                        fullname,
                        email,
                        password))
    conn.commit()
    conn.close()

#delete function optional (it deletes all users from the table)
def delete_all():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("delete from users")
    conn.commit()
    conn.close()

#---------------ORM functions in order to select and insert------------------------
def get_dataORM():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("select username,password,email,fullname from users")
    acces = [row for row in cursor]
    conn.close()
    return acces





#-------------------------------App methods----------------------------------------
# HOME PAGE.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_user')
def insert_user():
    return render_template('insert_user.html')

# In this function insert different parameters and compared with all existing.
def user_exist_and_insert(data,username,fullname,email,password):
    exist = None
    for userdata in data:
        (dbuser,dbpass,dbemail,dbfullname) = userdata
        if (username == dbuser):
            exist = True
            break
    if (exist != True):
        set_data(username,fullname,email,password)
    return exist

@app.route('/user_register', methods=['POST'])
def user_register():
    username = request.form.get('username')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    exist=ORM.insert_user(username,fullname,email,password)
    print exist
    return render_template('user_inserted.html',
                           username=username,
                           fullname=fullname,
                           email=email,
                           password=password,
                           exist=exist)

@app.route('/show_users', methods=['POST','GET'])
# We show different users with the GET method and eliminate the parameters with POST method.
def show_users():
    delete="False"
    if request.method=='GET':
        data=get_data()
    if request.method=='POST':
        delete = request.form.get('delete')
        if delete=="True":
            delete_all()
            return render_template('index.html')
    return render_template('show_users.html',
                           data=data)

@app.route('/login')
def login_form():
    return render_template('login_form.html')
# In this function we make a search in our list and if it matches, the values are returned
def login(acces,username,password):
    enter = None
    for userdata in acces:
        (dbuser,dbpass,dbemail,dbfullname) = userdata
        if (dbuser == username and dbpass == password):
            enter=True
            break
    return enter,dbuser,dbpass,dbemail,dbfullname

@app.route('/user_login',  methods=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    acces = get_data()
    (enter,dbuser,dbpass,dbemail,dbfullname)=login(acces,username,password)
    return render_template('login.html',
                           enter=enter,
                           username = dbuser,
                           password = dbpass,
                           email = dbemail,
                           fullname = dbfullname)


if __name__=="__main__":
    app.run('0.0.0.0')
