#!/usr/bin/python3

from models import base
""" importing base """
from models import rectangle
import unittest
""" importing the unittest module"""


"""
Unit test for class Base(testing base) for Question 1
"""


class TestBase(unittest.TestCase):
    """
    class to validate that the class Base is working well
    as this class will be the "base" of other classes in this project
    """
    def test_module_documentation(self):
        """ method to ascertain that module documentation is present"""
        q1_module_doc = base.__doc__
        self.assertTrue(len(q1_module_doc) > 1,
                        "documentation for q1 module not found")

    def test_class_documentation(self):
        """ method to ascertain the class documentation is present"""
        class_doc = base.Base.__doc__
        self.assertTrue(len(class_doc) > 1,
                        "documentation for q1 class present not found")

    def test_function_documentation(self):
        """ method to ascertain the function documentation is present"""
        func_doc = base.Base.__init__.__doc__
        self.assertTrue(len(func_doc) > 1,
                        "documentation for q1 function present not found")

    def test_instance_count(self):
        """ method to ascertain the number of instances"""
        object1 = base.Base()
        object2 = base.Base()

        self.assertEqual(object2.id, 3)

        object3 = base.Base()
        object4 = base.Base()
        object5 = base.Base()

        self.assertEqual(object5.id, 6)  # 6 instances created

    def test_values(self):
        """ ascertain the values printed by Base.id representing
        the number of instances created.
        """
        b1 = base.Base()
        self.assertEqual(b1.id, 7)

        b2 = base.Base()
        self.assertEqual(b2.id, 8)

        b3 = base.Base()
        self.assertEqual(b3.id, 9)

        b4 = base.Base(12)
        self.assertEqual(b4.id, 12)

        b5 = base.Base()
        self.assertEqual(b5.id, 10)

    def test_with_no_print_arguments(self):
        """ test with no print args"""
        with self.assertRaises(NameError):
            Base()

    def test_dict_to_json_string(self):
        """ test case for the implementation
        of dictionary to json string
        """
        r1 = rectangle.Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = base.Base.to_json_string([dictionary])
        self.assertEqual(dictionary.__str__(),
                         "{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}")
        self.assertEqual(type(dictionary), dict, "<class 'dict'>")
        self.assertEqual(json_dictionary.__str__(), '[{"id": 1,\
 "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str, "<class 'str'>")


def test_init_documentation(self):
    """ method to ascertain that the init documentation is 0"""
    with open("models/__init__.py", mode="r") as file:
        file_content = file.read()
    assert len(file_content.strip() == 0,
               "package initialization __init__ must be empty")
