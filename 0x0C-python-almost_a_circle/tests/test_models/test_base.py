#!/usr/bin/python3

from models.base import Base  # """ importing base """
from models.rectangle import Rectangle  # """ importing rectangle"""
from models.square import Square  # """ importing square"""
import os  # """ import os"""
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
        q1_module_doc = Base.__doc__
        self.assertTrue(len(q1_module_doc) > 1,
                        "documentation for q1 module not found")

    def test_class_documentation(self):
        """ method to ascertain the class documentation is present"""
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc) > 1,
                        "documentation for q1 class present not found")

    def test_function_documentation(self):
        """ method to ascertain the function documentation is present"""
        func_doc = Base.__init__.__doc__
        self.assertTrue(len(func_doc) > 1,
                        "documentation for q1 function present not found")

    def test_instance_count(self):
        """ method to ascertain the number of instances"""
        object1 = Base()
        object2 = Base()

        self.assertEqual(object2.id, 19)

        object3 = Base()
        object4 = Base()
        object5 = Base()

        self.assertEqual(object5.id, 22)  # 18 instances created

    def test_values(self):
        """ ascertain the values printed by Base.id representing
        the number of instances created.
        """
        b1 = Base()
        self.assertEqual(b1.id, 23)

        b2 = Base()
        self.assertEqual(b2.id, 24)

        b3 = Base()
        self.assertEqual(b3.id, 25)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 26)

    def test_dict_to_json_string(self):
        """ test case for the implementation
        of dictionary to json string
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary.__str__(), "{'id': 17,\
 'width': 10, 'height': 7, 'x': 2, 'y': 8}")
        self.assertEqual(type(dictionary), dict, "<class 'dict'>")
        self.assertEqual(json_dictionary.__str__(), '[{"id": 17,\
 "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str, "<class 'str'>")

    def test_to_json_str_empty(self):
        """ test with an empty list"""
        empty_list = []
        json_str_1 = Base.to_json_string(empty_list)
        self.assertEqual(json_str_1.__str__(), '[]')

    def test_to_json_str_none(self):
        """ test using none list"""
        None_list = None
        json_str_1 = Base.to_json_string(None_list)

        self.assertEqual(json_str_1.__str__(), '[]')

    def test_JSON_string_to_file(self):
        """ test implementation of json string to file """
        r1_to_file = Rectangle(10, 7, 2, 8)
        r2_to_file = Rectangle(2, 4)
        Rectangle.save_to_file([r1_to_file, r2_to_file])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), '[{"id": 11,\
 "width": 10, "height": 7, "x": 2, "y": 8},\
 {"id": 12, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_empty_list_obj(self):
        """ test empty list_obj"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), '[]')

    def test_JSON_string_to_dictionary(self):
        """ test json string to dictionary"""
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
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
        json_empty_result = Base.from_json_string(empty_json)
        self.assertEqual(json_empty_result, [])

    def test_none_json_string(self):
        """ test using none string"""
        None_str = None
        None_json = Base.from_json_string(None_str)
        self.assertEqual(None_json, [])

    def test_Dictionary_to_Instance(self):
        """
        Testing the implementation of question 18 dictionary
        to instance
        """
        rect1 = Rectangle(3, 5, 1)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 1)
        r1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**r1_dict)
        self.assertEqual(rect1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(rect2.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(rect1 is rect2.__str__(), False)
        self.assertEqual(rect1 == rect2.__str__(), False)

    def test_File_to_instances(self):
        """
        Test case for the implementation of question 19 file to
        instances
        """
        R1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(R1.width, 10)
        self.assertEqual(R1.height, 7)
        self.assertEqual(R1.x, 2)
        self.assertEqual(R1.y, 8)
        R2 = Rectangle(2, 4)
        self.assertEqual(R2.width, 2)
        self.assertEqual(R2.height, 4)
        list_rectangles_input = [R1, R2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for q in range(len(list_rectangles_input)):
            self.assertEqual(str(list_rectangles_input[q]),
                             str(list_rectangles_output[q]))

        S1 = Square(5)
        self.assertEqual(S1.size, 5)
        self.assertEqual(S1.x, 0)
        self.assertEqual(S1.y, 0)
        S2 = Square(7, 9, 1)
        self.assertEqual(S2.size, 7)
        self.assertEqual(S2.x, 9)
        self.assertEqual(S2.y, 1)
        list_squares_input = [S1, S2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
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
            instance = Base.load_from_file()
            self.assertEqual(instance, [])

    def test_csv_rectangle(self):
        """
        Test case for if the implementation of csv was
        succesful, case: Rectangle
        """
        n_re1 = Rectangle(10, 7, 5, 8)
        self.assertEqual(n_re1.width, 10)
        self.assertEqual(n_re1.height, 7)
        self.assertEqual(n_re1.x, 5)
        self.assertEqual(n_re1.y, 8)

        n_re2 = Rectangle(2, 4)
        self.assertEqual(n_re2.width, 2)
        self.assertEqual(n_re2.height, 4)
        self.assertEqual(n_re2.x, 0)
        self.assertEqual(n_re2.x, 0)

        n_list_rect_input = [n_re1, n_re2]
        Rectangle.save_to_file_csv(n_list_rect_input)
        n_list_rect_output = Rectangle.load_from_file_csv()
        for rec_in, rec_out in zip(n_list_rect_input, n_list_rect_output):
            self.assertEqual(str(rec_in), str(rec_out))

    def test_csv_square(self):
        """
        Test case for if the implementation of csv was
        succesful, case: Square
        """
        squa1 = Square(5)
        self.assertEqual(squa1.size, 5)
        self.assertEqual(squa1.x, 0)
        self.assertEqual(squa1.x, 0)
        squa2 = Square(7, 9, 1)
        self.assertEqual(squa2.size, 7)
        self.assertEqual(squa2.x, 9)
        self.assertEqual(squa2.y, 1)
        list_squa_input = [squa1, squa2]
        Square.save_to_file_csv(list_squa_input)
        list_squa_output = Square.load_from_file_csv()
        for sq_in, sq_out in zip(list_squa_input, list_squa_output):
            self.assertEqual(str(sq_in), str(sq_out))

    def test_init_documentation(self):
        """ method to ascertain that the init documentation is 0"""
        with open("models/__init__.py", mode="r") as file:
            file_content = file.read()
            assert len(file_content.strip()) == 0,\
                   "package initialization __init__ must be empty"
