#!/usr/bin/env python
# coding: utf-8

# In[57]:


class weather:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range (self.MAX)]
    def gethash(self,key):
        hash = 0
        for char in key:
            hash+=ord(char)
        return hash % self.MAX
        
    def __setitem__(self,datekey, tempval):
        h = self.gethash(datekey)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0]==datekey:
                    self.arr[h][idx] = tempval
                    found = True
                    break
        if not found:
                self.arr[h].append((datekey, tempval))
    def __getitem__(self, datekey):
        h = self.gethash(datekey)
        for element in self.arr[h]:
            if element[0]== datekey:
                tempval = element[1]
                return tempval  
    def __delitem__(self,datekey):
        h = self.gethash(datekey)
        for idx, element in enumerate(self.arr[h]):
            if element[0]== datekey:
                del self.arr[h][idx]
        
        
t = weather()
t["jan 1"] =27
t["jan 2"] = 31
t["jan 3"]=23
t["jan 4"]=34
t["jan 5"]=37
t["jan 6"]=38
t["jan 7"]=29
t["jan 8"]=30
t["jan 9"]=35
t["jan 10"]=30


# In[61]:


t.arr


# In[59]:


t["jan 10"]


# In[60]:


del t["jan 3"]


# In[97]:


import csv
arr= []
with open ('nyc_weather.csv', mode= 'r') as file:
        for line in file:
            values = line.split(',')
            try:
                temp = int(values[1])
                arr.append(temp)
            except:
                print("invalid")


            


# In[99]:


arr


# In[100]:


(sum(arr[0:7]))/len(arr[0:7])


# In[101]:


max(arr[0:11])


# In[102]:


min(arr[0:11])


# In[113]:


import csv
thisdict= {}
with open ('nyc_weather.csv', mode= 'r') as file:
        for line in file:
            values = line.split(',')
            try:
                key = values[0]
                value = int(values[1])
                thisdict.update({key:value})
            except:
                print("invalid")


            


# In[120]:


print(thisdict)


# In[128]:


x= thisdict["Jan 9"]
print("The temperature on Jan 9 is",x)


# In[129]:


y=thisdict["Jan 4"]
print("The temperature on Jan 4 is",y)


# In[228]:


poem =[ ]
with open("poem.txt","r") as file1:
    poem = file1.readlines()
print(poem)


# In[238]:


d1 = dict()
for line1 in poem:
    line1 = line1.strip().lower()
    
    replacements = [(',', ''), ('!', ''),(';', ''),(':',''),('.',''),('i-',''),('\n','')]
    for char, replacement in replacements:
        if char in line1:
            line1 =line1.replace(char, replacement)
    words = line1.split(" ")
    
    for word in words:
        if word in d1:
            d1[word]+=1
        else:
            d1[word]=1
d1


# In[232]:


for key in list(d1.keys()):
        print(key,':',d1[key])


# In[ ]:





# In[ ]:




