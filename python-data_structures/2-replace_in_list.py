#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces an element at a given index in a list.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to replace.
        element: The new element to replace the existing one.

    Returns:
        list: The modified list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
