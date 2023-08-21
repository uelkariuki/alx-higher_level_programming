#!/usr/bin/python3

"""
Python file similar to model_state.py named model_city.py that
contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
""" importing create_engine for connecting"""

Base = declarative_base()


class City(Base):
    """ class City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
