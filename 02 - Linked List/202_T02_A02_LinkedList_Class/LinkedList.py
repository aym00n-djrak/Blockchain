#!/usr/bin/env python3
"""Linked Lists -> Linked List Implementation: Tutorial 2

The goal of this tutorial is to learn how to create a custom singly linked list data structure.
This data structure consists of a collection of nodes which together represent a sequence.  
The LinkedList class should contain methods that can be performed on a linked lists:
Those methods include insertion, deletion and traversal. 
In this tutorial we will implement only a selection of those methods such as:
insertion, length and traversal

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run LinkedList_t.py in your command line'

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        # self.last = None
        # self.length = 0

    def append(self, item):
        # TODO 1: Append an item to the end of the list
        if not self.first:
            self.first = item
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = item

        pass

    def getLen(self):
        # TODO 2: Find the length of the list and return it
        if not self.first:
            return 0
        length = 1
        current = self.first
        while current.next:
            length += 1
            current = current.next
        return length

    def printAll(self):
        # TODO 3: Traverse through all elements in the list from the head to the end and print each value
        if not self.first:
            return 0
        current = self.first
        while current:
            print(current.data)
            current = current.next
        pass
