#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Prints the elements of a list in reverse order.
    """
    my_list.reverse()
    
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
