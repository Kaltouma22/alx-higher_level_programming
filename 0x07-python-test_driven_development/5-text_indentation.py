#!/usr/bin/python3
""" Module for text_indentaion method """


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':' characters.

    Parameters:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    split_chars = ['.', '?', ':']

    line = ""

    for char in text:
        if char in split_chars:
            print(line.strip())
            print()
            print()
            line = ""
        else:
            line += char

    if line:
        print(line.strip())

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
