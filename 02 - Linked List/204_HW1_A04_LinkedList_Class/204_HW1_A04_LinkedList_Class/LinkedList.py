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

    # TODO 1: Insert at the beginning of the list
    def insertBeg(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return self

    # TODO 2: Insert at the end
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return self

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return self

    # TODO 3: Insert after a specific node
    def insertAfter(self, data, new_data):
        if not self.find(data) + 1:
            return None
        new_node = Node(new_data)
        current = self.head
        while current.data != data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return self

    # TODO 4: Deleting a node at a specific index
    def deleteIndex(self, index):
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    # TODO 5: Search an element
    def find(self, key):
        current = self.head
        index = 0
        if not current:
            return -1

        while current:
            if current.data == key:
                return index
            index += 1
            current = current.next
        return -1

    # TODO 6: Sort the linked list
    def sort(self, head):
        # def sort(self):
        current = head
        if head == None:
            return
        else:
            while current != None:
                next_node = current.next

                while next_node != None:
                    if current.data > next_node.data:
                        temp = current.data
                        current.data = next_node.data
                        next_node.data = temp
                    next_node = next_node.next
                current = current.next

    # TODO 7: Print the linked list
    def printList(self):
        if not self.head:
            print("Nothing is printed")

        current = self.head
        while current:
            print(current.data)
            current = current.next


# ssl = LinkedList()
# # ssl.insertBeg(1)
# # ssl.insertBeg(4)
# # ssl.insertBeg(27)
# # ssl.insertBeg(20)
# # ssl.insertBeg(0)

# ssl.insertEnd(2)
# ssl.insertEnd(34)
# ssl.insertEnd(0)
# ssl.insertEnd(23)
# # ssl.printList()
# ssl.deleteIndex(2)
# # ssl.printList()
# # print(ssl.find(2))
# # print(ssl.find(3))
# # print(ssl.find(0))
# ssl.insertAfter(1, 2)
# ssl.insertAfter(0, 0.5)
# print(ssl.insertAfter(14, 15))
# ssl.sort(ssl.head)
# ssl.printList()
