#!/usr/bin/python3
"""
Custom list class inheriting from the built-in list class.
"""


class MyList(list):
    """ A custom list class """
    def print_sorted(self):
        """ A methode for print a sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
