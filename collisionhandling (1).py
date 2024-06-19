#!/usr/bin/env python
# coding: utf-8

# In[316]:


class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    def gethash(self,key):
        has = 0
        for char in key:
            has+=ord(char)
        return has % self.MAX
    def __setitem__(self, key, val):
        h = self.gethash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:  
                self.arr[h][idx]=val
                found = True
                break
        if not found : 
            if len(self.arr[h]) == 0 :
                self.arr[h].append((key,val))
            else:
                i = 1
                while i < (self.MAX):
                    n_h = (h+i)%self.MAX
                    i+=1
                    if len(self.arr[n_h]) == 0 :
                        self.arr[n_h].append((key,val))
                        break
                        
                
                    
                
    def __getitem__(self, key):
        h = self.gethash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    def __delitem__(self,key):
        h = self.gethash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                  del self.arr[h][index]


# In[317]:


t.gethash("march 6")


# In[318]:


t.gethash("march 9")


# In[319]:


t = Hashtable()
t["march 6"]= 120
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459


# In[320]:


t.arr


# In[168]:


del t['march 17']


# In[ ]:





# In[ ]:




