class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.value)
class CircularcDLlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node:
            result +=str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:break
            result+='<->'
        return result
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length+=1
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next
            if current_node == self.head: break
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node)
            current_node = current_node.prev
            if current_node == self.tail: break
    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head: break
        return False
    def get(self,index):
        if index < 0 or index > self.length:
            return None
        current_node = None
        if index < self.length // 2:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for i in range (self.length-1, index, -1):
                current_node = current_node.prev
        return current_node
    def set(self, index, target):
        temp = self.get(index)
        if temp:
            temp.value = target
            return True
        return False
    def insert(self, index, target):
        if index <0 or index>self.length:
            print("index out of bound")
        if index == 0:
            self.prepend(target)
            return
        if index == self.length:
            self.append(target)
            return
        new_node = Node(target)
        temp = self.get(index-1)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.length+=1
    def pop_first(self):
        if self.head is None:
            return None
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        self.head = self.head.next
        pop_node.prev = None
        pop_node.next = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.length-=1
        return pop_node
    def pop(self):
        if self.head is None:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        self.tail = self.tail.prev
        pop_node.prev = None
        pop_node.next = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.length-=1
        return pop_node
    def remove(self, index):
        if index <0 or index>self.length:
            return None
        if index == 0 :
            return self.pop_first()
        if index == -1:
            return self.pop()
        pop_node = self.get(index)
        pop_node.prev.next = pop_node.next
        pop_node.next.prev = pop_node.prev
        pop_node.next = None
        pop_node.prev = None
        self.length-=1
        return pop_node
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length=0

cdllist = CircularcDLlist()
cdllist.append(10)
cdllist.append(20)
cdllist.append(30)
cdllist.append(40)
cdllist.prepend(50)
print(cdllist)
print(cdllist.remove(0))
print(cdllist)
