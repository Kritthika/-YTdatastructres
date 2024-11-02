class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head
        result =' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result+= '-->'
            temp_node = temp_node.next
        return result
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        
new_linkedlist = LinkedList()
new_linkedlist.prepend(50)
new_linkedlist.prepend(30)
new_linkedlist.prepend(10)
new_linkedlist.prepend(20)
print(new_linkedlist.length)
print(new_linkedlist)
        