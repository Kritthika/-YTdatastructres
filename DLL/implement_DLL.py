class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
   
class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node:
            result +=str(temp_node.value)
            if temp_node.next is not None:
                result+='<->'
            temp_node = temp_node.next
        return result
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
    def traversal(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
    def reversetraversal(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
    def search(self, target):
        current = self.head
        index =0
        while current:
            if current.value==target:
               return index
            current = current.next
            index+=1
        return -1
    def get(self, index):
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1, index, -1):
                current = current.prev
        return current
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    def insert(self, index,value):
        if index < 0 or index > self.length:
            print("index out of bound")
            return
        node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        if index == -1:
            self.append(value)
            return

        temp_node = self.get(index-1)
        node.next = temp_node.next
        node.prev = temp_node
        temp_node.next.prev = node
        temp_node.next = node
    def pop_first(self):
        if not self.head:
            return None
        pop_node =self.head
        if self.head == 1 :
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev =None
            pop_node.next = None
        self.length-=1
        return pop_node
    def pop(self):
        if not self.head:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            pop_node.prev = None
        self.length-=1
        return pop_node.value
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0 :
           return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        pop_node = self.get(index)
        pop_node.prev.next = pop_node.next
        pop_node.next.prev = pop_node.prev
        pop_node.next = None
        pop_node.prev = None
        self.length-=1
        return pop_node


dllist = DoubleLinkedlist()
dllist.append(10)
dllist.append(20)
dllist.append(30)
dllist.append(40)
dllist.append(50)
dllist.prepend(100)

print(dllist)
print(dllist.remove(3))
print(dllist)
