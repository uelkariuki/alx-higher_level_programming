#!/usr/bin/python3

for a in range(122, 96, -1):
    print('{:s}'.format(chr(a)) if a % 2 == 0
          else '{:s}'.format(chr(a - 32)), end="")
