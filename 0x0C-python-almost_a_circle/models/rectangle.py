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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ property def width(self) to retrieve (getter)"""
        return self.__width

    @width.setter
    def width(self):
        """ property def width(self) to set it (setter)"""
        self.width = width

    @property
    def height(self):
        """ property def height(self) to retrieve (getter)"""
        return self.__height

    @height.setter
    def height(self):
        """ property def height(self) to set it (setter)"""
        self.height = height

    @property
    def x(self):
        """ property def x(self) to retrieve (getter)"""
        return self.__x

    @x.setter
    def x(self):
        """ property def x(self) to set it (setter)"""
        self.x = x

    @property
    def y(self):
        """ property def y(self) to retrieve (getter)"""
        return self.__y

    @y.setter
    def y(self):
        """ property def y(self) to set it (setter)"""
        self.y = y
