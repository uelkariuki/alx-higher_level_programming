#!/usr/bin/python3

"""
Write a function that multiplies 2 matrices by using the module NumPy
"""

import numpy as np
"""
importing numpy
"""

def lazy_matrix_mul(m_a, m_b):
    """ a function to multiply 2 matrices using NumPy"""
    result = np.dot(m_a, m_b)
    return result
