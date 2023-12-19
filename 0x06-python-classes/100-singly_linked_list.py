#!/usr/bin/python3
"""This module defines the Square class."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node with type check."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the node with type check."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a singly linked list with head."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    def __str__(self):
        """Represents the entire linked list."""
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
