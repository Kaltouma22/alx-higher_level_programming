#!/usr/bin/python3
"""This Module for Rectangle class."""


class Rectangle:
    """ Class to define a Rectangle """

    number_of_instances = 0
    """ int: Number of active instance """

    print_symbol = "#"
    """ type: This print symbol, and can be any type """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter method to retrieve the width """
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

    def area(self):
        """ Method to calculate and return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Method to calculate and return the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Str representation of the rectangle with print_symbol char """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """ String representation of the rectangle object """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Destructor method called when an instance of Rectangle is dele """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
