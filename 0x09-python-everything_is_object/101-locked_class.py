#!/usr/bin/python3

"""
Write a class LockedClass with no class or
object attribute, that prevents the user from dynamically
creating new instance attributes, except if the new instance
attribute is called first_name.
"""


class LockedClass:
    """ class LOckedClass """
    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"'{self.__class__.__name__}'\
 object has no attribute '{name}'")
        super().__setattr__(name, value)
