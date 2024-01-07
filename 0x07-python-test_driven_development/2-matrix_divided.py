#!/usr/bin/python3
""" Modul for matrix_divided method """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists): Matrix containing integers or floats.
    div (int or float): Divisor used for division.

    Returns:
    list of lists: New matrix with elements divided by the divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
              or if each row of the matrix does not have the same size,
              or if the divisor is not a number (integer or float).
    ZeroDivisionError: If the divisor is equal to zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return divided_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
