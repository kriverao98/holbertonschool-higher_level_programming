#!/usr/bin/python3


def uppercase(str):
    """Converts a string to uppercase and prints it."""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
