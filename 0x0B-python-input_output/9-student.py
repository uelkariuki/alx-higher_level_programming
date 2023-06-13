#!/usr/bin/python3

"""
Task 9. Student to JSON Write a class Student that defines a student by
: Public instance attributes, Public method def to_json(self):
"""


class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
