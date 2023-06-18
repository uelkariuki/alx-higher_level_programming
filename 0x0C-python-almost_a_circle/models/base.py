#!/usr/bin/python3

"""
Write the first class Base: (Question 1)
"""
import json
""" importing json"""
import os
""" importing os to check if file exists"""


class Base:
    """ class Base"""
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor"""
        if id is not None:
            self.id = id
        else:
            Base._Base__nb_objects += 1
            self.id = Base._Base__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Update the class Base by adding the static
        method def to_json_string(list_dictionaries):
        that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            if type(list_dictionaries[0]) is dict:
                return json.dumps(list_dictionaries)
            else:  # convert to dictionary first
                return json.dumps([obj.to_dictionary()
                                  for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method def save_to_file(cls, list_objs): that
        writes the JSON string representation of list_objs to
        a file:
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        static method def from_json_string(json_string):
        that returns the list of the JSON string
        representation json_string:
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            if type(json_string) is str:
                return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method def create(cls, **dictionary): that
        returns an instance with all attributes already set:
        """
        dummy_instance = cls(1, 1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """
        update method to be called to the dummy instance to
        apply the real values
        """
        for key, value in dictionaty.items():
            return (self, key, value)

    @classmethod
    def load_from_file(cls):
        """
        class method def load_from_file(cls): that
        returns a list of instances:
        """
        filename = "{}.json".format(cls.__name__)
        total_instances = []
        if not os.path.isfile(filename):
            return total_instances
        else:
            with open(filename, "r") as f:
                json_data = f.read()
                dictionary_data = cls.from_json_string(json_data)
                for items in dictionary_data:
                    instance = cls.create(**items)
                    total_instances.append(instance)

        return total_instances
