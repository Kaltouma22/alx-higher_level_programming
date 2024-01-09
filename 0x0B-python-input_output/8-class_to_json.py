#!/usr/bin/python3
""" Module with the "class_to_json" function """


def class_to_json(obj):
    """ return the dictionary representation of the
    serializable attributes of an object """
    return obj.__dict__
