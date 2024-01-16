#!/usr/bin/python3
"""Module defining the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square."""
        return f'[{type(self).__name__}] ({self.id})\
                {self.x}/{self.y} - {self.width}'
