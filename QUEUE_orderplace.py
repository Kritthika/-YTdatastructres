#!/usr/bin/env python
# coding: utf-8

# In[136]:


from collections import deque
import time
import threading
class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    def orders(self, val):
        for order in val:
            print("Order item placed:",order)
            self.enqueue(order)
            time.sleep(0.5)
            
    def serve(self):
        time.sleep(1.0)
        while True:
            if not self.is_empty():
                time.sleep(2.0)
                print("Order item done:",self.dequeue())
            else:
                break
ordersitem =['pizza','samosa','pasta','biryani','burger']
pq = Queue()
t = time.time()
t1 = threading.Thread(target=pq.orders, args = [ordersitem,])
t2 = threading.Thread(target=pq.serve)
t1.start()

t2.start()
t1.join()
t2.join()
print(time.time()-t)


# In[ ]:




