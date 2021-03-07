#!/usr/bin/env python
# coding: utf-8

# # Virat Kohli : Batting Analysis (2008-2018):
# **Virat Kohli** is an Indian cricketer. He was born in Delhi, India on November 5, 1988. Virat is the first player in ICC cricket history to win all 3 ICC awards in a single year- ICC ODI player of the year, ICC Test player of the year and ICC Player of the year award in 2018.
# 
# <img src="https://images.thequint.com/thequint%2F2018-01%2F5d369107-8477-4216-a39d-ad806e1d3a0c%2FVirat-century.jpg?rect=0%2C0%2C4650%2C2616&auto=format%2Ccompress&fmt=webp&w=700&dpr=1.0.jpg" width="500" height="500" />
# 
# **Born**: November 5, 1988, Delhi, India
# 
# **Team**: India national cricket team
# 
# **Sport**: Cricket
# 
# **Nationality**: India

# **Data Dictionary**
# 1. RunsScored : Number of Runs scored by Kohli in the match.
# 2. BallsFaced : Number of Balls Faces by Kohli in the match.
# 3. BattingPosition : Batting position is Virat Kohli's position on the batting order.
# 4. Dismissal : How Kohli got out in the match or not out. Caught, NO: Not Out, Bowled, Run out, LBW, Stumped, Hit wicket.
# 5. Inning : An innings is one of the divisions of a match during which one team takes its turn to bat. Two 1st inning or 2nd inning.
# 6. Opposition : Name of the Opposition team.
# 7. Year : Year in which the match was played.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 
from warnings import filterwarnings
filterwarnings("ignore")


# In[2]:


# Read Bastman details file
mydata = pd.read_csv('Batsman.csv')


# In[3]:


# View first 5 rows
mydata.head()


# In[4]:


#Checking Info
# mydata.info()
mydata.dtypes


# In[5]:


#Shape of the data
mydata.shape


# In[6]:


#Null Value Check
mydata.isnull().sum()


# In[7]:


# Descriptive summary
mydata.describe()


# In[8]:


# Descriptive summary for Numeric and Categorical variables
mydata.describe(include="all")


# ## Q-1 What is the percentage for Kohli being Not Out.
# **Make a Pie Chart displaying the distribution of Dismissals**

# In[13]:


mydata['Dismissal'].value_counts()


# In[15]:


mydata['Dismissal'].value_counts().index


# In[17]:


plt.figure(figsize=(9,9))
dismissal = mydata['Dismissal']
plt.pie(dismissal.value_counts(), labels=dismissal.value_counts().index,
       autopct='%1.1f%%',
       explode=(0, 0.30, 0, 0, 0, 0, 0),
       radius=1)
plt.show()


# In[ ]:





# ## Q-2 Find the number of times when kohli scored less than or equal to 7 runs?

# In[20]:


plt.figure(figsize=(15,7))
sns.distplot(mydata['RunsScored'], bins=26, kde=True, color='b', hist_kws={'linewidth': 0.5, 'edgecolor': 'white'})
plt.xticks(np.arange(0, 183, 7))
plt.show()


# ## Q.4 Use Boxplot to tell the IQR( Inter Quartile Range) middle 50% of runs scored by Kohli?
# [Hint: Middle 50% Range= Q3(75%)-Q1(25%)]

# In[22]:


sns.boxplot(x='RunsScored', color='violet', data=mydata, showmeans=True)
plt.show()


# In[23]:


mydata['RunsScored'].quantile(.25) # Q1


# In[24]:


mydata['RunsScored'].quantile(.75) # Q2


# In[25]:


81.25-10.75


# In[ ]:





# ## Q. What is the best way that the opposition team bowlers can get Kohli out?
# 
# How Kohli got dismissed most of the times?
# 
# [Hint: Use countplot]

# In[28]:


sns.countplot(mydata['Dismissal'])
plt.show()


# In[ ]:





# ## Q. Against which opposition team Kohli has played the most in his career?
# [Hint: Use Countplot]

# In[32]:


sns.countplot(y=mydata['Opposition'], order = mydata['Opposition'].value_counts().index)
plt.show()


# ## Q. Find out some interesting dismissal patterns in Kohli's career againsts the oppositions.
# [Hint: Stacked Bar Plot]

