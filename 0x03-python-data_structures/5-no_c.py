#!/usr/bin/python3

def no_c(my_string):
    new_my_string = my_string.translate({ord(q): None for q in 'c' 'C'})
    return new_my_string
