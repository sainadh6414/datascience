#!/usr/bin/env python
# coding: utf-8

# In[3]:


from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import fcluster
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# In[4]:

df = pd.read_csv('Nutrient-Composition-Dataset.csv')


# In[5]:


df.head()


# In[7]:


# confirm if the data is scaled
df.iloc[:, 1:5].describe()

# Mean, maximum, small values are close to each other, so it's understood that scaling was performed.


# In[8]:


data = df.iloc[:, 1:5]


# In[9]:


data.head()


# # Hierarchical - Agglomerative

# In[12]:


# In[13]:


wardlink = linkage(data, method='ward')


# In[23]:


# dend = dendrogram(wardlink)


# In[16]:


dend = dendrogram(wardlink, truncate_mode='lastp', p=10)


# In[17]:


# Obtain products that belong to each cluster


# In[19]:


# Create cluster lables with fcluster

# Method 1
clusters = fcluster(wardlink, 3, criterion='maxclust')
clusters


# In[20]:


# Method 2
clusters = fcluster(wardlink, 23, criterion='distance')
clusters


# In[21]:


df['clusters'] = clusters
df.head()


# In[22]:


df.to_csv('hc.csv')


# # Non-Hierarchical K-Means Clustering

# In[25]:


df = pd.read_csv('Cust_Spend_Data_New.csv')


# In[27]:


df.head(10)


# In[28]:


df.describe()


# In[29]:

# K-Means Clustering Workout

df = pd.read_csv('Cust_Spend_Data_New.csv')

df.head(10)

df.shape

df.dtypes

# No Null  Values
df.info()

# Description of the data
df.describe()

# Check for duplicates
df.duplicated().sum()

# Drop the non-numeric columns to support Scaling
dropdf = df.drop(['Name', 'Cust_ID'], axis=1)

dropdf.head()

# Scale the data to apply K Means

# Declare standardscaler as an object
x = StandardScaler()

# Fit and Transform
sdf = x.fit_transform(dropdf)

sdf

# K-MEANS

# Understand optimal number of Cluster Count
k_means = KMeans(n_clusters=2)

k_means.fit(sdf)

# Cluster Labels for every row
k_means.labels_

# K Means Inertia (or) WithIn-Sum-Of_Squares (WSS)
k_means.inertia_

# Check the WSS for 3 clusters
k_means = KMeans(n_clusters=3)
k_means.fit(sdf)
# K Means Inertia (or) WithIn-Sum-Of_Squares (WSS)
k_means.inertia_


# Check the WSS for 3 clusters
k_means = KMeans(n_clusters=4)
k_means.fit(sdf)
# K Means Inertia (or) WithIn-Sum-Of_Squares (WSS)
k_means.inertia_

# Check the WSS for 3 clusters
k_means = KMeans(n_clusters=5)
k_means.fit(sdf)
# K Means Inertia (or) WithIn-Sum-Of_Squares (WSS)
k_means.inertia_


# Visualize the above information using WSS Plot

wss = []

def addWSSValues():
    for i in range(1, 10):
        km = KMeans(n_clusters=i)
        km.fit(sdf)
        wss.append(km.inertia_)

addWSSValues()    

print(wss)

# Is there a significant drop? Let's verify in a plot
plt.plot(range(1, 10), wss)

# We have our cluster size to be 3.
# Check the WSS for 3 clusters
k_means = KMeans(n_clusters=3)
k_means.fit(sdf)

# K Means Inertia (or) WithIn-Sum-Of_Squares (WSS)
labels = k_means.labels_

df['KMeans_Cluster'] = labels
print(df.head())

# Compute the Silhouette Score and Silhouette Width
from sklearn.metrics import silhouette_score, silhouette_samples

# Silhouette Score
print('silhouette_score: ', silhouette_score(sdf, labels))

# Find Silhouette Widths
# Silhouete Widths

silwidths = silhouette_samples(sdf, labels)
print('Silhouette Widths', silwidths)

# Attach it to the main df
df['Sil_Width'] = silwidths
print(df.head(5))

print('Minimum Silwidth is: ', silwidths.min())

# All Sil Widths are positive, that means there's no blunder in Cluster Mapping.

# Put the results in to a csv file
df.to_csv('workout result.csv')

# What can we do with the above csv?

# By Grouping clusters, we can identify which cluster spends money in various categories.

# Clustering will let us Profile with the Attributes (Inside the Cluster). For example, 
# Avg of no_of_visits for clusters 1, 2 and 3 will tell you which Cluster are more coming to
# super markets



# %%

# %%
