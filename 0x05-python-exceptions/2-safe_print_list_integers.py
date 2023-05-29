#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for q in range(x):
            if isinstance(my_list[q], int):
                print("{:d}".format(my_list[q]), end="")
                counter = counter + 1
    except IndexError:
        raise
    print()
    return counter
