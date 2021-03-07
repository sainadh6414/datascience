import pandas as pd
import numpy as np
from pandas.core.computation.ops import _cast_inplace

# Pandas has 2 datatypes, Series(columns) and DataFrame
myList = [5.4, 4.1, 5.2, 65.3]
myarray = np.array(myList)

mySeries1 = pd.Series(data=myList)
print('mySeries1\n', mySeries1)

mySeries2 = pd.Series(data=myarray)
print('mySeries2\n', mySeries2)

print('Access elements mySeries[1]', mySeries1[1])

# Label the rows with index labels

myLabels = ['first', 'second', 'third', 'fourth']
mySeries3 = pd.Series(data=myList, index=myLabels)
print('custom row names or index labels for series\n', mySeries3)

# need not mention the type for pandas
mySeries4 = pd.Series(myList, myLabels)
print('mySeries4\n', mySeries4)

# Access items with label
print('mySeries3[second]', mySeries3['second'])

# Sum uneven series results in NaN
mySeries5 = pd.Series([5.5, 1.1, 8.8, 1.6], ['first', 'third', 'fourth', 'fifth'])
print('mySeries4 + mySeries5\n', mySeries4 + mySeries5)

# Combine series to make a dataframe axis=1 is columns & axis = 0 is rows

df1 = pd.concat([mySeries4, mySeries5], axis=1, sort=False)
print('concatenated data frame with axis=1', df1)

# Create a new dataframe using pd.DataFrame
df2 = pd.DataFrame(np.random.randn(5, 5))
print('Use pd.DataFrame(np.random.randn(5, 5)\n', df2)

# Give labels to row and columns

df3 = pd.DataFrame(np.random.randn(5, 5), index=['first row', 'second row', 'third row', 'fourth row', 'fifth row'], columns=['first col', 'second col', 'third col', 'fourth col', 'fifth col'])
print('custom row and column names for dataframe \n', df3)

# Access individual series or a column
print(' Access individual series or a column df3[[third col, second col]]\n', df3[['third col', 'second col']])
print(' Access individual series or a column df3[first col]\n', df3['first col'])

# Access rows
print('Access fourth row df3.loc[fourth row]\n', df3.loc['fourth row'])
print('Access fourth row using indexes df3.iloc[3]\n', df3.iloc[3])

# Get certain rows and columns
print('Get data frame with specific rows ande columns\n', df3.loc[['fourth row', 'first row'], ['second col', 'third col']])

# Access data frame logically
print('df3>0\n', df3 > 0)
print('df3\n', df3)
print('df3[df3>0]\n', df3[df3 > 0])

# Modify a dataframe
df3['sixth col'] = np.random.randn(5, 1)
print('modified df3 added with sixth col\n', df3)

# Drop a column from data frame
df4 = df3.drop('first col', axis=1)
print('first col dropped\n', df4)

# Drop a row from data frame
df5 = df3.drop('second row', axis=0)
print('second row dropped\n', df5)

# Remove data frame index labels
print('Remove index labels using reset_index()\n', df5.reset_index())

# No need to re initialize use inplace=True
df5.reset_index(inplace=True)
print('No need to re initialize use inplace=True\n', df5)

# Assign new names to the index
df5['new name'] = ['This', 'is', 'the', 'row']
print('new column added\n', df5)
df5.set_index('new name', inplace=True)
print('use set index to re initialize row names\n', df5)

# Combining data frames

df7 = pd.DataFrame({'customer': ['101', '102', '103', '104'],
                    'category': ['cat2', 'cat2', 'cat1', 'cat3'],
                    'important': ['yes', 'no', 'yes', 'yes'],
                    'sales': [123, 52, 214, 663]}, index=[0, 1, 2, 3])
df8 = pd.DataFrame({'customer': ['101', '103', '104', '105'],
                    'color': ['yellow', 'green', 'green', 'blue'],
                    'distance': [12, 9, 44, 21],
                    'sales': [123, 214, 663, 331]}, index=[4, 5, 6, 7])

