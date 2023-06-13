#!/usr/bin/python3

"""
Write a function that returns the JSON representation of an object (string)
"""

import json
""" importing the json module"""


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)
    """

    json_string_representation = json.dumps(my_obj)
    return json_string_representation
