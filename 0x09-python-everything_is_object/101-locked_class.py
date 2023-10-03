#!/usr/bin/python3
"""Defines a class called lockedClass."""


class LockedClass:
    """
    This prevents the user from dynamically creating new LockedClass instance
    attributes except the new instance attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