print('df7\n', df7)
print('df8\n', df8)

# First way to combine data frames
con1 = pd.concat([df7, df8], axis=0, sort=False)
print('concatenated by row\n', con1)

# combine df with sort True
con1 = pd.concat([df7, df8], axis=0, sort=True)
print('concatenated by row with column sort true\n', con1)

# concat using columns
con1 = pd.concat([df7, df8], axis=1, sort=False)
print('concatenated by column\n', con1)

# Merge Dataframes
mf1 = pd.merge(df7, df8, how='outer', on='customer')
print('Outer Merge on "customer"\n ', mf1)

mf1 = pd.merge(df7, df8, how='inner', on='customer')
print('Inner Merge on "customer"\n ', mf1)

mf1 = pd.merge(df7, df8, how='left', on='customer')
print('LeftMerge on "customer"\n ', mf1)

mf1 = pd.merge(df7, df8, how='right', on='customer')
print('Right Merge on "customer"\n ', mf1)

# Join Dataframes
df9 = pd.DataFrame({'Q1': [101, 102, 103],
                    'Q2': [201, 202, 203]},
                    index=['I0', 'I1', 'I3'])

df10 = pd.DataFrame({'Q3': [301, 302, 303],
                    'Q4': [401, 402, 403]},
                    index=['I0', 'I2', 'I3'])

# join behaves just like merge, except instead of using the values of one of the columns to combine data frames, it uses the index labels or rows
print('Outer Join\n', df9.join(df10, how='outer'))
print('Inner Join\n', df9.join(df10, how='inner'))
print('Left Outer Join\n', df9.join(df10, how='left'))
print('Right Outer Join\n', df9.join(df10, how='right'))

# Panda Functions

print('Find unique colors in data frame\n', df8['color'].unique())
print('Find value count colors in data frame\n', df8['color'].value_counts())
print('Find mean of every column\n', df9.mean())
print('Get all columns\n', df8.columns)
new_df = df8[(df8['customer'] != '105') & (df8['color'] != 'green')]
print('df8\n', df8)
print('new_df\n', new_df)
print('mean\n', df8['sales'].mean())
print('min\n', df8['distance'].mean())

# Pass your own function
def profit(s):
    return s* 0.5
print('Pass profit function using"apply"\n', df8['sales'].apply(profit))
print('Use len function in "apply"\n', df8['color'].apply(len))

# Apply map
df11 = df8[['distance', 'sales']]
print('apply map only works on data frames\n', df11.applymap(profit))

def col_sum(co):
    return sum(co)
print('df11.apply(col_sum)\n', df11.apply(col_sum))

# Delete
del df8['color']
print('del df8["color"]\n', df8)

print('df8.index\n', df8.index)

print("df8.sort_values(by='distance')\n", df8.sort_values(by='distance'))

# Group by
mydict = {'customer': ['Customer 1','Customer 1', 'Customer 2', 'Customer 2', 'Customer 3', 'Customer 3'],
          'product1': [1.1, 2.1, 3.8, 4.2, 5.5, 6.9],
          'product2': [8.2, 9.1, 11.1, 5.2, 44.66, 983]}
df6 = pd.DataFrame(mydict, index=['Purchase 1', 'Purchase 2', 'Purchase 3', 'Purchase 4', 'Purchase 5', 'Purchase 6'])

print('Group by ex\n', df6)

grouped_data = df6.groupby('customer')
print('Group by customer\n', grouped_data.describe())
print('Std\n', grouped_data.std())
print('Min\n', grouped_data.mean())

# load the data frame to csv
df8.to_csv('df8.csv', index=True)

# Can mention the index column number in csv
new_df8 = pd.read_csv('df8.csv', index_col=0)
print('new_df8\n', new_df8)

# Save to xlsx
df8.to_excel('df8.xlsx',index=False, sheet_name='first sheet')
excel_df8 = pd.read_excel('df8.xlsx', sheet_name='first sheet', index_col=0)
print('excel_df8\n', excel_df8)












