#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sorted_dict = sorted(a_dictionary)
    return sorted_dict[-1]
