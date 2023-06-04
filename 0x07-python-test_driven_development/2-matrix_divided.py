#!/usr/bin/python3

"""
1. Divide a matrix
Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
1. matrix must be a list of lists of integers or floats
otherwise raise a TypeError exception with the message
``matrix must be a matrix (list of lists) of integers/floats``
2. Each row of the matrix must be of the same size,
otherwise raise a TypeError exception with the message
``Each row of the matrix must have the same size``
3. div must be a number (integer or float), otherwise raise a
TypeError exception with the message ``div must be a number``
4. div can’t be equal to 0, otherwise raise a
ZeroDivisionError exception with the message ``division by zero``
5. All elements of the matrix should be divided by
div, rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    Arguments:
    -matrix: must be a matrix (list of lists) of integers/floats
    -div: div must be a number

    Returns: a new matrix

    Raises:
    -ZeroDivisionError : if division by zero is done
    -TypeError:
    1.if Each row of the matrix does not have the same size
    2. matrix is not a matrix (list of lists) of integers/floats
    3. if div is not a number (integer or float)
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
        if any(not isinstance(elem, (int, float)) for row in matrix for elem
                in row):
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = []
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for elem in row:
                new_row.append(elem/div)
            result.append(new_row)

    final_result = [[round(elem, 2) for elem in row] for row in result]
    return final_result
