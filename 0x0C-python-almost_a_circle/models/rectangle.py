#!/usr/bin/python3

""" Write the class Rectangle that inherits from Base: """

from models.base import Base
""" importing Base """


class Rectangle(Base):
    """ Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor with Private instance attributes
        width, height, x, y
        """
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ property def width(self) to retrieve (getter)"""
        return self.__width

    @width.setter
    def width(self, value):
        """ property def width(self) to set it (setter)"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ property def height(self) to retrieve (getter)"""
        return self.__height

    @height.setter
    def height(self, value):
        """ property def height(self) to set it (setter)"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0") 

        self.__height = value

    @property
    def x(self):
        """ property def x(self) to retrieve (getter)"""
        return self.__x

    @x.setter
    def x(self, value):
        """ property def x(self) to set it (setter)"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ property def y(self) to retrieve (getter)"""
        return self.__y

    @y.setter
    def y(self, value):
        """ property def y(self) to set it (setter)"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be > 0")

        self.__y = value
