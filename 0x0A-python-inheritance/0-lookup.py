#!/usr/bin/python3
"""A module to retrive attributes and methods of an object."""


def lookup(obj):
    """
    Returns a list containing the attributes and methods of the given object.

    Args:
    - obj: Any Python object whose attributes and methods are to be listed.

    Returns:
    - A list containing the attributes and methods of the provided object.
    """
    return dir(obj )
