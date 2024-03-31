#!/usr/bin/python
""" holds class City"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
import models
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    if storage_type != 'db':
        @property
        def places(self):
            """
            getter for places
            :return: list
            """
            all_places = models.storage.all("Place")

            result = []

            for obj in all_places.values():
                if str(obj.city_id) == str(self.id):
                    result.append(obj)

            return result
