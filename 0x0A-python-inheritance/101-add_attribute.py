#!/usr/bin/python3
"""Defines a function that adds new attributes to an object if possible."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if (
        hasattr(obj, "__dict__") or
        (hasattr(type(obj), "__slots__") and att in type(obj).__slots__)
    ):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
