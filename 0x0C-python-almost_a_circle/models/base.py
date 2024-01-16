#!/usr/bin/python3
"""Module defining the Base class."""
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attri set based on the provided dict."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls == Square:
            dummy_instance = Square(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Function that loads string from file and unjsonfiles"""
        from os import path
        file_js = f"{cls.__name__}.json"
        if not path.isfile(file_js):
            return []
        with open(file_js, "r", encoding="utf-8") as file:
            return [cls.create(**d) for d in cls.from_json_string(file.read())]
