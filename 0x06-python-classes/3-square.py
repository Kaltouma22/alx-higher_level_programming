#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with a given size (default is 0)."""
        self.__size = size
        self.__check_size()

    def __check_size(self):
        """Checks if size is an integer and >= 0."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2
