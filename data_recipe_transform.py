#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


# !pip install mlxtend
from mlxtend.preprocessing import TransactionEncoder


# In[4]:


# !pip install ExcelWriter
import openpyxl
import xlsxwriter
#import pandas.ExcelWriter as ExcelWriter


# In[5]:


data = pd.read_excel("D:\Arya\sem 5\campanion bot\CODES n data set\mini_dataset.xlsx")
data


# In[6]:


df = pd.DataFrame(data)
df


# In[7]:


df_Ingredients = df['TranslatedIngredients'].values
df_Ingredients[0]


# In[ ]:


df_ing_list = []
for i in range (0, len(df_Ingredients)):
    df_ing_list.append(df_Ingredients[i].split(','))
    
df_ing_list[0:2]


# In[9]:


df2 = df.copy(deep=True)
df2.head(3)


# In[10]:


recipe_name = df['TranslatedRecipeName']
recipe_name


# In[11]:


recipe_id = df['Srno']
recipe_id


# In[ ]:





# In[12]:


df_ing = pd.DataFrame(data=df_ing_list)
df_ing.insert(0, 'TranslatedRecipeName', recipe_name)
df_ing.insert(0, 'Recipe_id', recipe_id)
df_ing.head(3)


# In[13]:


df_steps = df['TranslatedInstructions'].values
df_steps[0]


# In[14]:


steps = []
for i in range (0, len(df_steps)):
    steps.append(df_steps[i].split('.'))
    
steps[0:2]


# In[15]:


df_recipe_steps = pd.DataFrame(data = steps)
df_recipe_steps.insert(0, 'Recipe_id', recipe_id)
df_recipe_steps.insert(1, 'Recipe_name', recipe_name)
df_recipe_steps.head(3)


# In[16]:


df_bot = [df, df_ing, df_recipe_steps]
df_bot


# In[19]:


Excelwriter = pd.ExcelWriter("D:\Arya\sem 5\campanion bot\CODES n data set\sorted_Recipes.xlsx", engine="xlsxwriter")

for i, df0 in enumerate (df_bot):
    df0.to_excel(Excelwriter, sheet_name="Sheet"+str(i+1))
    
Excelwriter.save()


# In[ ]:




