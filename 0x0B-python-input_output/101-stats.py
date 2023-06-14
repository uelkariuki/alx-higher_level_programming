#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics
"""
import sys
""" importing the sys module to use std input"""


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

code_count = {code: 0 for code in status_codes}
line_counter = 0
total_size = 0

try:
    for line in sys.stdin:
        try:
            line_counter = line_counter + 1
            data = line.split()
            status_code = int(data[-2])
            file_size = int(data[-1])
            total_size += file_size
            if status_code in code_count:
                code_count[status_code] += 1
            if line_counter % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(code_count.keys()):
                    if code_count[code] > 0:
                        print("{}: {}".format(code, code_count[code]))
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(code_count.keys()):
        if code_count[code] > 0:
            print("{}: {}".format(code, code_count[code]))
