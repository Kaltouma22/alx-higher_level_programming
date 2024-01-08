#!/usr/bin/python3
"""Module defining a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry-related operations"""
    def area(self):
        """Raises an Exception indicating that area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates the provided value as an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
