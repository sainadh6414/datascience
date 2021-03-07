# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("deep")
df = pd.read_csv('amazon_data.csv')

sns.pairplot(df, diag_kind='kde')


df1 = pd.read_csv('amazon_data1.csv')
sns.distplot(df1['discount percentage'], hist=False)
plt.show()

x=[1,2,3,4,5,6,7,8,9,10]
y=[8,12,16,20,24,28,30,32,36,30]

plt.xticks(rotation=90)
plt.plot(x, y)

irisDf = sns.load_dataset("iris")
sns.countplot(irisDf.species)

irisDf.boxplot(figsize=(12,7))

hospDf = pd.read_csv('Hospitalization//hospitalisations.csv')

hospDf.info()
hospDf.isna().sum()