#!/usr/bin/python3

"""
python file that contains the class definition of a State and an
instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
""" importing create_engine for connecting"""

Base = declarative_base()


class State(Base):
    """ class State"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="states")
