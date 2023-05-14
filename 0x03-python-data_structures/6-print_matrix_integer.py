#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for q in range(len(row)):
            number = row[q]
            if q == len(row) -1:
                print("{:d}".format(number), end="")
            else:
                print("{:d}".format(number), end=" ")
        print("{}".format(""))
