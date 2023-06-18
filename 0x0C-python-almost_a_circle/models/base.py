#!/usr/bin/python3

"""
Write the first class Base: (Question 1)
"""
import json
""" importing json"""


class Base:
    """ class Base"""
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor"""
        if id is not None:
            self.id = id
        else:
            Base._Base__nb_objects += 1
            self.id = Base._Base__nb_objects

    def to_json_string(list_dictionaries):
        """
        Update the class Base by adding the static
        method def to_json_string(list_dictionaries):
        that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
