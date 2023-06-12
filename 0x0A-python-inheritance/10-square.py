#!/usr/bin/python3

"""
Write a class Square that inherits from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle
""" class Rectangle that the square class will inherit from"""


class Square(Rectangle):
    """ class square that inherits from Rectangle"""
    def __init__(self, size):
        """ Instantiation with size
        Args:
        size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
