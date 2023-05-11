#!/usr/bin/python3

for a in range(10):
    for b in range(a, 10):
        if (a, b) == (8, 9):
            print("{:d}{:d}".format(a, b))
        elif a != b:
            print("{:d}{:d}".format(a, b), end=(", "))
