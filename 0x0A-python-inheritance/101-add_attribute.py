#!/usr/bin/python3
"""Module defining a function to add a new attr to an object if possible"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible.
    Args:
    - obj: Any Python object to which the attribute will be added.
    - attr: A string representing the attribute name.
    - value: The value to assign to the new attribute.
    Raises:
    - TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
