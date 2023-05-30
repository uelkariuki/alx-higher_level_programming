#!/usr/bin/python3


"""
 Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """ class square """
    def __init__(self, size=0, position=(0, 0)):
        """ Access and update private attribute """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ property def size(self): to retrieve it (getter) """
        return self.__size

    @property
    def position(self):
        """ property def position(self): to retrieve it """
        return self.__position

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

    @position.setter
    def position(self, value):

        """
        property setter def position(self, value): to set it
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value

        if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print()
            return
        for q in range(self.__position[1]):
            print()

        for q in range(self.__size):
            for r in range(self.__position[0]):
                print(" ", end="")
            for r in range(self.__size):
                print("#", end="")
            print()
