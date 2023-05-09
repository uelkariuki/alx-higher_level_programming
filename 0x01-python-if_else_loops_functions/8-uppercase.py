#!/usr/bin/python3

def uppercase(str):
    the_result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            the_result = the_result + chr(ord(char) - 32)
        else:
            the_result = the_result + char
    print("{}\n".format(the_result))
