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
        try:
            for attr in attrs:
                if type(attr) in not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dicts = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dicts[key] = value
        return dicts

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        instance with data from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
