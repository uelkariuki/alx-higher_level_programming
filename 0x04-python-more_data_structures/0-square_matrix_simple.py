#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix.copy()
    return list(map(lambda q: [z * z for z in q], matrix))
