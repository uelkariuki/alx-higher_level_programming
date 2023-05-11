#!/usr/bin/python3

import sys

if __name__ == "__main__":
    a = len(sys.argv[1:])
    if a == 1:
        print('{}'. format(a), "argument:")
    elif a > 1:
        print('{}'. format(a), "arguments:")
    else:
        print('{}'. format(a), "arguments.")

    arg_position = 1
    while (a >= arg_position):
        print('{}:'.format(arg_position), sys.argv[arg_position])
        arg_position = arg_position + 1
