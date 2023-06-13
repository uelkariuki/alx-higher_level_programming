#!/usr/bin/python3

"""
Write a script that adds all arguments to a Python list, and
then save them to a file
"""
import sys
""" importing the sys module to use sys.argv"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
importing the save_to_json_file module to save the args to the json file
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
importing the load_from_json_file module to load the args from the json file
"""


def add_args_to_plist(filename, args):
    """
    Function to add all args to a python list and save them to a file
    """
    # load
    try:
        the_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        the_list = []

    # add
    the_list.extend(sys.argv[1:])

    # save
    save_to_json_file(the_list, "add_item.json")


# call
args = sys.argv[1:]
add_args_to_plist("add_item.json", args)
