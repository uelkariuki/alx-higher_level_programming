#!/usr/bin/python3

"""
A module that houses a function that prints a text with 2\
        new lines after each of these characters: ., ? and :
Prototype: def text_indentation(text):
There should be no space at the beginning\
or at the end of each printed line
You are not allowed to import any module

"""


def text_indentation(text):
    """
     A function that prints a text with 2 new\
             lines after each of these characters: ., ? and :
    Args:
    text: must be a string
    Returns:
    Text with 2 new lines after each of these characters: ., ? and :
    Raises:
    TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    a = a.strip()
    print(a)
