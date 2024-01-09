#!/usr/bin/python3
""" Script to update JSON file with additional arguments """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = list(sys.argv[1:])

try:
    existing_data = load_from_json_file('add_item.json')
except Exception:
    existing_data = []
    
existing_data.extend(arguments)
save_to_json_file(existing_data, 'add_item.json')
