#!/usr/bin/python3
"""
A module to handle the printing of My name is <first name> <last name>
Prototype: def say_my_name(first_name, last_name=""):
You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """
    This Function prints My name is <first name> <last name>
    Arguments:
    first_name: the first name to be printed
    last_name: to be printed (default is an empty string)
    Returns:
    My name is <first name> <last name>
    Raises:
    TypeError: if first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
