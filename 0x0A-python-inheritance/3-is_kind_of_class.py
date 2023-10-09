#!/usr/bin/python3
"""Defines similar classes."""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of the class inherited from.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
