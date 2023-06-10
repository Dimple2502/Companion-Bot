#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd


# In[2]:


os.getcwd()


# In[3]:


os.chdir("D:\\Arya\\sem 5\\campanion bot\\CODES n data set\\companion bot")


# In[5]:


os.getcwd()


# In[32]:


data = pd.read_excel("D:\Arya\sem 5\campanion bot\CODES n data set\RECEPIESdataset.xlsx")
data


# In[33]:


data.isnull().sum()


# In[34]:


data.duplicated()


# In[35]:


data.duplicated().sum()


# In[36]:


data[data['Srno'].duplicated()].head()


# In[37]:


data['Srno'].duplicated().sum()


# In[ ]:




