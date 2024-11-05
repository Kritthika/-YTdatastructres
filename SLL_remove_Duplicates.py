
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
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_duplicates(self):
        if self.head is None:
            return None
        
        prev = None
        curr = self.head
        seen_values = set()
        while curr:
            if curr.value in seen_values:
                prev.next = curr.next
            else:
                seen_values.add(curr.value)
                prev = curr
            curr = curr.next
        return self.head
new_linkedlist = LinkedList()
new_linkedlist.append(50)
new_linkedlist.append(30)
new_linkedlist.append(50)
new_linkedlist.append(20)
new_linkedlist.append(10)


print("Original Linked List:", new_linkedlist)
print("Length of Linked List:", new_linkedlist.length)

new_linkedlist.remove_duplicates()
print("removed_duplicates Linked List:", new_linkedlist)
            