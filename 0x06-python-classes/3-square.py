#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """ class square """
    def __init__(self, size=0):
        """
        defines a square by private instance attribute `size`
        and instantation with optional size:
        def __init__(self, size=0):
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return self.__size ** 2
