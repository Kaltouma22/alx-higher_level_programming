#!/usr/bin/python3
""" Module to write a string to a text file """


def write_file(filename="", text=""):
    """ Reads the contents of the file with UTF-8 encoding """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
