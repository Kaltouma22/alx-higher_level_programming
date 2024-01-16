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

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Internal method that updates instance attr using keyword args"""
        attr = {'id': id, 'size': size, 'x': x, 'y': y}
        for key, value in attr.items():
            if value is not None:
                 setattr(self, key, value)

    def update(self, *args, **kwargs):
        """Assign args to attr using both positional and keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
