#!/usr/bin/python3
"""Module defining a Rectangle class inheriting from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size):
        """ The constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__size ** 2

    def __str__(self):
        """Returns a formatted string representation of the square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
