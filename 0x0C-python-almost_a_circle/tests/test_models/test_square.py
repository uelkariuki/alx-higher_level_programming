#!/usr/bin/python3

from io import StringIO  # importing StringIO from io
from models import square  # importing square from models"""
import sys  # importing the sys module"""
import unittest
""" importing the unittest module"""

"""
Unit test for the class Square that inherits
from Rectangle: Question 10. And now, the Square!
"""


class TestsSquare(unittest.TestCase):
    """
    class to validate that the class Square is working well
    """
    def test_module_documentation(self):
        """ method to ascertain the module documentation is present"""
        q_module_doc = square.__doc__
        self.assertTrue(len(q_module_doc) > 1,
                        "documentation for module not found")

    def test_class_documentation(self):
        """ method to ascertain the class documentation is present"""
        class_doc = square.Square.__doc__
        self.assertTrue(len(class_doc) > 1,
                        "documentation for class present not found")

    def test_function_documentation(self):
        """ method to ascertain the function documentation is present"""
        func_doc = square.Square.__init__.__doc__
        self.assertTrue(len(func_doc) > 1,
                        "documentation for function present not found")

    def test_values(self):
        """ ascertain the values printed by the Square class
        that inherits from Rectangle
        """

        s1 = square.Square(5)
        self.assertEqual(s1.__str__(), "[Square] (4) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

    def test_square_display(self):
        """ test square display"""
        expected_output = "#####\n#####\n#####\n#####\n#####\n"

        capture_output = StringIO()
        sys.stdout = capture_output

        sq = square.Square(5)
        sq.display()

        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertMultiLineEqual(display_output, expected_output)

    def test_values_1(self):
        """ ascertain the values printed by the Square class
        that inherits from Rectangle
        """
        s2 = square.Square(2, 2)
        self.assertEqual(s2.__str__(), "[Square] (5) 2/0 - 2")
        self.assertEqual(s2.area(), 4)

    def test_display_small_square_with_x_coordinate(self):
        """ display small square with x coordinate using #"""
        expected_output = "  ##\n  ##\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        sq1 = square.Square(2, 2)
        sq1.display()
        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)

    def test_values_2(self):
        """ ascertain the values printed by the Square class
        that inherits from Rectangle
        """
        s3 = square.Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (6) 1/3 - 3")
        self.assertEqual(s3.area(), 9)

    def test_display_small_square_with_both_x_y_coordinate(self):
        """ display small square with x and y coordinate using #"""
        expected_output = "\n\n\n ###\n ###\n ###\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        sq2 = square.Square(3, 1, 3)
        sq2.display()
        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)
