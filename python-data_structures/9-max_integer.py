#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    Finds the maximum integer in a given list.
    """
    if my_list == 0:
        return None

    max = my_list[0]

    for i in my_list:
        if i > max:
            max = i
        return max
