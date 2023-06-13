#!/usr/bin/python3

"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    """
    try:
        with open(filename, encoding="utf-8") as f:
            read_text = f.read()
            print(read_text)
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print("Error: {}".format(e))
