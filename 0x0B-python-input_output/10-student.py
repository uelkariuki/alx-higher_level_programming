#!/usr/bin/python3

"""
Write a class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method that retrieves a dictionary
        representation of a Student instance
        """
        if attrs is not None and isinstance(attrs, list)\
                and all(isinstance(attr_elem, str) for attr_elem in attrs):
            return {attr_elem: getattr(self, attr_elem)
                    for attr_elem in attrs if hasattr(self, attr_elem)}
        else:
            return self.__dict__
