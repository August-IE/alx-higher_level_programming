#!/usr/bin/python3
"""Defines a Rectangle subclass Square based on 10-square.py."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
