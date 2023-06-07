#!/usr/bin/python3

"""
Module to handle writing a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ A function that multiplies 2 matrices"""
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

    row_A = len(m_a)
    row_B = len(m_b)
    column_A = len(m_a[0])
    column_B = len(m_b[0])

    # create C that is the matrix result
    result_C = [[0 for q in range(column_B)] for q in range(row_A)]

    for m in range(row_A):
        for n in range(column_B):
            for o in range(column_A):
                result_C[m][n] += m_a[m][o] * m_b[o][n]

    return result_C
