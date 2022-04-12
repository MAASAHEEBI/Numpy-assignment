#!/usr/bin/env python
# coding: utf-8

# # Numpy Assignment 1

# In[28]:


import numpy as np


# In[38]:


#1. Create a null vector of size 10 but the fifth value which is 1.

arr=np.zeros(10,int)
arr[4]=1
print(arr)


# In[39]:


#2 Create a vector with values ranging from 10 to 49.

arr=np.arange(10,50)
print(arr)


# In[40]:


#3. Create a 3x3 matrix with values ranging from 0 to 8

arr=np.arange(9).reshape(3,3)
print(arr)


# In[41]:


#4. Find indices of non-zero elements from [1,2,0,0,4,0]

arr=np.nonzero([1,2,0,0,4,0])
print(arr)


# In[42]:


#5. Create a 10x10 array with random values and find the minimum and maximum values

arr=np.random.random((10,10))
arrmin,arrmax=arr.min(),arr.max()
arrmin,arrmax


# In[43]:


#6. Create a random vector of size 30 and find the mean value.

arr = np.random.random(30)
m = arr.mean()
print(arr)
print("\nMean is:",m)


# In[ ]:




