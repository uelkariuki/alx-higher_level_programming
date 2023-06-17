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
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec1.id, 15)

    def test_with_no_arguments(self):
        """ test with no args"""
        with self.assertRaises(TypeError):
            rectangle.Rectangle()
