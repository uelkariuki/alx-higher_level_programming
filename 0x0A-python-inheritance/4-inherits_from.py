#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Function: inherits_from
    Args:
    obj: the object to be verified
    a_class: the class to verify from
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
