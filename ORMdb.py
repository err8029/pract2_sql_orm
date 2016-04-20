from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
     __tablename__ = 'users'
     # this field will identify uniquely any user in the database
     # more info here -> http://www.w3schools.com/sql/sql_primarykey.asp
     id = Column(Integer, primary_key=True)
     username = Column(String)
     fullname = Column(String)
     email = Column(String)
     password = Column(String)

     def __repr__(self):
        return "<user(username='%s', fullname="%s" ,="" email="%s" password="%s" )="">" % (
                             self.username, self.fullname, self.email, self.password)
				    </user(username='%s',>


     path_to_db = "mydatabase.db"
     engine = create_engine('sqlite:///' + path_to_db)
     Base.metadata.create_all(engine)


