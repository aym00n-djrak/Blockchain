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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #TODO 2: Insert at the end
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    #TODO 3: Insert after a specific node
    def insertAfter(self, data, new_data):
        new_node = Node(new_data)
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    #TODO 4: Deleting a node at a specific index
    def deleteIndex(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
            return
        current_node = self.head
        for i in range(index - 1):
            if current_node is None:
                return
            current_node = current_node.next
        if current_node is None:
            return
        if current_node.next is not None:
            current_node.next = current_node.next.next

    #TODO 5: Search an element
    def find(self, key):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.data == key:
                return index
            current_node = current_node.next
            index += 1
        return -1


    #TODO 6: Sort the linked list
    def sort(self, head):
        end = None
        while end != self.head.next:
            current = head
            while current.next != end:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            end = current
        
    
    #TODO 7: Print the linked list
    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()