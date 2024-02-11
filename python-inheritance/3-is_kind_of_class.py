#!/usr/bin/python3
"""Check if an object is an instance of a given class or a subclass of it."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or a subclass of it."""
    return isinstance(obj, a_class)
