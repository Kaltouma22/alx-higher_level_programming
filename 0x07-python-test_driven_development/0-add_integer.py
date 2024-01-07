#!/usr/bin/python3
""" Modul for add_integer method"""


def add_integer(a, b=98):
    """ Function to add two integers or floats

    Parameters:
    a: The first number.
    b: The second number. Defaults to 98.

    Raises:
    TypeError: If a or b is not an integer or float.

    Returns:
    int: The addition of a and b as an integer.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
