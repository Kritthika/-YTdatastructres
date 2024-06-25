#!/usr/bin/env python
# coding: utf-8

# In[66]:


from collections import deque
class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return self.buffer[-1]
    
    def binary(self, val):
        e = Queue()
        e.enqueue("1")
        for i in range(val):
            bina = e.front()
            print(bina)
            e.enqueue(bina+ "0" )
            e.enqueue(bina + "1")
            e.dequeue()


# In[67]:


q = Queue()
q.binary(10)


# In[ ]:




