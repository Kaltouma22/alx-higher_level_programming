#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with a given size (default is 0)."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size
    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
