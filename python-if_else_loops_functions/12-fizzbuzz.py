#!/usr/bin/python3


def fizzbuzz():
    """
    Prints the numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end='')
        elif i % 3 == 0:
            print("Fizz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        else:
            print(i, " ", end='')
