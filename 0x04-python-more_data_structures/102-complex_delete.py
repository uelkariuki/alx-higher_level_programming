#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_this = []
    for key, the_value in a_dictionary.items():
        if the_value == value:
            delete_this.append(key)
    for key in delete_this:
        del a_dictionary[key]
    return a_dictionary
