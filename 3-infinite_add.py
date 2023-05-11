#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total_args = 0
    for q in range(1, len(sys.argv)):
        total_args = total_args + int(sys.argv[q])

    print(total_args)
