#!/usr/bin/python3

"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class BaseGeometry:
    """
    class  BaseGeometry
    """

    def area(self):
        """
        Public instance method that raises an
        Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate integers
        """
        self.name = name
        self.value = value
        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantation with width and height
        """
        self.__width = width
        self.__height = height

        width = self.integer_validator("width", width)
        height = self.integer_validator("height", height)
