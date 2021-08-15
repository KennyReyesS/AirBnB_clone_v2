#!/usr/bin/python3
"""
New engine DBStorage.
"""


from models.state import BaseModel, Base
from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    classes = {
        'State': State
    }

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                               format(user, passwd, host, db),
                               pool_pre_ping=True)
        if getenv('HBNB') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return a dictionary """
        new_dict = {}
        if cls is None:
            for cls_iter in DBStorage.classes.values():
                for obj in self.__session.query(cls_iter).all():
                    new_dict[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            if cls in DBStorage.classes.values():
                for obj in self.__session.query(cls).all():
                    new_dict[obj.__class__.__name__ + "." + obj.id] = obj
                print ("se encontro")
        return new_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
