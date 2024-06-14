#!/usr/bin/env python
# coding: utf-8

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and got a refund of 200$.Make a correction to your monthly expense list based on this

# In[51]:


list = [2200, 2350, 2600, 2130, 2190]
print(list)


# In[52]:


print(list[1]-list[0])


# In[53]:


print(list[0]+list[1]+list[2])


# In[75]:


2000 in list
    


# In[64]:


list.append(1980)
print(list)


# In[83]:


list[3]=list[3]-200
print(list)


# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# In[109]:


heros=['spider man','thor','hulk','iron man','captain america']


# In[110]:


len(heros)


# In[111]:


heros.append("black panther")
print(heros)


# In[112]:


del heros[5]


# In[113]:


heros.insert(2,"black panther")
print(heros)


# In[114]:


heros[1:3] =['doctor strange']
print(heros)


# In[116]:


heros.sort()


# In[117]:


print(heros)


# In[ ]:




