#!/usr/bin/python3

"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
gettin from the module 7-base_geometry
"""


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantation with width and height
        Args:
        width: the width of rectangle
        height: the height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
