#!/usr/bin/python3

""" Write the class Rectangle that inherits from Base: """

from models.base import Base
""" importing Base to be inherited by Rectangle"""


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
            raise ValueError("x must be >= 0")
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
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ public method def area(self):
        that returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        public method def display(self):that prints in
        stdout the Rectangle instance with the character # - you
        don’t need to handle x and y here.
        """

        for a in range(self.y):
            print()
        for q in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """ over riding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ public method def update(self, *args):
        that assigns an argument to each attribute:
        """
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for q in range(len(args)):
                setattr(self, attrs[q], args[q])
        elif len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method def to_dictionary(self):
        that returns the dictionary representation of a Rectangle:
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
