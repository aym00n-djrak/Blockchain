class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def insertAtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
        if self.tailval is None:
            self.tailval = NewNode

    def insertAtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            self.tailval = NewNode
            return
        self.tailval.nextval = NewNode
        self.tailval = NewNode

    def length(self):
        count = 0
        current = self.headval
        while current is not None:
            count += 1
            current = current.nextval
        return count

    def remove(self, key):
        current = self.headval
        if current is not None:
            if current.dataval == key:
                self.headval = current.nextval
                if current == self.tailval:
                    self.tailval = None
                current = None
                return
        while current is not None:
            if current.dataval == key:
                break
            prev = current
            current = current.nextval
        if current is None:
            return
        prev.nextval = current.nextval
        if current == self.tailval:
            self.tailval = prev
        current = None

    def insertBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def bubblesort(self):
        end = None
        while end != self.headval.nextval:
            current = self.headval
            while current.nextval != end:
                if current.dataval > current.nextval.dataval:
                    current.dataval, current.nextval.dataval = current.nextval.dataval, current.dataval
                current = current.nextval
            end = current