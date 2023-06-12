#!/usr/bin/python3

"""
Write a function that returns the list of available attributes
and methods of an object:
"""


def lookup(obj):
    """
    lookup function to list the available attributes and methods of an object
    """
    return dir(obj)
