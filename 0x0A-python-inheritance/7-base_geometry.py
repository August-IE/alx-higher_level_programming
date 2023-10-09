#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-base_geometry.py."""


class BaseGeometry:
    """An empty class BaseGeometry."""

    def area(self):
        """Required public instance method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a given parameter.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
