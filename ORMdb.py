from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
     
     #same operation as CREATE TABLE in SQL but ORM 
     __tablename__ = 'users'
     id = Column(Integer, primary_key=True)
     username = Column(String)
     fullname = Column(String)
     email = Column(String)
     password = Column(String)

     def __init__(self, username, fullname, email, password):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = password
        
     def __repr__(self):
        return "<user(username='%s', fullname='%s' , email='%s' password='%s' )>" % (
                             self.username, self.fullname, self.email, self.password)


     #we specify the path and create engine
     path_to_db = "mydatabase.db"
     engine = create_engine('sqlite:///' + path_to_db)
     Base.metadata.create_all(engine)
