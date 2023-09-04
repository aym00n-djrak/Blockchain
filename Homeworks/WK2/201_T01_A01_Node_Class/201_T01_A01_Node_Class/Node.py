#!/usr/bin/env python3
"""Linked Lists -> Node Implementation: Tutorial 1

The goal of this tutorial is to learn how to create a custom node data structure. 
In its most basic form, each node contains: 
    * data, 
    * and a reference (in other words, a link) to the next node in the sequence
A node class contains setters and getters methods to set and retrieve data of a node. 
Similarly, to set and get a reference of the next node in sequence, 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'Node_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""
class Node:
    # TODO 1: Set the initial values of the current Node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    # TODO 2: Return the value inside a node
    def getData(self):
        return self.data
    
    # TODO 3: change or set the value of the current Node
    def setData(self, data):
        self.data = data
    
    # TODO 4: Get the reference to next node in the list
    def getNext(self):
        return self.next
    
    # TODO 5: Set the reference to the next Node in the list
    def setNext(self, next):
        self.next = next