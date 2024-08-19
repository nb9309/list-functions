#!/usr/bin/env python
# coding: utf-8

# In[1]:


[].pop()


# In[5]:


lst = []
lst.append(6)
lst.append('you')
lst.append(3+4j)
lst.append(6.8)
print(lst)


# In[6]:


lst.insert(1,8)
print(lst)


# In[8]:


lst.insert(20,'lol')
print(lst)


# In[9]:


lst.pop()
print(lst)


# In[10]:


lst.pop(1)
print(lst)


# In[11]:


lst.pop(20)
print(lst)


# In[12]:


lst.remove('you')
print(lst)
lst.remove(76)
print(lst)


# In[13]:


del lst[2]
print(lst)
del lst[1:2]
print(lst)
del lst
print(lst)


# In[14]:


a = [3,5,'de',8.4,4+7j]
print(a)


# In[15]:


a.clear()
print(a)


# In[16]:


print(a.clear())


# In[17]:


a = []
a.clear()
print(a)


# In[23]:


s = 'messissippi'
for i,v in enumerate(s):
    if(v == 's'):
        print(i,'----->',v)


# In[24]:


s.index('s')


# In[25]:


s.count('s')
s.count('a')


# In[26]:


s.count('s')


# In[28]:


lst1 = ['hii',8,'how',3+6j,'are',7.8]
lst2 = []
lst2 = lst1.copy()
print(lst2)


# In[29]:


lst3 = ['koo',8]
lst3 = lst1.copy()
print(lst3)


# In[32]:


lst2=lst3
print(lst2)


# In[33]:


lst4 = [7,5,8,4]
lst2 = lst4
print(lst2)


# In[34]:


lst2 = lst4[1:3]
print(lst2)


# In[35]:


print(lst1)
lst1.reverse()


# In[36]:


print(lst1)


# In[ ]:




