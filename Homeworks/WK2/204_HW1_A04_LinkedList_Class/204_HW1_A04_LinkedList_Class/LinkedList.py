#!/usr/bin/env python3
"""Linked List -> Extended Linked List Implementation: Homework

The goal of this homework is to implement a singly linked list data structure with additional functionalities. 
In previous tutorials you have learned how a node and a linked list data structure in its basic form can be created.
However, a LinkedList class can have more methods to perform additional operations on a linked list,
such as: insertion (begin, end, or after a specific element), deletion, traversal, and sorting.

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this homework located in same folder.

To test run LinkedList_t.py in your command line'

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #TODO 1: Insert at the beginning of the list
    def insertBeg(self, new_data):
        pass
    
    #TODO 2: Insert at the end
    def insertEnd(self, new_data):
        pass

    #TODO 3: Insert after a specific node
    def insertAfter(self, data, new_data):
        pass

    #TODO 4: Deleting a node at a specific index
    def deleteIndex(self, index):
        pass

    #TODO 5: Search an element
    def find(self, key):
        return -1

    #TODO 6: Sort the linked list
    def sort(self, head):
        pass

    #TODO 7: Print the linked list
    def printList(self):
        pass