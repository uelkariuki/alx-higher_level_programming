#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True or False depending
    on if it is an instance
    Args:
    obj: the object to be verified
    a_class: the class to verify from
    """
    if isinstance(obj, a_class):
        return True
    return False
