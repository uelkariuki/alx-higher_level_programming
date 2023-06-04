#!/usr/bin/python3

"""
This module houses a function that prints a square with
the character #
Prototype: def print_square(size):
You are not allowed to import any module
"""


def print_square(size):
    """
    This function prints a square with the character #
    Args:
    size is the size length of the square
    Returns:
    a square with the character #
    Raises:
        TypeError:
                    1. If size is not an integer
                    2. if size is a float and is less than 0
        ValueError:
                    1.if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print("")
