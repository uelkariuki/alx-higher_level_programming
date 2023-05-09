#!/usr/bin/python3

for a in range(122, 96, -1):
    print(chr(a) if a % 2 == 0 else chr(a - 32), end="")
