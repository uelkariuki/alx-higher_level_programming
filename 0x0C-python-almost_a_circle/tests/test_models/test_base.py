#!/usr/bin/python3

from models import base
""" importing base """
from models import rectangle
""" importing rectangle"""
from models import square
""" importing square"""
import os
""" import os"""
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

        self.assertEqual(object2.id, 15)

        object3 = base.Base()
        object4 = base.Base()
        object5 = base.Base()

        self.assertEqual(object5.id, 18)  # 18 instances created

    def test_values(self):
        """ ascertain the values printed by Base.id representing
        the number of instances created.
        """
        b1 = base.Base()
        self.assertEqual(b1.id, 19)

        b2 = base.Base()
        self.assertEqual(b2.id, 20)

        b3 = base.Base()
        self.assertEqual(b3.id, 21)

        b4 = base.Base(12)
        self.assertEqual(b4.id, 12)

        b5 = base.Base()
        self.assertEqual(b5.id, 22)

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
        self.assertEqual(dictionary.__str__(), "{'id': 13,\
 'width': 10, 'height': 7, 'x': 2, 'y': 8}")
        self.assertEqual(type(dictionary), dict, "<class 'dict'>")
        self.assertEqual(json_dictionary.__str__(), '[{"id": 13,\
 "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str, "<class 'str'>")

    def test_to_json_str_empty(self):
        """ test with an empty list"""
        empty_list = []
        json_str_1 = base.Base.to_json_string(empty_list)
        self.assertEqual(json_str_1.__str__(), '[]')

    def test_to_json_str_none(self):
        """ test using none list"""
        None_list = None
        json_str_1 = base.Base.to_json_string(None_list)

        self.assertEqual(json_str_1.__str__(), '[]')

    def test_JSON_string_to_file(self):
        """ test implementation of json string to file """
        r1_to_file = rectangle.Rectangle(10, 7, 2, 8)
        r2_to_file = rectangle.Rectangle(2, 4)
        rectangle.Rectangle.save_to_file([r1_to_file, r2_to_file])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), '[{"id": 11,\
 "width": 10, "height": 7, "x": 2, "y": 8},\
 {"id": 12, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_empty_list_obj(self):
        """ test empty list_obj"""
        rectangle.Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), '[]')

    def test_JSON_string_to_dictionary(self):
        """ test json string to dictionary"""
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = rectangle.Rectangle.to_json_string(list_input)
        list_output = rectangle.Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list,
                         "[<class 'list'>] [{'height': 4,\
 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]")
        self.assertEqual(type(json_list_input), str,
                         "[<class 'str'>] [{\"height\": 4, \"width\": 10,\
 \"id\": 89}, {\"height\": 7, \"width\": 1, \"id\": 7}]")
        self.assertEqual(type(list_output), list,
                         "[<class 'list'>] [{'height': 4, 'width': 10,\
 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]")
        self.assertEqual(len(list_input), len(list_output))
        self.assertEqual(list_input[0]['id'], list_output[0]['id'])
        self.assertEqual(list_input[1]['width'], list_output[1]['width'])
        for q in range(len(list_output)):
            self.assertDictEqual(list_input[q], list_output[q])

    def test_empty_json_string(self):
        """ test empty json string"""
        empty_json = "[]"
        json_empty_result = base.Base.from_json_string(empty_json)
        self.assertEqual(json_empty_result, [])

    def test_none_json_string(self):
        """ test using none string"""
        None_str = None
        None_json = base.Base.from_json_string(None_str)
        self.assertEqual(None_json, [])

    def test_Dictionary_to_Instance(self):
        """
        Testing the implementation of question 18 dictionary
        to instance
        """
        rect1 = rectangle.Rectangle(3, 5, 1)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 1)
        r1_dict = rect1.to_dictionary()
        rect2 = rectangle.Rectangle.create(**r1_dict)
        self.assertEqual(rect1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(rect2.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(rect1 is rect2.__str__(), False)
        self.assertEqual(rect1 == rect2.__str__(), False)

    def test_File_to_instances(self):
        """
        Test case for the implementation of question 19 file to
        instances
        """
        R1 = rectangle.Rectangle(10, 7, 2, 8)
        self.assertEqual(R1.width, 10)
        self.assertEqual(R1.height, 7)
        self.assertEqual(R1.x, 2)
        self.assertEqual(R1.y, 8)
        R2 = rectangle.Rectangle(2, 4)
        self.assertEqual(R2.width, 2)
        self.assertEqual(R2.height, 4)
        list_rectangles_input = [R1, R2]
        rectangle.Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = rectangle.Rectangle.load_from_file()
        for q in range(len(list_rectangles_input)):
            self.assertEqual(str(list_rectangles_input[q]),
                             str(list_rectangles_output[q]))

        S1 = square.Square(5)
        self.assertEqual(S1.size, 5)
        S2 = square.Square(7, 9, 1)
        self.assertEqual(S2.size, 7)
        self.assertEqual(S2.x, 9)
        self.assertEqual(S2.y, 1)
        list_squares_input = [S1, S2]
        square.Square.save_to_file(list_squares_input)
        list_squares_output = square.Square.load_from_file()
        for q in range(len(list_squares_input)):
            self.assertEqual(str(list_squares_input[q]),
                             str(list_squares_output[q]))

    def test_file_not_exist(self):
        """
        Test case for If the file doesn’t exist, return
        an empty list
        """
        filename = "no_file.json"
        if not os.path.isfile(filename):
            instance = base.Base.load_from_file()
            self.assertEqual(instance, [])


def test_init_documentation(self):
    """ method to ascertain that the init documentation is 0"""
    with open("models/__init__.py", mode="r") as file:
        file_content = file.read()
    assert len(file_content.strip() == 0,
               "package initialization __init__ must be empty")
