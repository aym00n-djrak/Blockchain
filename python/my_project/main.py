from linked_list import LinkedList, Node

list1 = LinkedList()

list1.headval = Node("Mon")
list1.insertAtBeginning("Sun")
list1.insertAtEnd("Thu")

list1.printlist()

print("Length:", list1.length())
list1.insertAtEnd("Tue")
list1.printlist()
print("Removing Tue")
list1.remove("Tue")
list1.printlist()

list2= LinkedList()

list2.insertAtEnd(5)
list2.insertAtEnd(1)
list2.insertAtEnd(3)

list2.bubblesort()
list2.printlist()