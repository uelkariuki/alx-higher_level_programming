#!/usr/bin/python3

"""
Integer validator: Write a class BaseGeometry (based on 6-base_geometry.py).
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
        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
