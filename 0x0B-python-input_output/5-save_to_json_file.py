#!/usr/bin/python3

"""
Write a function that writes an Object to a text file,
using a JSON representation:
"""

import json
""" importing the json module"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation:
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
