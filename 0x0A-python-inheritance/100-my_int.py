#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """MyInt has both == and != operators inverted."""

    def compare(self, value):
        """Override == operator with != behavior and vice versa."""
        if self.real == value:
            return False
        else:
            return True
