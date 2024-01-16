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

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' character."""
        rec_str = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rec_str, end='')

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width,
                       self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attr using keyword args"""
        attr = {'id': id, 'width': width, 'height': height, 'x': x, 'y': y}
        for key, value in attr.items():
            if value is not None:
                 setattr(self, key, value)

    def update(self, *args, **kwargs):
        """Assign args to attr using both positional and keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Return the dictionary representation of this class."""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
