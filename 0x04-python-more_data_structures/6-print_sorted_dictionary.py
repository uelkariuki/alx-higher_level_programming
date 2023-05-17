#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    the_sort = dict(sorted(a_dictionary.items()))
    for q in the_sort:
        print(q + ':', a_dictionary[q])
