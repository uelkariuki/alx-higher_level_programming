#!/usr/bin/python3

"""
Improve the files model_city.py and save them as relationship_city.py
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
""" importing required modules for connecting"""

Base = declarative_base()


class City(Base):
    """ class City"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
