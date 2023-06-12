#!/usr/bin/python3

"""
Write a class MyInt that inherits from int:
"""


class MyInt(int):
    """ class MyInt that inherits from int"""

    def __eq__(self, other):
        """ method for the equals to operator to be inverted"""
        return self.real != other.real

    def __ne__(self, other):
        """ method for the not equals operator to be inverted"""
        return self.real == other.real
