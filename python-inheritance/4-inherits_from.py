#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
