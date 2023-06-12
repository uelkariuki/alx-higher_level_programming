#!/usr/bin/python3

"""
Write a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Function that adds a new attribute to an object if it’s possible:
    Args:
    obj: the object to which the attribute is to be added
    attr_name: the attribute name
    attr_value: the attribute value
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
