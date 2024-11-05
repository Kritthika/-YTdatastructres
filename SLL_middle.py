
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def find_middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
new_linkedlist = LinkedList()
new_linkedlist.append(10)
new_linkedlist.append(10)
new_linkedlist.append(100)
new_linkedlist.append(10)
new_linkedlist.append(10)

print(new_linkedlist.length)
print(new_linkedlist.find_middle())

