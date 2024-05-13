#!/usr/bin/python3


def no_c(my_string):
    """
    Removes all occurrences of the letter 'c'
    (both lowercase and uppercase) from a given string.
    """
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
