from typing import Any


class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while (printval != None):
            print(printval.dataval)
            printval = printval.nextval

    def insertAtBeginning(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval # type: ignore
        self.headval = NewNode

    def insertAtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode # type: ignore

    def length(self):
        count = 0
        current = self.headval
        while(current):
            count += 1
            current = current.nextval
        return count
    
    def remove(self, key):
        current = self.headval
        if current is not None:
            if current.dataval == key:
                self.headval = current.nextval
                current = None
                return
        while current is not None:
            if current.dataval == key:
                break
            prev = current
            current = current.nextval
        if current == None:
            return
        prev.nextval = current.nextval
        current = None

    def insertBetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval # type: ignore
        middle_node.nextval = NewNode # type: ignore

list1 = LinkedList()

list1.headval = Node("Mon") # type: ignore

e2 = Node("Tue")
e3 = Node("Wed")


list1.headval.nextval = e2 # type: ignore

e2.nextval = e3 # type: ignore

list1.insertAtBeginning("Sun")
list1.insertAtEnd("Thu")


list1.printlist()
print(list1.length())

print("Removing Tue")
list1.remove("Tue")
list1.printlist()

print("Inserting between Mon and Wed")

list1.insertBetween(list1.headval.nextval,"Tue")

list1.printlist()