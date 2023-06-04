#!/usr/bin/python3

"""
Write a function that adds 2 integers.
Prototype: def add_integer(a, b=98):
Default value of b is 98 unless otherwise
"""


def add_integer(a, b=98):
    """ A function that adds two integers
    Arguments:
    a and b must be integers or floats, otherwise raise a
    TypeError exception with the message `a` must be an integer
    or `b` must be an integer
    a and b must be first casted to integers if they are float
    Returns:
    An integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, (float)):
        a = int(a)
    if not isinstance(b, (float)):
        b = int(b)
    return a + b
