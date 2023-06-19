#!/usr/bin/python3

from io import StringIO
"""importing StringIO from io"""
from models.rectangle import Rectangle
""" importing rectangle from models"""
import sys
"""importing the sys module"""
import unittest
""" importing the unittest module"""

"""
Write the class Rectangle that inherits from Base: Question 2: First Rectangle
"""


class TestRectangle(unittest.TestCase):
    """
    class to validate that the class Rectangle is working well
    """
    def test_module_documentation(self):
        """ method to ascertain the module documentation is present"""
        q2_module_doc = Rectangle.__doc__
        self.assertTrue(len(q2_module_doc) > 1,
                        "documentation for q2 module not found")

    def test_class_documentation(self):
        """ method to ascertain the class documentation is present"""
        class_doc = Rectangle.__doc__
        self.assertTrue(len(class_doc) > 1,
                        "documentation for q2 class present not found")

    def test_function_documentation(self):
        """ method to ascertain the function documentation is present"""
        func_doc = Rectangle.__init__.__doc__
        self.assertTrue(len(func_doc) > 1,
                        "documentation for q2 function present not found")

    def test_values(self):
        """ ascertain the values printed by Rectangle.id representing
        the number of instances created.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 36)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.id, 37)
        r3 = Rectangle(2, 10, 0)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 10)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.id, 38)
        r4 = Rectangle(2, 10, 0, 0)
        self.assertEqual(r4.width, 2)
        self.assertEqual(r4.height, 10)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 39)
        r5 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
        self.assertEqual(r5.id, 12)
        rec = Rectangle(20, 30)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 40)
        rec1 = Rectangle(20, 30, 2, 7, 15)
        self.assertEqual(rec1.width, 20)
        self.assertEqual(rec1.height, 30)
        self.assertEqual(rec1.x, 2)
        self.assertEqual(rec1.y, 7)
        self.assertEqual(rec1.id, 15)

        area_rec = Rectangle(3, 2)
        self.assertEqual(area_rec.width, 3)
        self.assertEqual(area_rec.height, 2)
        self.assertEqual(area_rec.area(), 6)
        area_rec_1 = Rectangle(2, 10)
        self.assertEqual(area_rec_1.width, 2)
        self.assertEqual(area_rec_1.height, 10)
        self.assertEqual(area_rec_1.area(), 20)
        area_rec_2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(area_rec_2.width, 8)
        self.assertEqual(area_rec_2.height, 7)
        self.assertEqual(area_rec_2.area(), 56)

    def test_with_no_arguments(self):
        """ test with no args"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_type(self):
        """ test to ensure only int are passed"""
        with self.assertRaises(TypeError):
            Rectangle("hair", 2, 0, 0, 10)
        with self.assertRaises(TypeError):
            Rectangle(1, "dog", 3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2.4, 3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "water", 4, 16)
        with self.assertRaises(TypeError):
            Rectangle({}, {}, {}, {}, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 4, 4, "animal", 16)
        with self.assertRaises(TypeError):
            Rectangle(1.1, 2, 3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.5, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, True, 3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(True, 2, 3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, False, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, True, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2+3j, 3, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2+3j, 4, 16)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 2+3j, 16)
        with self.assertRaises(TypeError):
            Rectangle(2+3j, 1, 3, 4, 16)
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, 4, 16)
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 3, 4, 16)
        with self.assertRaises(ValueError):
            Rectangle(-3, 2, 3, 4, 16)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4, 16)
        with self.assertRaises(ValueError):
            Rectangle(3, 2, -4, 4, 16)
        with self.assertRaises(ValueError):
            Rectangle(3, 2, 4, -6, 16)

    def test_display_small_rec(self):
        """ testing how rectangle is displayed using #"""
        expected_output = "##\n##\n"

        capture_output = StringIO()
        sys.stdout = capture_output

        rect = Rectangle(2, 2)
        rect.display()

        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertMultiLineEqual(display_output, expected_output)

    def test_display_large_rec(self):
        """ display large rec using #"""
        expected_output = "####\n####\n####\n####\n####\n####\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        rect = Rectangle(4, 6)
        rect.display()
        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)

    def test__str__override(self):
        """
        Update the class Rectangle by overriding
        the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        str1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str1.width, 4)
        self.assertEqual(str1.height, 6)
        self.assertEqual(str1.x, 2)
        self.assertEqual(str1.y, 1)
        self.assertEqual(str1.id, 12)
        self.assertEqual(str1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        str2 = Rectangle(5, 5, 1)
        self.assertEqual(str2.width, 5)
        self.assertEqual(str2.height, 5)
        self.assertEqual(str2.x, 1)
        self.assertEqual(str2.y, 0)
        self.assertEqual(str2.id, 27)
        self.assertEqual(str2.__str__(), "[Rectangle] (27) 1/0 - 5/5")

    def test_updated_display_small_rec(self):
        """ display small rec using # and x, y coordinate"""
        expected_output = "\n\n ###\n ###\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        rect_updated = Rectangle(3, 2, 1, 2)
        rect_updated.display()
        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)

    def test_updated_display_rec(self):
        """ display rec using # and x, y coordinate"""
        expected_output = "\n\n\n\n   #####\n   #####\n   #####\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        rect_updated = Rectangle(5, 3, 3, 4)
        rect_updated.display()
        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)

    def test_updated_display_rec_1(self):
        """ display rec using # and x, y coordinate"""
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        rect_updated = Rectangle(2, 3, 2, 2)
        rect_updated.display()
        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)

    def test_updated_display_rec_2(self):
        """ display rec using # and x, y coordinate"""
        expected_output = " ###\n ###\n"
        capture_output = StringIO()

        sys.stdout = capture_output
        rect_updated = Rectangle(3, 2, 1, 0)
        rect_updated.display()

        display_output = capture_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual(display_output, expected_output)

    def test_update_args(self):
        """ test the implementation of *args"""

        arg_test = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(arg_test.width, 10)
        self.assertEqual(arg_test.height, 10)
        self.assertEqual(arg_test.x, 10)
        self.assertEqual(arg_test.y, 10)
        self.assertEqual(arg_test.id, 1)
        self.assertEqual(arg_test.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        arg_test.update(89)
        self.assertEqual(arg_test.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        arg_test.update(89, 2)
        self.assertEqual(arg_test.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        arg_test.update(89, 2, 3)
        self.assertEqual(arg_test.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        arg_test.update(89, 2, 3, 4)
        self.assertEqual(arg_test.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        arg_test.update(89, 2, 3, 4, 5)
        self.assertEqual(arg_test.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_and_kwargs(self):
        """ test the implementation of *args and *kwargs"""
        kwarg_test = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(kwarg_test.width, 10)
        self.assertEqual(kwarg_test.height, 10)
        self.assertEqual(kwarg_test.x, 10)
        self.assertEqual(kwarg_test.y, 10)
        self.assertEqual(kwarg_test.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        kwarg_test.update(height=1)
        self.assertEqual(kwarg_test.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        kwarg_test.update(width=1, x=2)
        self.assertEqual(kwarg_test.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        kwarg_test.update(y=1, width=2, x=3, id=89)
        self.assertEqual(kwarg_test.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        kwarg_test.update(x=1, height=2, y=3, width=4)
        self.assertEqual(kwarg_test.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """
        test the impelementation of Rectangle instance to
        dictionary representation
        """
        recty1 = Rectangle(10, 2, 1, 9)

        self.assertEqual(recty1.width, 10)
        self.assertEqual(recty1.height, 2)
        self.assertEqual(recty1.x, 1)
        self.assertEqual(recty1.y, 9)
        self.assertEqual(recty1.id, 30)
        self.assertEqual(recty1.__str__(), "[Rectangle] (30) 1/9 - 10/2")
        recty_dict = recty1.to_dictionary()
        self.assertEqual(recty_dict.__str__(), "{'id': 30,\
 'width': 10, 'height': 2, 'x': 1, 'y': 9}")
        self.assertEqual(type(recty_dict), dict, "<class 'dict'>")

        recty2 = Rectangle(1, 1)
        self.assertEqual(recty2.width, 1)
        self.assertEqual(recty2.height, 1)
        self.assertEqual(recty2.__str__(), "[Rectangle] (31) 0/0 - 1/1")

        recty2.update(**recty_dict)
        self.assertEqual(recty2.__str__(), "[Rectangle] (30) 1/9 - 10/2")
        self.assertEqual(recty1 == recty2.__str__(), False)
