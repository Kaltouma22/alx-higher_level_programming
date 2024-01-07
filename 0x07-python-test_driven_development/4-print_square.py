#!/usr/bin/python3
""" Module that prints a square with the character # """


def print_square(size):
    """
    Prints a square of '#' characters.

    Parameters:
    size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer or if size is a float less than 0.
    ValueError: If size is less than 0.
    """    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
