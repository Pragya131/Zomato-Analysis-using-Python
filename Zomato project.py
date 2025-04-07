#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis Project

# # Step 1 - Importing Libraries

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Step 2 - Create the data frame

# In[12]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe .head())


# In[13]:


dataframe


# # convert the datatype of column-rate

# In[16]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())



# In[17]:


dataframe.info()


# # Type of Resturants

# In[18]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of resturant")


# # Conclusion - majority of the reasturants falls in dinning category

# In[20]:


dataframe.head()


# In[19]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green',marker = 'o')
plt.xlabel("Type of Resturents", c = "red", size = 20)
plt.ylabel("Votes", c= "red", size = 20)


# # Conclusion- Dinning resturants has received maximum votes

# In[21]:


dataframe.head()


# In[23]:


plt.hist(dataframe['rate'],bins =5)
plt.title("ratings distribution")
plt.show()


# # Conclusion- The majority resturants received ratings from 3.5 to 4

# # Average order spending by couples

# In[24]:


dataframe.head()


# In[25]:


couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # Conclusion - The majority of the couples prefer resturants with an approximate cost of 300 rupees

# # Which mode recieve maximum Rating

# In[29]:


dataframe.head()


# In[27]:


plt.figure(figsize= (6,6))
sns.boxplot(x = 'online_order',y='rate',data = dataframe)


# # Conclusion - offline order recieved lower rating in comparison to online rating

# In[30]:


dataframe.head()


# In[33]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns = "online_order",aggfunc ='size', fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt ='d')
plt.title('Heatmap')
plt.xlabel("Online order")
plt.ylabel("Listed_In (type)")
plt.show()


# # Conclusion- Dining restaurants primarily accept offline orders,whereas cafes primarily receive online orders.This suggests that clients prefer orders in person at restaurants, but prefer online ordering at cafes.

# In[ ]:




