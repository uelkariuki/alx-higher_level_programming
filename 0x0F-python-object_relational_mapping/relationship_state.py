#!/usr/bin/python3

"""
python file that has a class State
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from relationship_city import Base, City
""" importing create_engine for connecting"""

Base = declarative_base()


class State(Base):
    """ class State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
