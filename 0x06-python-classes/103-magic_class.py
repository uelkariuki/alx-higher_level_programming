#!/usr/bin/python3

"""
class MagicClass:
Write the Python class MagicClass that does exactly
the same as the following Python bytecode:
"""


class MagicClass:
    """ magic class """
    def __init__(self, radius=0):
        """ Disassembly of __init__ """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Disassembly of area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        circumference of magic class(circle) and
        Disassembly of circumference
        """
        return 2 * math.pi * self.__radius
