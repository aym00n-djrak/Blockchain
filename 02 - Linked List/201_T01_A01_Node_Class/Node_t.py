#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for Node.py is correct.
"""
from Node import *

# Instantiate the first node
A = Node('A')

# Instantiate another node
B = Node()
B.setData('B')

print(A)
print(B)

# Get data and the reference to next Node of the node A 
print(A.getData())
print(A.getNext())

# Get data and the reference to next Node of the node B 
A.setNext(B)
tmp = A.getNext()
print(tmp.getData())

print(B.getNext())