#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def last_digit(number):
    last_digit_unsigned = abs(number) % 10
    return -last_digit_unsigned if (number < 0) else last_digit_unsigned
the_digit = last_digit(number)
if the_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, the_digit))
elif the_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, the_digit))
elif the_digit < 6 and the_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, the_digit))
