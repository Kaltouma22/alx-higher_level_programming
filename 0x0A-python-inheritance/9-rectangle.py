#!/usr/bin/python3
"""Module defining a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """ The constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates and returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a formatted string representation of the rectangle """
        return f"[Rectangle] " + str(self.__width) + "/" + str(self.__height)
