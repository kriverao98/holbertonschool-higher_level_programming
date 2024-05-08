#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints and returns the last digit of a given number.
    """
    if number < 0:
        number = number * -1
    last_digit = number % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
