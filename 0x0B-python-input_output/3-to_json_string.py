#!/usr/bin/python3
""" Function to returns the JSON representation of a file """


import json

def to_json_string(my_obj):
    """ Converts a Python object to its JSON representation """
    return json.dumps(my_obj)
