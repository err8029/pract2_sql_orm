from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#we import the 2 main parameters of our virtual ORM db 
from ORMdb import User, Base

class ORM():

    #initialize the engine and the session parameters
    def __init__(self):
        self.path_to_database = 'mydatabase.db'
        self.engine = create_engine('sqlite:///'+self.path_to_database, echo=True)
        Base.metadata.create_all(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    #method for inserting the user to the ORM virtual db
    def insert_userORM(self,username,fullname,email,password):
        #----------check user abiability--------------------------------------------------
        exist = None
        for log in self.session.query(User.username, User.password, User.email, User.fullname).\
            filter(User.username == username):
                exist = True
        #----------------------------------------------------------------------------------
        if exist == None:
            new_user = User(str(username),str(fullname),str(email), str(password))
            self.session.add(new_user)
            self.session.commit()
        return exist

    #method that returns the users contained in the ORM virtual db
    def show_usersORM(self):
        data = list()
        for row in self.session.query(User.username, User.password, User.email, User.fullname):
            data.append(row)
        return data

    #method for comparing the username and password introduced with the db ones and then return all the user data if there is a match
    def loginORM(self,username,password):
        login = None
        (dbuser,dbpass,dbemail,dbfullname) =(None, None, None, None)
        for log in self.session.query(User.username, User.password, User.email, User.fullname).\
            filter(User.username == username, User.password == password):
                (dbuser,dbpass,dbemail,dbfullname) = log
                login = True
        return (login, dbuser,dbpass,dbemail,dbfullname)






