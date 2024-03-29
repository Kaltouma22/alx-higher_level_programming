#!/usr/bin/python3
""" Module that contains the Student class """


class Student:
    """A class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """ Initializes a Student instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
