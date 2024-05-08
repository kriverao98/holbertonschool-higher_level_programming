#!/usr/bin/python3


def islower(c):
    """
    Check if a character is a lowercase letter.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
