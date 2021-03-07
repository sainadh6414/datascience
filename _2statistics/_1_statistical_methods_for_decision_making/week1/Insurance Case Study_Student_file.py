#!/usr/bin/env python
# coding: utf-8

# Data source: https://www.kaggle.com/mirichoi0218/insurance/downloads/insurance.zip/1

# # Introduction
# 
# Health insurance in India is a growing segment of India's economy. The Indian health system is one of the largest in the world, with the number of people it concerns: nearly 1.3 billion potential beneficiaries. The health industry in India has rapidly become one of the most important sectors in the country in terms of income and job creation. In 2018, one hundred million Indian households (500 million people) do not benefit from health coverage. In 2011, 3.9%[1] of India's gross domestic product was spent in the health sector.
# 
# According to the World Health Organization (WHO), this is among the lowest of the BRICS (Brazil, Russia, India, China, South Africa) economies. Policies are available that offer both individual and family cover. Out of this 3.9%, health insurance accounts for 5-10% of expenditure, employers account for around 9% while personal expenditure amounts to an astounding 82%.
# 
# In the year 2016, the NSSO released the report “Key Indicators of Social Consumption in India: Health” based on its 71st round of surveys. The survey carried out in the year 2014 found out that, more than 80% of Indians are not covered under any health insurance plan, and only 18% (government funded 12%) of the urban population and 14% (government funded 13%) of the rural population was covered under any form of health insurance.
# 
# India's public health expenditures are lower than those of other middle-income countries. In 2012, they accounted for 4% of GDP, which is half as much as in China with 5.1%. In terms of public health spending per capita, India ranks 184th out of 191 countries in 2012. Patients' remaining costs represent about 58% of the total.[4] The remaining costs borne by the patient represent an increasing share of the household budget, from 5% of this budget in 2000 to over 11% in 2004-2005.[5] On average, the remaining costs of poor households as a result of hospitalization accounted for 140% of their annual income in rural areas and 90% in urban areas.
# 
# This financial burden has been one of the main reasons for the introduction of health insurance covering the hospital costs of the poorest.

# # Data Description:
# 
# The data at hand contains medical costs of people characterized by certain attributes.
# 
# # Domain:
# Healthcare
# 
# # Context:
# Leveraging customer information is paramount for most businesses. In the case of an insurance company, attributes of customers like the ones mentioned below can be crucial in making business decisions. Hence, knowing to explore and
# generate value out of such data can be an invaluable skill to have.
# 
# # Attribute Information:
# 
# - age : age of primary beneficiary
# - sex : insurance contractor gender, female, male
# - bmi : Body mass index, providing an understanding of body,
# - weights that are relatively high or low relative to height,
# - objective index of body weight (kg / m ^ 2) using the ratio of
# - height to weight, ideally 18.5 to 24.9
# - children : Number of children covered by health insurance /
# - Number of dependents
# - smoker : Smoking
# - region : the beneficiary's residential area in the US, northeast,southeast, southwest, northwest.
# - charges : Individual medical costs billed by health insurance.

# ## Import all the necessary libraries

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

sns.set()


# ## Read the data into the notebook

# In[2]:


df = pd.read_csv('insurance.csv')
df.head()


# ## Basic EDA
# * Find the shape of the data,data type of individual columns
# * Check the presence of missing values
# * Descriptive stats of numerical columns
# * Find the distribution of numerical columns and the asssociated skeweness and presence of outliers 
# * Distribution of categorical columns

# In[3]:


df.info()


# In[4]:


df.shape


# # Check for missing value

# In[5]:


df.isnull().sum()


# # Checking the summary of dataframe

# In[6]:


df.describe().T.round() # T transposes the data


# # Plot the Histograms

# In[8]:


df.hist(figsize=(10,10))
plt.show()


# In[12]:


skewness = pd.DataFrame({'skewness': [stats.skew(df.bmi), stats.skew(df.age), stats.skew(df.charges)]},
                       index=['bmi', 'age', 'charges'])
skewness


# # Check Outliers

# In[10]:


plt.figure(figsize=(15,10))
plt.subplot(3,1,1)
sns.boxplot(x=df.bmi,color='lightblue')

plt.subplot(3,1,2)
sns.boxplot(x=df.age,color='lightblue')

plt.subplot(3,1,3)
sns.boxplot(x=df.charges,color='lightblue')

plt.show()


# # Plot Count Plot

# In[14]:


sns.countplot(x=df['sex'])


# In[15]:


sns.countplot(x=df['region'])


# In[17]:


sns.countplot(x=df['smoker'])


# In[18]:


sns.countplot(x=df['children'])


# In[ ]:





# ### Bi-variate distribution of every possible attribute pair

# In[22]:


sns.pairplot(df)
plt.show()


# In[ ]:





# # Check Correlation
# 
# To find out the correlation we will use the corr function and also we will plot a heatmap to visualise this correlation.

# In[24]:


corr = df.corr()
corr


# In[25]:


sns.heatmap(corr, annot=True,cmap='coolwarm')
plt.show()


# ## Do charges of people who smoke differ significantly from the people who don't?

# In[27]:


df.smoker.value_counts()


# In[29]:


plt.figure(figsize=(8,6))
sns.scatterplot(df.age, df.charges, hue=df.smoker, palette=['red', 'green'], alpha=0.6)
plt.show()


# ## Does bmi of males differ significantly from that of females?

# In[31]:


df.sex.value_counts()


# In[33]:


sns.boxplot(x='sex', y='bmi', hue='sex', data=df)
plt.title('BMI across genders')
plt.show()


# In[34]:


df.groupby(['sex'])['bmi'].median()

