#!/usr/bin/python3

"""
Write a function that creates an Object from a “JSON file”:
"""

import json
""" importing from the json module"""


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data
