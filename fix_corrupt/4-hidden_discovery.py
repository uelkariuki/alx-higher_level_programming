#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    a = dir(hidden_4)
    for valid_names in a:
        if not valid_names.startswith("__"):
            print(valid_names)
