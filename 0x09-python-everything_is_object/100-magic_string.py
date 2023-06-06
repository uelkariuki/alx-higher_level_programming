#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "counter", getattr(magic_string, "counter", 0) + 1)
    return ", ".join(['BestSchool'] * getattr(magic_string, "counter"))
