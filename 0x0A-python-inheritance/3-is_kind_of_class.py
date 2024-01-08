#!/usr/bin/python3
"""Module to check object's class instance."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is instance of the specified class or subclass"""
    return isinstance(obj, a_class)
