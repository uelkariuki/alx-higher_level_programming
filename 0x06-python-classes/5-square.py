#!/usr/bin/python3

"""
 Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """ class square """
    def __init__(self, size=0):
        """ Access and update private attribute """
        self.__size = size

    @property
    def size(self):
        """ property def size(self): to retrieve it (getter) """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter def size(self, value): to set it (setter)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method: def area(self): that returns
        the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method: def my_print(self): that prints
        in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        if (self.__size == 0):
            print("")
        for q in range(self.__size):
            for q in range(self.__size):
                print("#", end="")
            print()
