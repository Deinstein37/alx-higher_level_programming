#!/usr/bin/python3
"""This module creates the linked list"""

<<<<<<< HEAD

class SinglyLinkedList:
    ''' class SinglyLinkedList '''

    def __init__(self):
        self.__head = None

    def __str__(self):
        ''' string representation of Singly Linked List '''
        tmp = self.__head
        while tmp is not None:
            print(type(tmp), end='')
            print(tmp)
            tmp = tmp.next_node

    def sorted_insert(self, value):
        ''' insert new node at proper position
        (sorted) ascending order '''
        self.__head.append(Node(value))

    def insert_at_end(self, value):
        ''' insert at end of SLL '''
        if self.__head is None:
            self.__head = Node(value)
            print("first insert {}".format(self.__head))
        else:
            print("InAtEnd=======")
            tmp = self.__head
            print("----ID{}".format(id(tmp)))
            while(tmp.next_node is not None):
                tmp = tmp.next_node
                print("+++++ID{}".format(id(tmp)))
            print("what is value --> {}".format(str(value)))
            # tmp.next_node = Node(value)
            tmp = Node(value)
            print("jus before end - {}".format(tmp))
            # print("NODEatEND-> {}".format(tmp.next_node))
=======
>>>>>>> 5c1728cf17c4bd3f8e071d9d8ee1aee512f77122

class Node:
    """Node Class represents the node of the linked list"""

    def __init__(self, data, next_node=None):
        """The constructor of the class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """The data setter"""

        if isinstance(value, int) is not True:
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """The next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """The next_node setter"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """The class that represents a singly linked list"""

    def __init__(self):
        """The constructor of the class"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts element into the list sorted"""

        """If list is empty"""
        if self.__head is None:
            self.__head = Node(value)
            return self.__head

        """Append to the end"""
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return self.__head

        temp = self.__head

        """Find a proper place"""
        while (temp.next_node and temp.next_node.data < value):
            temp = temp.next_node

        temp.next_node = Node(value, temp.next_node)

        return temp.next_node

    def __str__(self):
        """Makes the instance printable via print() function"""
        if self.__head is None:
            return ""

        list_string = ""
        temp = self.__head

        while(temp):
            list_string += str(temp.data)

            if (temp.next_node):
                list_string += "\n"

            temp = temp.next_node

        return list_string
