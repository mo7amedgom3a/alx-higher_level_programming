#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rec = __import__('9-rectangle').Rectangle


class Square(Rec):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
