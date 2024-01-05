#!/usr/bin/python3
""" Define a LockedClass that restricts instance attribute creation """


class Lockedclass:
    """
    Lockedclass defines a class that restricts the creation of new
    instance attributes allowing only 'first_name' as a valid attribute
    """

    __kati__ = ["first_name"]
