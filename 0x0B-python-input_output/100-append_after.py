#!/usr/bin/python3

"""
Write a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