# In[38]:


ct = pd.crosstab(mydata['Opposition'], mydata['Dismissal'], margins=True)
print(ct)
ct.drop('All', inplace=True)
ct.drop('All', axis=1, inplace=True)
ct.plot.bar(stacked=True, figsize=(20,7))
plt.show()


# ## Q. Which opposition has Kohli scored most runs against? Find the median score against different oppositions and use a boxplot to represent it?
# [Hint: Use barchart & BoxPlot]

# In[39]:


sns.barplot(x='RunsScored', y='Opposition', estimator=np.sum, data=mydata, ci=None)


# In[42]:


plt.figure(figsize=(15,7))
sns.boxplot(x='RunsScored', y='Opposition', data=mydata, showmeans=True)


# In[44]:


mydata[mydata['Opposition'] =='Bangladesh']['RunsScored'].median()


# In[45]:


mydata[mydata['Opposition'] =='New Zealand']['RunsScored'].median()


# In[46]:


mydata[mydata['Opposition'] =='Sri Lanka']['RunsScored'].median()


# ## Q. Compare the runs scored by Kohli in 1st innings vs the 2nd innings.
# [Hint: Use Boxplot]

# In[47]:


sns.boxplot(x='RunsScored', y='Inning', data=mydata, orient='h')


# ## Q. Pre and Post transformation comparison
# 
# **It is well known that Kohli started taking fitness much more seriously post an ordinary IPL in 2012. He changed his training regime and eating habits completely, realising the need to transform his body to survive the rigours of playing all three formats.**
# <img src="https://cdn.wisden.com/wp-content/uploads/2020/07/Untitled-design-47.png" width="500" height="500" />
# <img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSskALcVu6o9iI-7Q_rsehBkQ4PpDN6IAjWwA&usqp=CAU" width="500" height="500" />
# 
# **Kohli says it was the absence of fear or respect for him in the opposition's eye that has forced him to change his work ethic
# Kohli revealed how working on his fitness has lifted his game after coming back from the Australian tour in 2012
# While he considers his idol Tendulkar's skills as a cricketer in a different league, his is a case of pure hard work**

# Adding a column giving true for those rows which represent post transformation 

# In[49]:


mydata['post_transform'] = mydata["Year"]>2012
mydata


# ## Use a Boxplot to compare the runs Scored before and after transformation
# 

# In[51]:


sns.boxplot(x='RunsScored', y='post_transform', data=mydata, orient='h')


# ## Use a Boxplot to compare the Balls Faced before and after transformation

# In[52]:


sns.boxplot(x='BallsFaced', y='post_transform', data=mydata, orient='h')


# ## Use a Boxplot to compare the runs Scored before and after transformation with Hue as innings(innings wise)
# 

# In[54]:


sns.boxplot(x='RunsScored', y='post_transform', hue='Inning', data=mydata, orient='h')


# ## Use a bar plot to compare the dismissal patterns before and after transformation.
# [Hint: Bar Plot]

# In[57]:


pd.crosstab(index=mydata['post_transform'], columns=mydata['Dismissal'], values=mydata['RunsScored'], margins=True, aggfunc='mean')


# In[61]:


ct = pd.crosstab(index=mydata['post_transform'], columns=mydata['Dismissal'], values=mydata['RunsScored'], margins=True, aggfunc='mean')
ct.drop('All',inplace=True)
ct.drop('All',axis=1, inplace=True)
ct.plot.bar(figsize=(10,6))
plt.ylabel('Average Run Scored')
plt.show()


# ## Use Pointplot to Visualize Yearly trend in run scored by Virat Kohli
# [Hint: pointplot]

# In[ ]:





# ## Can we say there is a  linear relationship between RunsScored & BallsFaced over different batting positions?
# [Hint: Use LMplot]

# In[62]:


sns.lmplot(x='RunsScored', y='BallsFaced', hue='BattingPosition', data=mydata, height=7)


# ## How the batting position has changed with different oppositions yearly?
# [Hint: FacetGrid]

# In[64]:


g = sns.FacetGrid(mydata, col='Opposition', col_wrap=3, height=3)
g= g.map(plt.plot, 'Year', 'BattingPosition', marker='*')
plt.show()


#                                              **Happy Learning**
