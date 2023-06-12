#!/usr/bin/python3

"""
Write a class MyList that inherits from list:
"""


class MyList(list):
    """
    child class named class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method: def print_sorted(self):
        that prints the list, but sorted (ascending sort)
        """
        for elem in self:
            result = sorted(self)
        print(result)
