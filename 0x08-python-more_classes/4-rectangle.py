#!/usr/bin/python3
"""
A module that handles writing a class Rectangle that
defines a rectangle by: (based on 0-rectangle.py)
Private instance attribute: width
Private instance attribute: height
Instantiation with optional width and height:\
def __init__(self, width=0, height=0):
"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property to retrieve the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter to set the private instance attribute width
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        property to retrieve the private instance atrtibute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property setter to set the private instance attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method: def area(self): that
        returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Public instance method: def perimeter(self):
        that returns the rectangle perimeter:
        """
        if (self.__height == 0) or (self.__width == 0):
            return (self.__height + self.__width) * 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """
        print() and str() should print the rectangle with
        the character #:
        """
        if (self.__width == 0) or (self.__height == 0):
            return ""
        represent_string = ""

        for q in range(self.__height):
            represent_string += "#" * self.__width + "\n"
        return represent_string.strip()

    def __repr__(self):
        """
        repr() should return a string representation of the
        rectangle to be able to recreate a
        new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"
