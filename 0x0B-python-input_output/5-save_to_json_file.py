#!/usr/bin/python3
""" Function save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """ That write an object to a text file """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
