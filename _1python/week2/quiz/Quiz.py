import pandas as pd
import numpy as np
from pandas.tests.frame.test_sort_values_level_as_str import ascending

demo_array = np.arange(0,10)
print(demo_array)

print(demo_array <3)
print(demo_array[demo_array <6])
print(np.max(demo_array))

demo_matrix = np.array(([13,35,74,48], [23,37,37,38],[73,39,93,39]))
print(demo_matrix)
print(demo_matrix[:, (1,2)])

demo_array = np.arange(10,21)
print(demo_array)
subset_demo_array = demo_array[0:7]

subset_demo_array[:]= 101

print(subset_demo_array)


df = pd.read_excel('GDP_Dataset.xlsx')
print(df)
print(df.Status.value_counts())
print(df.Population.sum())
print(df[['Country', 'Median_Age']].sort_values(by='Median_Age', ascending=False))

print(df[df['Urban_Population'] > 90]['Country'].count())

print(df[['Country','Population_Density']].sort_values(by='Population_Density', ascending=False).head(3))

print(df[df['Country'] == 'India'].GDP.sum())
print(df[df.GDP > df[df['Country'] == 'India'].GDP.sum()])
# 100000000
print(df['GDP_per_Capita'])
print(df['Population'])
print('\n',df['GDP'])
print('\n\n\n', df[(df['Population'] > 100000000) & (df['GDP'] == 250)]['GDP_per_Capita'])

