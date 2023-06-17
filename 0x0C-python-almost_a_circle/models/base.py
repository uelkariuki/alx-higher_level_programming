#!/usr/bin/python3

"""
Write the first class Base: (Question 1)
"""


class Base:
    """ class Base"""
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor"""
        if id is not None:
            self.id = id
        else:
            Base._Base__nb_objects += 1
            self.id = Base._Base__nb_objects
