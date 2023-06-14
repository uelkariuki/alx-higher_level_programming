#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics
"""
import sys
""" importing the sys module to use std input"""
import re
""" importing regex module"""


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

stats = {'file size': 0, 'status_codes': {code: 0 for code in status_codes}}

try:
    line_counter = 0
    for line in sys.stdin:
        line_counter = line_counter + 1
        match = re.search(r'"GET /projects/260 HTTP/1.1" (\d{3} (\d+))', line)
        if match:
            status_code = match.group(1)
            file_size = match.group(2)
            stats['file size'] += int(file_size)
            if status_code in status_codes:
                stats['status_codes'][status_code] += 1
        if line_counter % 10 == 0:
            print("File size: {}".format(stats['file size']))
            for code in sorted(stats['status_codes']):
                if stats['status_codes'][code] > 0:
                    print("{}: {}".format(code, (stats['status_codes'][code])))
            print()

except KeyboardInterrupt:
    print("File size: {}".format(stats['file size']))
    for code in sorted(stats['status_codes']):
        if stats['status_codes'][code] > 0:
            print("{}: {}".format(code, (stats['status_codes'][code])))
