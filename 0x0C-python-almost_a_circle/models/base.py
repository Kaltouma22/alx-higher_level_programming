#!/usr/bin/python3
"""Module defining the Base class."""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int): The identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
