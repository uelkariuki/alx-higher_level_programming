#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(map(lambda q: replace if q == search else q, my_list))
