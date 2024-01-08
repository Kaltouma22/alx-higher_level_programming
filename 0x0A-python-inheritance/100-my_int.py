#!/usr/bin/python3
"""Module defining a rebel MyInt class inheriting from int."""


class MyInt(int):
    """Class inheriting from int with inverted == and != operators."""
    def __eq__(self, other):
        """Inverts the behavior of the equality operator (==)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of the non-equality operator (!=)."""
        return super().__eq__(other)
