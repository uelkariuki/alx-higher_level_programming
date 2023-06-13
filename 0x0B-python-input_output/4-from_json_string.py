#!/usr/bin/python3

"""
Write a function that returns an object (Python data structure)
represented by a JSON string
"""

import json
""" importing the json module"""


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string
    """
    return (json.loads(my_str))
