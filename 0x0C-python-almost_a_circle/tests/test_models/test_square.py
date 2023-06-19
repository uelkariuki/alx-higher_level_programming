#!/usr/bin/python3

from io import StringIO  # """importing StringIO from io"""
from models import square  # """importing square from models"""
import sys  # """ importing the sys module"""
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
        self.assertEqual(s1.__str__(), "[Square] (50) 0/0 - 5")
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
        self.assertEqual(s2.__str__(), "[Square] (51) 2/0 - 2")
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
        self.assertEqual(s3.__str__(), "[Square] (52) 1/3 - 3")
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

    def test_square_size_setter(self):
        """ method to test the square size"""
        squ1 = square.Square(5)
        self.assertEqual(squ1.__str__(), "[Square] (49) 0/0 - 5")
        self.assertEqual(squ1.size.__str__(), "5")
        squ1.size = 10
        self.assertEqual(squ1.__str__(), "[Square] (49) 0/0 - 10")
        with self.assertRaises(TypeError):
            squ1.size("9")

    def test_args_and_kwargs(self):
        """ test case for the implementation of args and kwargs"""
        sq_arg_test = square.Square(5)
        self.assertEqual(sq_arg_test.size, 5)
        self.assertEqual(sq_arg_test.x, 0)
        self.assertEqual(sq_arg_test.y, 0)
        self.assertEqual(sq_arg_test.id, 43)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (43) 0/0 - 5")
        sq_arg_test.update(10)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (10) 0/0 - 5")
        sq_arg_test.update(1, 2)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (1) 0/0 - 2")
        sq_arg_test.update(1, 2, 3)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (1) 3/0 - 2")
        sq_arg_test.update(1, 2, 3, 4)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (1) 3/4 - 2")
        sq_arg_test.update(x=12)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (1) 12/4 - 2")
        sq_arg_test.update(size=7, y=1)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (1) 12/1 - 7")
        sq_arg_test.update(size=7, id=89, y=1)
        self.assertEqual(sq_arg_test.__str__(), "[Square] (89) 12/1 - 7")

    def test_dict_representation(self):
        """
        test case to test the implementation of the
        Square instance to dictionary representation (Q14)
        """
        squay1 = square.Square(10, 2, 1)

        self.assertEqual(squay1.size, 10)
        self.assertEqual(squay1.x, 2)
        self.assertEqual(squay1.y, 1)
        self.assertEqual(squay1.id, 44)
        self.assertEqual(squay1.__str__(), "[Square] (44) 2/1 - 10")
        squay_dict = squay1.to_dictionary()
        self.assertEqual(squay_dict.__str__(),
                         "{'id': 44, 'size': 10, 'x': 2, 'y': 1}")
        self.assertEqual(type(squay_dict), dict, "<class 'dict'>")

        squay2 = square.Square(1, 1)
        self.assertEqual(squay2.size, 1)
        self.assertEqual(squay2.x, 1)
        self.assertEqual(squay2.id, 45)
        self.assertEqual(squay2.__str__(), "[Square] (45) 1/0 - 1")

        squay2.update(**squay_dict)
        self.assertEqual(squay2.__str__(), "[Square] (44) 2/1 - 10")
        self.assertEqual(squay1 == squay2.__str__(), False)
