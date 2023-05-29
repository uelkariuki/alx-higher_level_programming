#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for q in range(x):
            print(my_list[q], end="")
            counter = counter + 1
    except IndexError:
        pass
    print()
    return counter
