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

    @property
    def size(self):
        """ property def size(self) to retrieve (getter)"""
        return self.width  # width and height are the same for square

    @size.setter
    def size(self, value):
        """ property def size(self) to set it (setter)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ public method def update(self, *args, **kwargs)
        that assigns attributes: *args and *kwargs
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            for q in range(len(args)):
                setattr(self, attrs[q], args[q])
        elif len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ the overloading __str__ method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.size))
