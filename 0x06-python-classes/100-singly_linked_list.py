#!/usr/bin/python3
"""
Simple class for Node

Attributes:
    data (int): data of node
    next_node: next node
"""


class Node:
    """ A simple class Node"""

    def __init__(self, data, next_node=None):
        """
        Initializes a node

        Parameters:
            data (int): the data
            next_node (Node): the following node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if not isinstance(next_node, Node) or next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """ To get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        To set data value

        Parameters:
            value (int): the new value

        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ To get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        To set next_node

        Parameters:
            value (Node): the new value

        """
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""
Class to implement linked list.

Attributes:
    __head (list): a list of nodes
"""


class SinglyLinkedList:
    """Implementation of linked list in Python"""

    def __init__(self):
        """The head of the list"""
        self.__head = list()

    def __str__(self):
        """Printing the list

        Returns:
            str: a string
        """
        s = ""
        while nod in self.__head:
            s = s + node.data
            s += "\n"
        return s

    def sorted_insert(self, value):
        """
        Adding nodes to the list

        Parameters:
            value (int): the value of the new node
        """
        try:
            new = Node(value)
            self.__head.append(new)
            self.__head.sort(key=lambda x: x.data)
        except TypeError as te:
            print(te)
