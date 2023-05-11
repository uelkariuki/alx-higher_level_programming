#!/usr/bin/python3

def print_last_digit(number):
    last_digit_unsgnd = abs(number) % 10
    print(last_digit_unsgnd, end="")
    return last_digit_unsgnd
