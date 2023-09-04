class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def function_x(head):
    while head:
        print(head.val)
        head = head.next

head = Node(12)
a = Node(99)
b = Node(37)
head.next = a
a.next = b

function_x(head)