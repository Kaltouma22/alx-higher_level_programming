#!/usr/bin/python3
""" Define a LockedClass that restricts instance attribute creation """


class LockedClass:
    """
    Lockedclass defines a class that restricts the creation of new
    instance attributes allowing only 'first_name' as a valid attribute
    """

    __kati__ = ["first_name"]
