#!/usr/bin/python3 -u
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b"Holberton School"
lib.print_python_bytes(s)
b = b'New String'
lib.print_python_bytes(b)
