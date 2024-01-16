#!/usr/bin/python3
"""Module defining the Base class."""
from json import dumps, loads


class base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance."""
        self.id = id if id is not None else self.__class__.__nb_objects + 1
        self.__class__.__nb_objects += 1
