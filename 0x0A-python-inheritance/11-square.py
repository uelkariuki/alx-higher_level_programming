#!/usr/bin/python3

"""
Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
the class Rectangle
"""


class Square(Rectangle):
    """ class square that inherits from Rectangle"""
    def __init__(self, size):
        """ Instantiation with size
        Args:
        size: the size of the square
        """
        super().__init__(size, size)
        self.__size = size


    def __str__(self):
        """ 
        print() should print, and str() should return,
        the square description: [Square] <width>/<height>
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
