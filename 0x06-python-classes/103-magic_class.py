#!/usr/bin/python3

import math

"""
Write the Python class MagicClass that does exactly
the same as the following Python bytecode:
"""


class Magicclass:
    """ class magic class"""
    def __init__(self, radius=0):
        """ initializing radius"""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ area of the magic class (circle)"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ circumference of magic class(circle)"""
        return 2 * math.pi * self.__radius
