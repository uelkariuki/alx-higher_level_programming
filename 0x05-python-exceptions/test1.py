#!/usr/bin/python3 -u
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
l = [-1.0, -0.1, 0.0, 1.0, 30.14, 3.141059, 3.14159265, 3.141592653589791238462643383279502884197169399375105820974944592307816406286]
print(l)
lib.print_python_list(l)
lib.print_python_float(l)
