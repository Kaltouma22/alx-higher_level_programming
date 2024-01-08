#!/usr/bin/python3
"""Module to check inheritance of an object's class."""


def inherits_from(obj, a_class):
    """Checks if the object is true subclass of a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
