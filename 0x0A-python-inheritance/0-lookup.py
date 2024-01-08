#!/usr/bin/python3
"""A module to retrive attributes and methods of an object."""


def lookup(obj):
    """Looks up the object attributes and methods.
    Args:
        obj (object): object whose attributes and methods are to be listed.

    Returns:
        A list containing the attributes and methods of the provided object.
    """
    return dir(obj )
