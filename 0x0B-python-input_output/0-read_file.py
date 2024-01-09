#!/usr/bin/python3
""" Function to read and print the contents of a file """


def read_file(filename=""):
    """ Reads the contents of the file with UTF-8 encoding """
    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end="")
