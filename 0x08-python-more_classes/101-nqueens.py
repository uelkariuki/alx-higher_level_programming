#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves
the N queens problem.
"""

import sys
""" importing the sys module"""


def main():
    """ main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)

    if (N < 4):
        print("N must be at least 4\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
