import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('startup_funding.csv')
print(df.head())

plt.figure(figsize = (15,6))
sns.countplot(df['InvestmentnType'])
sns.pairplot(df[['Amount in USD','year_funding','month_funding']])

sorted_df = df.groupby('year_funding').sum()['Amount in USD'].sort_values()
print(sorted_df)

plt.figure(figsize=(12,7))
sns.barplot(x=sorted_df.index, y=sorted_df.values)
plt.yscale('log')

sns.pointplot(x = df['month_funding'],y = df['Amount in USD'],hue = df['year_funding'],markers = 'x',estimator=sum,ci = None,legend = 'full',palette = 'rainbow')

sns.pointplot(x = df['month_funding'],y = df['Amount in USD'],hue = df['year_funding'],markers = 'x',estimator=sum,ci = None,legend = 'full',palette = 'rainbow')

df[df['Industry Vertical'] == 'Transportation'].sort_values('Amount in USD',ascending = False)['Startup Name'].head(2)
