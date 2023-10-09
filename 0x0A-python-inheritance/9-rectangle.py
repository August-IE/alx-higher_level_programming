#!/usr/bin/python3
"""Defines a Rectangle that inherits from BaseGeometry based
    on 8-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class using BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
