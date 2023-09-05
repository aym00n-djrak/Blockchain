#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for LinkedList.py is correct.
"""
from LinkedList import *

# Instantiate  a node and set a value 
new_node = Node()
new_node.setData('A')

# Instantiate a linked list
llst1 = LinkedList()
# Insert a node to the list
llst1.append(new_node)
# Traverse through the list and print values
llst1.printAll()
# Print the length of the list
print(llst1.getLen())

# Instantiate aother node and set a value 
new_node = Node('B')
# Insert another node to the list
llst1.append(new_node)
# Traverse through the list and print values
llst1.printAll()
# Print the length of the list
print(llst1.getLen())

# Insert multiple values to the list
for item in ['C', 'D', 'E', 'F']:
    new_node = Node(item, None)
    llst1.append(new_node)    

# Print all values in the list and its length  
llst1.printAll()
print(llst1.getLen())