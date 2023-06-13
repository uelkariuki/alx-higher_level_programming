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
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []
    append_now = False

    for line in lines:
        new_lines.append(line.rstrip())

        if search_string in line:
            append_now = True

        if append_now:
            new_lines.append(new_string)
            append_now = False

        new_text = "\n".join(new_lines)

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(new_text)
