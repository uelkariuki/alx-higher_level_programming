#!/usr/bin/python3

"""
Write a class Node that defines a node of a singly linked list by
"""


class Node:
    """ class Node of a singly linke list """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        property def data(self): to retrieve the Private instance
        attribute that is data
        """
        return self.__data

    """
    property setter def data(self, value): to set the Private instance
    attribute: data
    """
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """
    property def next_node(self): to retrieve Private
    instance attribute: next_node
    """
    @property
    def next_node(self):
        return self.__next_node

    """
    property setter def next_node(self, value): to set
    Private instance attribute: next_node
    """
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList that defines a singly linked list
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Public instance method: def sorted_insert(self, value)
        that inserts a new Node into the correct sorted
        position in the list (increasing order)
        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next_node is not None and \
                    current_node.next_node.data < value:
                current_node = current_node.next_node

            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """
        List should be printable: print the entire list in stdout
        one node number by line
        """
        print_values = []
        current_node = self.head
        while current_node is not None:
            print_values.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(print_values)
