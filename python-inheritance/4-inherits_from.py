#!/usr/bin/python3
"""Check if an obj inherits from a specif class"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class)
