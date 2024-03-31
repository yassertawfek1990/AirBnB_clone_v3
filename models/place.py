#!/usr/bin/python
""" holds class Place"""
import os
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id')),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id',
                                            ondelete="CASCADE")))



class Place(BaseModel, Base):
    """Representation of Place """
    if models.storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if storage_type != "db":
        @property
        def amenities(self):
            """
            ammenities getter
            :return: list of amenitites
            """
            amenity_objs = []

            for a_id in self.amenity_ids:
                amenity_objs.append(models.storage.get("Amenity", str(a_id)))

            return amenity_objs

        @amenities.setter
        def amenities(self, amenity):
            """
            ammenities setter
            :return:
            """
            self.amenity_ids.append(amenity.id)

        @property
        def reviews(self):
            """
            reviews getter
            :return: list of reviews
            """
            all_reviews = models.storage.all("Review")
            place_reviews = []

            for review in all_reviews.values():
                if review.place_id == self.id:
                    place_reviews.append(review)

            return place_reviews
