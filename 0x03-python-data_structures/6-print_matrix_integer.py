#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            if len(row) == len(row) -1:
                print("{:d}".format(number), end="")
            elif len(row):
                print("{:d}".format(number), end="")
        print("{}".format(""))
