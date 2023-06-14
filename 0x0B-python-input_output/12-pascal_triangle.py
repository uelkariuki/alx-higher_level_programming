#!/usr/bin/python3

"""
Create a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s
triangle of n:
"""


def pascal_triangle(n):
    """ function to create Pascal's triangle
    n will always be an integer
    """
    if n <= 0:
        return []
    triangle = [[]]

    for a in range(1, n):
        row = [1]
        prev_row = triangle[a - 1]
        for b in range(1, a):
            # ends are always 1
            elem = prev_row[b - 1] + prev_row[b]
            row.append(elem)
        row.append(1)
        triangle.append(row)

    return triangle
