#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import *


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """ returns the list of Review instances  """
            new_list = []
            reviews_dict = models.storage.all(Review)
            for obj in reviews_dict.values():
                if obj.place_id == self.id:
                    new_list.append(obj)
            return new_list

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on amenity_ids """
            new_list = []
            amenities_dict = models.storage.all(Amenity)
            for obj in amenities_dict.values():
                if obj.id == self.amenity_ids:
                    new_list.append(obj)
            return new_list

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding an Amenity.id to amenity_ids"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
