#!/usr/bin/python3
"""Defines similar classes."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that's inherited.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
