import sys
from flask import Flask, request
from flask import render_template
from ORMmethods import ORM

app = Flask(__name__)

def get_userORM():
    engine = create_engine('sqlite:///'+path_to_database, echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.query(User.username.label('username_label')).all()
    session.query(User.fullname.label('fullname_label')).all()
    session.query(User.email.label('e_label')).all()
    data = session.query(User.username, User.fullname, User.email, User.password).all()
    return data

def save_userORM(username, fullname, email, password):
    engine = create_engine('sqlite:///'+path_to_database)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_user = User(username, fullname, email, password)
    session.add(ed_user)
    session.commit()

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
