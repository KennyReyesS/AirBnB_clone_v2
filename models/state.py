#!/usr/bin/python3
""" State Module for HBNB project """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref="states",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ Returns the list of City """
            new_list = []
            cities_dict = models.storage.all(City)
            for obj in cities_dict.values():
                if obj.state_id == self.id:
                    new_list.append(obj)
            return new_list
