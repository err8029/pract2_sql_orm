from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy_declarative import User, Base

class ORM():

    def __init__(self):
        path_to_dabase = 'mydatabase.db'
        engine = create_engine('sqlite:///'+path_to_database, echo=True)
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def insert_user(self,username,fullname,email,password):
        new_user = User(username='%s', fullname='%s', email='%s', password='%s'),(username,fullname,email,password)
        session.add(new_user)
        session.commit()
        exist=False
        return exist
