#!/usr/bin/python3

"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        read_text = file.read()
        print(read_text)
