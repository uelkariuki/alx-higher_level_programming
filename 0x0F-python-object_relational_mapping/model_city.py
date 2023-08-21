#!/usr/bin/python3

"""
Python file similar to model_state.py named model_city.py that
contains the class definition of a City.
"""
import sys
from sqlalchemy import ForeignKey
# from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
""" importing create_engine for connecting"""

Base = declarative_base()


class City(Base):
    """ class City"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
