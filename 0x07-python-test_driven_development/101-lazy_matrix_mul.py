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
    if (m_a == []):
        raise ValueError("shapes (0,) and (2,2) not aligned: 0\
 (dim 0) != 2 (dim 0)")
    if (m_a == [[]]):
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0\
 (dim 1) != 2 (dim 0)")
    if (m_b == []):
        raise ValueError("shapes (2,2) and (0,) not aligned: 2\
 (dim 1) != 0 (dim 0)")
    if (m_b == [[]]):
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2\
 (dim 1) != 1 (dim 0)")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("invalid data type for einsum")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("invalid data type for einsum")

    no_column_a = len(m_a[0])
    if any(len(row) != no_column_a for row in m_a):
        raise ValueError("setting an array element with a sequence.")

    no_column_b = len(m_b[0])
    if any(len(row) != no_column_b for row in m_b):
        raise ValueError("setting an array element with a sequence.")

    # if no_column_a != len(m_b):
        # raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)
    return result
