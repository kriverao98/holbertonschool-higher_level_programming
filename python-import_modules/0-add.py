#!/usr/bin/python3
"""This script adds two numbers using the function add"""

from add_0 import add

a = 1
b = 2

if __name__ == "__main__":
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
