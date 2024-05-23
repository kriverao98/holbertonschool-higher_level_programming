#!/usr/bin/python3
"""Checks if an obj is an instance of specified class"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class"""
    return type(obj) is a_class
