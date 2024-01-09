#!/usr/bin/python3
""" Function to append a string to a text file """


def append_write(filename="", text=""):
    """ Appends the given text to the end of a file with UTF-8"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
