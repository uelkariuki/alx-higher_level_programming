#!/usr/bin/python3

def islower(c):
    if len(c) != 1:
        return False
    else:
        return (ord(c) >= 97 and ord(c) <= 122)
