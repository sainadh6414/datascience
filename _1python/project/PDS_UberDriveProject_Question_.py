#!/usr/bin/env python
# coding: utf-8

# **Instructions:** 
# 1. **For all questions after 10th, Please only use the data specified in the note given just below the question**
# 2. **You need to add answers in the same file i.e.  PDS_UberDriveProject_Questions.ipynb' and rename that file as 'Name_Date.ipynb'.You can mention the date on which you will be uploading/submitting the file.For e.g. if you plan to submit your assignment on 31-March, you can rename the file as 'STUDENTNAME_31-Mar-2020'**

# # Load the necessary libraries. Import and load the dataset with a name uber_drives .

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


# Get the Data
uberDrives_df = pd.read_csv('uberdrives.csv')
print(uberDrives_df)


# ## Q1. Show the last 10 records of the dataset. (2 point)

# In[8]:


last10Records = uberDrives_df.tail(10)
print(last10Records)


# ## Q2. Show the first 10 records of the dataset. (2 points)

# In[9]:


first10Records = uberDrives_df.head(10)
print(first10Records)


# ## Q3. Show the dimension(number of rows and columns) of the dataset. (2 points)

# In[12]:


uberDrives_df.shape


# ## Q4. Show the size (Total number of elements) of the dataset. (2 points)

# In[14]:


uberDrives_df.size


# ## Q5. Display the information about all the variables of the data set. (2 points)
# 
# #### Hint: Information includes - Total number of columns,variable data-types, number of non-null values in a variable, and usage

# In[15]:


uberDrives_df.info()


# ## Q6. Check for missing values. (2 points) -  Note: Output should be boolean only.

# In[17]:


uberDrives_df.isna()


# ## Q7. How many missing values are present? (2 points)
# 
# #### Hint: Find out the total number of missing values across all the variables

# In[18]:


uberDrives_df.isna().sum()


# ## Q8. Get the summary of the original data. (2 points). 
# 
# #### Hint: Summary includes- Count,Mean, Std, Min, 25%,50%,75% and max
# 
# #### Note:Outcome will contain only numerical column.

# In[19]:


uberDrives_df.describe()


# 
# 
# ## Q9. Drop the missing values and store data in a new dataframe (name it"df") (2-points)
# 
# #### Note: Dataframe "df" will not contain any missing value

# In[22]:


df = uberDrives_df.dropna()
print(df)


# ## Q10. Check the information of the dataframe(df). (2 points)
# #### Hint: Information includes - Total number of columns,variable data-types, number of non-null values in a variable, and usage

# In[23]:


df.info()


# ## Q11. Get the unique start locations. (2 points)
# #### Note: This question is based on the dataframe with no 'NA' values
# #### Hint- You need to print the unique start locations place names in this and not the count.

# In[32]:


uberDrives_df['START*']


# ## Q12. What is the total number of unique start locations? (2 points)
# #### Note: Use the original dataframe without dropping 'NA' values

# In[ ]:





# ## Q13. What is the total number of unique stop locations. (2 points)
# #### Note: Use the original dataframe without dropping 'NA' values.

# In[ ]:





# ## Q14. Display all the Uber trips that has the starting point of San Francisco. (2 points)
# #### Note: Use the original dataframe without dropping the 'NA' values.
# 
# #### Hint: You need to display the rows which has starting point of San Francisco. Try using loc function

# In[ ]:





# ## Q15. What is the most popular starting point for the Uber drivers? (2 points)
# #### Note: Use the original dataframe without dropping the 'NA' values.
# 
# #### Hint:Popular means the place that is visited the most

# In[ ]:





# ## Q16. What is the most popular dropping point for the Uber drivers? (2 points)
# #### Note: Use the original dataframe without dropping the 'NA' values.
# 
# #### Hint: Popular means the place that is visited the most

# In[ ]:





# ## Q17. List the most frequent route taken by Uber drivers. (3 points)
# #### Note: This question is based on the new dataframe with no 'na' values.
# #### Hint-Print the most frequent route taken by Uber drivers (Route= combination of START & END points present in the Data set). One may use Groupby function

# In[ ]:





# ## Q18. Display all types of purposes for the trip in an array. (3 points)
# #### Note: This question is based on the new dataframe with no 'NA' values.

# In[ ]:





# ## Q19. Plot a bar graph of Purpose vs Miles(Distance). (3 points)
# #### Note: Use the original dataframe without dropping the 'NA' values.
# #### Hint:You have to plot total/sum miles per purpose

# In[ ]:





# ## Q20. Display a dataframe of Purpose and the distance travelled for that particular Purpose. (3 points)
# #### Note: Use the original dataframe without dropping "NA" values

# In[ ]:





# ## Q21. Plot number of trips vs Category of trips. (3 points)
# #### Note: Use the original dataframe without dropping the 'NA' values.
# #### Hint : You can make a countplot or barplot.

# In[ ]:





# ## Q22. What is proportion of miles that are covered as Business trips and what is the proportion of miles that are covered as Personal trips? (3 points)
# 
# ### Note:Use the original dataframe without dropping the 'NA' values. The proportion calculation  is with respect to the 'miles' variable.
# 
# #### Hint: Proportion of miles covered as business trips= (Total Miles clocked as Business Trips)/ (Total Miles)
# #### Proportion of miles covered as personal trips= (Total Miles clocked as Personal Trips)/ (Total Miles)
# 

# In[ ]:




