#!/usr/bin/python3

import unittest
""" importing the unittest module"""
from models import rectangle
""" importing rectangle from models"""

"""
Write the class Rectangle that inherits from Base: Question 2: First Rectangle
"""


class TestRectangle(unittest.TestCase):
    """
    class to validate that the class Rectangle is working well
    """
    def test_module_documentation(self):
        """ method to ascertain the module documentation is present"""
        q2_module_doc = rectangle.__doc__
        self.assertTrue(len(q2_module_doc) > 1,
                        "documentation for q2 module not found")

    def test_class_documentation(self):
        """ method to ascertain the class documentation is present"""
        class_doc = rectangle.Rectangle.__doc__
        self.assertTrue(len(class_doc) > 1,
                        "documentation for q2 class present not found")

    def test_function_documentation(self):
        """ method to ascertain the function documentation is present"""
        func_doc = rectangle.Rectangle.__init__.__doc__
        self.assertTrue(len(func_doc) > 1,
                        "documentation for q2 function present not found")

    def test_values(self):
        """ ascertain the values printed by Rectangle.id representing
        the number of instances created.
        """
        r1 = rectangle.Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = rectangle.Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = rectangle.Rectangle(2, 10, 0)
        self.assertEqual(r3.id, 3)
        r4 = rectangle.Rectangle(2, 10, 0, 0)
        self.assertEqual(r4.id, 4)
        r5 = rectangle.Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r5.id, 12)
        rec = rectangle.Rectangle(20, 30)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        rec1 = rectangle.Rectangle(20, 30, 2, 7, 15)
        self.assertEqual(rec1.width, 20)
        self.assertEqual(rec1.height, 30)
        self.assertEqual(rec1.x, 2)
        self.assertEqual(rec1.y, 7)
        self.assertEqual(rec1.id, 15)

        area_rec = rectangle.Rectangle(3, 2)
        self.assertEqual(area_rec.width, 3)
        self.assertEqual(area_rec.height, 2)
        self.assertEqual(area_rec.area(), 6)
        area_rec_1 = rectangle.Rectangle(2, 10)
        self.assertEqual(area_rec_1.width, 2)
        self.assertEqual(area_rec_1.height, 10)
        self.assertEqual(area_rec_1.area(), 20)
        area_rec_2 = rectangle.Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(area_rec_2.width, 8)
        self.assertEqual(area_rec_2.height, 7)
        self.assertEqual(area_rec_2.area(), 56)

    def test_with_no_arguments(self):
        """ test with no args"""
        with self.assertRaises(TypeError):
            rectangle.Rectangle()

    def test_type(self):
        """ test to ensure only int are passed"""
        with self.assertRaises(TypeError):
            rectangle.Rectangle("hair", 2, 0, 0, 10)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, "dog", 3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2.4, 3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, "water", 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle({}, {}, {}, {}, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 4, 4, "animal", 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1.1, 2, 3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, 3.3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, 3, 4.5, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, True, 3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(True, 2, 3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, False, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, 3, True, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2+3j, 3, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, 2+3j, 4, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, 3, 2+3j, 16)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(2+3j, 1, 3, 4, 16)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(0, 2, 3, 4, 16)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(1, 0, 3, 4, 16)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(-3, 2, 3, 4, 16)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(1, -2, 3, 4, 16)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(3, 2, -4, 4, 16)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(3, 2, 4, -6, 16)
