#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[1]:


get_ipython().run_cell_magic('writefile', 'sample1.csv', 'c1, c2, c3\n1, 1.11, one\n2, 2.22, two\n3, 3.33, three')


# In[3]:


# csv 파일 입력
pd.read_csv('sample1.csv')


# In[5]:


get_ipython().run_cell_magic('writefile', 'sample2.csv', '1, 1.11, one\n2, 2.22, two\n3, 3.33, three')


# In[6]:


pd.read_csv('sample2.csv')


# In[7]:


pd.read_csv('sample2.csv', names=['c1', 'c2', 'c3'])


# In[11]:


df = pd.read_csv('sample1.csv')
df


# In[13]:


df.to_csv('sample3.csv')
get_ipython().system('type sample3.csv')


# In[15]:


df.to_csv('sample4.txt', sep='|')
get_ipython().system('type sample4.txt')


# In[17]:


df.index = ["a","b","c"]
df

