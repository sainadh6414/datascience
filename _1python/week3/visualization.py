import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

auto = pd.read_csv('Automobile.csv')
print(auto.head())

# Plotting uni variate distrubutions
# distplot will give a bar graph or a distribution histogram
# Kde is a curve that fits the bars kde == Kernel Density Estimate
sns.distplot(auto['highway_mpg'])

# With kde false and ticks true
sns.distplot(auto['city_mpg'], kde=False, rug=True)

# Plotting co variate distrubutions
# jointplot will give out the scatter plot
# param1 is x-axis and param2 is y-axis
sns.jointplot(auto['engine_size'], auto['horsepower'])

# Hex plot
sns.jointplot(auto['engine_size'], auto['horsepower'], kind='hex')

# Kernel Density Estimation in a joint plot
sns.jointplot(auto['engine_size'], auto['horsepower'], kind='kde')


# 2d
sns.pairplot(auto[['normalized_losses', 'engine_size', 'horsepower']])

# Plotting with categorical Data
sns.stripplot(auto['fuel_type'], auto['horsepower'], jitter=True)

# Plot categorical data with a more spaced, spaces a lot
sns.swarmplot(auto['fuel_type'], auto['horsepower'])

# Box Plots -- Very important to know about 
# 3 Quantiles always Q1 Q2 and A3
# +ve whisker = Q3 + 1.5 * IQR
# -ve whisker = Q3 - 1.5 * IQR
# IQR = Q3 - Q1

sns.boxplot(auto['number_of_doors'], auto['horsepower'])
sns.boxplot(auto['number_of_doors'], auto['horsepower'], hue=auto['fuel_type'])

# Bar Plots
# x, y and group_by
sns.barplot(auto['body_style'], auto['horsepower'], hue=auto['fuel_type'])

# Count plot
sns.countplot(auto['body_style'], hue=auto['fuel_type'])

# Point plot
sns.pointplot(auto['body_style'], auto['horsepower'], hue=auto['number_of_doors'])


# Multi panel categorical plots; kinds:- point, bar, count, box, violin, strip
sns.catplot(x='fuel_type', y='horsepower', hue='number_of_doors', col='drive_wheels', data=auto, kind='violin')


# Draw linear regression models
# Linear Model Plot

sns.lmplot(y='horsepower', x='engine_size', data=auto)
sns.lmplot(y='horsepower', x='engine_size', hue='fuel_type', data=auto)
