#!/usr/bin/env python
# coding: utf-8

# # Python for Data Science Quiz

# ## This quiz is to test your understanding on the concepts learnt in class during the 
# ## Python for Data Science Course. 
# ## Background of the data - The dataset to be used for the quiz pertains to the 
# ## number of hospitalisations under the scheme Ayushman Bharat - Pradhan 
# ## Mantri Jan Arogya Yojana (AB-PMJAY), this data is as on 19 June, 2019.
# ## The data contains number of cases of hospitalisation in public and private hospitalisations 
# ## state/ UT wise and on an all India level.
# ## PMJAY is a scheme which provides health cover of Rs. 5 Lakhs per family per year, for 
# ## secondary and tertiary care hospitalization across public and private empaneled hospitals
# ## in India. State/UT contains the list of states and union territories, Public column contains
# ## hospitalisations in public hospitals and Private column contains list of hospitalisations in 
# ## private hospitals. 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('hospitalisations.csv')


# ## Question 1: Import the dataset.

# In[3]:

df.info()

# ## Question 2: How many rows and columns does the data set have?

# In[ ]:
print(df.isnull().sum())

print(df)

# ## Question 3: Does the data set have missing values? If yes, how many?

# In[ ]:

df.dropna(axis=0, inplace=True)
print(df.isnull().sum())


# ## Question 4: Drop the NA values.

# In[ ]:

df['Total'] = df['Public'] + df['Private']
print(df)



# ## Question 5: Create a new column Total which contains a sum of private and public
# ## hospitalisations. So the column Total should be a summation of the two columns
# ## Public and Private.

# In[ ]:
df.sort_values(by=['Total'], ascending=False).head(3)




# ## Question 6: Which State or UT is the unhealthiest? (i.e. maximum number of hospitalisations) 
# ## HINT : Do not include Grand Total

# In[ ]:

df[df['State/UT'] == 'Chhattisgarh']



# ## Question 7: Chhattisgarh accounts for roughly 18% share in the total hospitalisations in India (assuming these are the only states/UTs in India). True for False?

# In[ ]:
    
df[df['State/UT'] == 'Dadra and Nagar Haveli']





# ## Question 8: In Dadra and Nagar Haveli, which type of hospitals do people prefer?

# In[ ]:

sns.catplot(x='Total', y='State/UT', kind='bar', data=df.sort_values(by='Total', ascending=True), height=5)
hosp_copy = df.iloc[:-1, :]
hosp_copy.head()

finding_healthy = hosp_copy.groupby(['State/UT']).sum()['Total'].sort_values()
print(finding_healthy.index)

plt.figure(figsize=(12,7))
sns.barplot(x=finding_healthy.values, y=finding_healthy.index)
plt.xscale('log')
# ## Question 9: Plot the total hospitalisations in a plot of your choice and comment on the 
# ## healthiest State/UT. (Assuming that the only parameter for Healthiest is the number of 
# ## hospitalisations only)

# In[ ]:

df['Public_Percentage'] = (df['Public']/df['Total']) * 100
print(df)
df_copy = df.iloc[:-1, :]
print(df_copy)
df_copy['Public_Percentage'].mean()

# ## Question 10: Public Hospitalisations are more on an all India level as compared to state/UT level. True or False? 
# ## HINT: Calculate the percentage of public hospitalisation (public/total), then find out the average percentage of all states using the mean() function. Compare this average percentage (state) with the grand total (all India) percentage and comment.

# In[ ]:
df_copy[df_copy.Total > 50000].sort_values(by='Total', ascending=False)['State/UT']




# ## Question 11: Which States/UTs have more than 50000 hospitalisations?

# In[ ]:

df_copy[df_copy.Private == 1]['State/UT']



# ## Question 12: Which state reported exactly 1 case of private hospitalisation?

# In[ ]:


df_copy[df_copy['Public'] == df_copy['Public'].max()]['State/UT']

# ## Question 13: Which State/UT has maximum number of people admitted to public hospitals?

# In[ ]:

df_copy[df_copy['State/UT'] == 'Tripura']['Total']

df_copy[df_copy['State/UT'] == 'Gujarat']['Total']



# ## Question 14: Which state among Tripura and Gujarat witnessed more hospitalisations? 
# ## (in absolute numbers)

# In[ ]:





# ## Question 15: Are there any extreme values/ outliers present in this data set? Do these
# ## values impact the analysis?

# In[ ]:





# THE END!
