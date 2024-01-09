#!/usr/bin/python3
""" Define a load_from_json_file function """


import json


def load_from_json_file(filename):
    """ that creates an Object from a JSON file """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
