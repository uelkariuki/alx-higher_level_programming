#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for q, number in enumerate(row):
            if q == len(row) - 1:
                print('{}'.format(number), end="")
            else:
                print('{}'.format(number), end=" ")
        print()
