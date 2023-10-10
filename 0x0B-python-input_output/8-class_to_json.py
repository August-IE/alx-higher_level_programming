#!/usr/bin/python3
"""A function that converts a class to JSON function."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
