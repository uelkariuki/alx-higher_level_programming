#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class to test and return the max integer in the list
    """
    def test_values(self):
        """ method to ascertain the max int in a list"""
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([1, 2, 3.4, 4]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1e6, 2, 3]), 1000000)
        self.assertAlmostEqual(max_integer([1, 3, 3, 2]), 3)
        self.assertAlmostEqual(max_integer([-1, -3, -3, -2]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_type(self):
        """ method to ensure only int are being passed """
        self.assertRaises(TypeError, max_integer, [1, 2, "integer"])
        self.assertRaises(TypeError, max_integer, [1, 2, 2+3j])
        self.assertRaises(TypeError, max_integer, [1, 2, "f"])
        self.assertRaises(TypeError, max_integer, [1, 2, (1, 2, 3)])
        self.assertRaises(TypeError, max_integer, [1, 2, ("abc", "jkl")])
        self.assertRaises(TypeError, max_integer, [1, 2, {"cat", "dog", "sh"}])
        self.assertRaises(TypeError, max_integer, [1, 2, b"Computer"])
        self.assertRaises(TypeError, max_integer, [1, 2, None])
        self.assertRaises(TypeError, max_integer, [1, 2, range(6)])
        self.assertRaises(TypeError, max_integer,
                          [1, 2, {"name": "cat", "age": 1}])
        self.assertRaises(TypeError, max_integer, [1, 2, bytearray(5)])
