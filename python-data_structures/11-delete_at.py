#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Deletes the element at the specified
    index in the given list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
