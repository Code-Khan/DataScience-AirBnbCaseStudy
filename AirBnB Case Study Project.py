#!/usr/bin/env python
# coding: utf-8

# # AirBnB NY Locations Data Case Study
# 
# In this final project, you task will be to take the data provided and find evidance to answer the following questions.
# 
# 2. How many neighborhood groups are available and which shows up the most?
# 3. Are private rooms the most popular in manhattan?
# 4. Which hosts are the busiest and based on their reviews?
# 5. Which neighorhood group has the highest average price?
# 6. Which neighborhood group has the highest total price?
# 7. Which top 5 hosts have the highest total price?
# 8. Who currently has no (zero) availability with a review count of 100 or more?
# 9. What host has the highest total of prices and where are they located?
# 10. When did Danielle from Queens last receive a review?
# 
# You will be given **4 hours** to complete this assignment. 
# **Be Advised** I will go dark for this intire assignment time period. That said, any questions that you would like to ask about the data, or the project **MUST** be asked before the time starts. Once the time has started, I can no longer give information.
# 
# This is to similate what you will face when you are out in the wild. 
# 
# Happy Coding!

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


air_bnb = pd.read_csv('./AB_NYC_2019.csv')
air_bnb.head()


# In[3]:


air_bnb.info()


# In[4]:


air_bnb.drop(['id', 'latitude', 'longitude', 'calculated_host_listings_count'], axis = 1, inplace = True)
air_bnb.head()


# In[5]:


air_bnb.sort_values(by='price',axis=0, ascending = True, inplace=True, kind='quicksort', na_position='last')
air_bnb


# In[6]:


print(f"{len(air_bnb)} rows are present in the AirBnb File")


# In[40]:


air_bnb.groupby('neighbourhood_group').neighbourhood_group.count().sort_values(ascending=False)


# In[8]:


air_bnb.neighbourhood_group.value_counts().nlargest(1)


# In[9]:


air_bnb.query('neighbourhood_group == "Manhattan"').room_type.value_counts().nlargest(5)


# In[10]:


air_bnb.groupby('room_type')['room_type'].count()


# In[11]:


air_bnb.groupby('host_name').number_of_reviews.sum().nlargest(10)


# In[12]:


air_bnb.groupby('host_name').reviews_per_month.sum().nlargest(10)


# In[13]:


air_bnb.host_name.value_counts()


# In[14]:


neghb_group_highest_avg = air_bnb.groupby('neighbourhood_group').price.mean().nlargest()
neghb_group_highest_avg


# In[15]:


neghb_group_highest_total = air_bnb.groupby('neighbourhood_group').price.max().nlargest()
neghb_group_highest_total


# In[16]:


top5_hosts_high_total_price = air_bnb.groupby('host_name')['price'].sum().nlargest(5)
top5_hosts_high_total_price


# In[17]:


tophost_rev100_0avail = air_bnb.query('number_of_reviews >= 100 and availability_365 == 0')
tophost_rev100_0avail


# In[42]:


host_high_price = air_bnb.groupby(['host_name','neighbourhood']).price.sum().nlargest(1)
host_high_price


# In[19]:


sonder = air_bnb.query('host_name == "Sonder (NYC)"')
sonder


# In[45]:


danielle_last_review = air_bnb.query('host_name == "Danielle" and neighbourhood_group == "Queens"').sort_values('last_review', ascending=False)
danielle_last_review.head(1)


# In[26]:


air_bnb.head()


# ## Further Questions
# 
# 1. Which host has the most listings?

# In[50]:


air_bnb.groupby('host_name').host_id.count().nlargest(10)


# 2. How many listings have completely open availability?

# In[51]:


air_bnb.query('availability_365 == 365').shape


# In[52]:


air_bnb.availability_365.value_counts()


# 3. What room_types have the highest review numbers?

# In[54]:


air_bnb.groupby(['room_type']).number_of_reviews.sum()


# # Final Conclusion
# 
# In this cell, write your final conclusion for each of the questions asked.
# 
# Also, if you uncovered some more details that were not asked above, please discribe them here.
# 
# -- Add your conclusion --

# In[ ]:


Conclusion Questions:
    
# (1)How many neighborhood groups are available and which shows up the most?
According to the data there are five neighborhood groups available, however Manhattan has the most listings with 21,661. 
# (2)Are private rooms the most popular in manhattan? 
'No private rooms' are not the most popular, rather the 'Entire home/ apt' are the most popular. In Manhattan more specifically there are 7,982 private rooms, 13,199 entire home/apt, and 480 shared rooms.
# (3)Which hosts are the busiest and based on their reviews?
With total reivews the busisest host is Michael with 11081 reviews, however with monthly reviews David would take the title with 508.61 /month. 
# (4)Which neighborhood group has the highest average price?
Manhattan would average the highest within the neighborhoods reviewed with an average of $196.88.
# (5)Which neighborhood group has the highest total price?
The highest neighborhood groups are Manhattan, Queens, and Brooklyn with a total of $10,000.
# (6)Which top 5 hosts have the highest total price?
Top Ranked Hosts based on highest total price: 
    Sonder (NYC) with a total of 82,795
    Blueground with a total of 70,331
    Michael with a total of 66,895
    David with a total of 65,844
    Alex with a total of 52,563
# (7)Who currently has no (zero) availability with a review count of 100 or more? 
Based on the data given there are currently 162 listing that hold 100+ reviews with zero availability.
# (8)What host has the highest total of prices and where are they located? 
The host known as Sonder (NYC) located in the Finacial District holds the highest total price with $82,795.
# (9)When did Danielle from Queens last receive a review? 
The last review given to Danielle was on 07/08/2019.

