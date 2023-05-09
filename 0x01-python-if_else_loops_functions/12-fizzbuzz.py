#!/usr/bqn/python3

def fizzbuzz():
    for q in range(1, 101):
        if q % 3 == 0 and q % 5 == 0:
            print("FizzBuzz", end=" ")
        elif q % 3 == 0:
            print("Fizz", end=" ")
        elif q % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(q), end=" ")
