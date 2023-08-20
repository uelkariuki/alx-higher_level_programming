#!/usr/bin/python3

"""
python file that contains the class definition of a State and an
instance Base = declarative_base():
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
""" importing create_engine for connecting"""

Base = declarative_base()


class State(Base):
    """ class State"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
