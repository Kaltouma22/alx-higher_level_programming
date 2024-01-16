#!/usr/bin/python3
"""Module defining the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        self.validate_attr("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        self.validate_attr("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        self.validate_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        self.validate_attr("y", value)
        self.__y = value

    def validate_attr(self, name, value, equal=True):
        """Validate that the value is an integer and set the attribute."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if equal and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not equal and value <= 0:
            raise ValueError(f"{name} must be > 0")
