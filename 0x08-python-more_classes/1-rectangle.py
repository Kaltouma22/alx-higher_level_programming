#!/usr/bin/python3
""" This script defines an empty Rectangle class """


class Rectangle:
    """ Class to define a rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize the rectangle with optional width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method to set the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method to retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method to set the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
