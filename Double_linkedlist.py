#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    def __init__ (self, data= None, next= None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def print_forward(self):
        if self.head is None:
            print("LIST IS EMPTY")
            return
        itr = self.head
        fllstr = ' '
        while itr:
            fllstr+=str(itr.data) + '-->'
            itr = itr.next
        print(fllstr)
        
    def print_reverse(self):
        if self.head is None:
            print("LIST IS EMPTY")
            return
        last_node = self.get_last()
        itr = last_node
        rllstr = ' '
        while itr:
            rllstr += itr.data + '-->'
            itr = itr.prev    
        print (rllstr)
        
    def get_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
 
    def length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        return count   
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None )
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
        
    def insert_at(self, index, data):
        if index<0 or index>= self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0 
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break
            itr = itr.next
            count+=1
    def remove_at(self, index):
        if index<0 or index>= self.length():
            raise Exception("Invalid Index")
        if index ==0:
            itr = self.head
            self.head = itr.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count+=1
    
if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.remove_at(2)
    ll.print_forward()
    ll.print_reverse()
  
    
    
    
    


# In[ ]:





# In[ ]:




