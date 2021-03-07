# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:39:33 2021

@author: 91966
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('IRIS.csv')

print(df['sepal length'].mean())

print(df['petal length'].std())

df.describe()

plt.scatter(df['sepal length'], df['sepal width'])

df.boxplot(figsize=(15,15))


sns.boxplot(x='petal width', data=df)
plt.show()
sns.boxplot(x='petal length', data=df)
plt.show()
sns.boxplot(x='sepal length', data=df)
plt.show()
sns.boxplot(x='sepal width', data=df)
plt.show()

df.hist(figsize=(15,15))

skewness = pd.DataFrame({'skewness': [stats.skew(df['petal width']), stats.skew(df['petal length']), stats.skew(df['sepal length']), stats.skew(df['sepal width'])]},
                       index=['petal width', 'petal length', 'sepal length', 'sepal width'])
skewness

pd.DataFrame([3,2,4,4,4,5]).mode()

range(12, 11, 10,1000,10010)

