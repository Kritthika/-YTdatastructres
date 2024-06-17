#!/usr/bin/env python
# coding: utf-8

# In[132]:


class Node:
    def __init__ (self, data= None, next= None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node   
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def remove_at(self, index):
        if index<0 or index>= self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count =0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1     
            
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
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)       
          
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        count = 0 
        itr = self.head
        for count in range(self.length()):
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node 
                break
            itr = itr.next
            count+=1
    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        index = 0
        itr = self.head
        for index in range(self.length()):
            if itr.data == data:
                self.remove_at(index)
            itr=itr.next
            index+=1      
   
    def print(self):
        if self.head is None:
            print("LIST IS EMPTY")
            return
        itr = self.head
        llstr = ' '
        while itr:
            llstr+=str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
 
    def length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        return count
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    print("length",ll.length())
    ll.remove_by_value("orange")
    ll.insert_after_value("banana","apple")
    ll.print()
    
    


# In[ ]:




