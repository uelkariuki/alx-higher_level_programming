#!/usr/bin/python3

def islower(c):
    if len(c) != 1:
        return False

    the_ascii = ord(c)

    if (97 <= the_ascii <= 122):
        return True
    return False
