#!/usr/bin/env python
# coding: utf-8

# In[113]:


from collections import deque 


# In[115]:


class stack:
    def __init__(self):
        self.container = deque()
    def push(self, value):
        self.container.append(value)
    def out(self):
        return self.container.pop()
    def is_empty(self):
        return len(self.container)==0
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def reverse_string(self,val):
        st = stack()
        for ch in val:
            st.push(ch)
        rstr =' '
        while st.size()!=0:
            rstr+= st.out()
        return rstr
            
            
            
        


# In[112]:


s = stack()
s.is_balanced("}}a+b})") 


# In[116]:


s = stack()
s.reverse_string("We will conquere COVID-19")


# In[48]:


s = stack()
s.push(5)
s.push(10)
s.push(20)
s.push(30)
s.push(30)
s.push(40)


# In[37]:


s.out()


# In[38]:


s.is_empty()


# In[39]:


s.peek()


# In[40]:


s.size()


# In[ ]:





# In[ ]:





# In[ ]:




