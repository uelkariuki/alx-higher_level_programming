#!/usr/bin/python3

"""
A module to handle writing a function that multiplies
2 matrices by using the module NumPy
"""

import numpy as np
"""
importing numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """ A function to multiply 2 matrices using NumPy"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if (m_a == []) or (m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == []) or (m_b == [[]]):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    no_column_a = len(m_a[0])
    if any(len(row) != no_column_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    no_column_b = len(m_b[0])
    if any(len(row) != no_column_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if no_column_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)
    return result
