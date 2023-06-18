#!/usr/bin/python3

"""
Write the class Square that inherits from Rectangle:
"""

from models.rectangle import Rectangle
""" importing the rectangle module to be inherited"""


class Square(Rectangle):
    """ class Sqaure that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ the class constructor for the class Square"""
        super().__init__(size, size, x, y, id)

        self.size = size

    def __str__(self):
        """ the overloading __str__ method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.size))
