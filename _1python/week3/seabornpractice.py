# -*- coding: utf-8 -*-
"""
1. Numerical Data Plotting
relplot()
scatterplot()
lineplot()

2. Categorical Data Ploting
catplot()
boxplot()
stripplot()
swarmplot()
etc…

3. Visualizing Distribution of the Data
distplot()
kdeplot()
jointplot()
rugplot()

4. Linear Regression and Relationship
regplot()
lmplot()

5. Controlling Plotted Figure Aesthetics
figure styling
axes styling
color palettes

"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set seaborn style
sns.set(style='darkgrid')

tips = sns.load_dataset('tips')
tips.head(10)

sns.relplot(x='total_bill', y='tip', data=tips)
dir(sns.FacetGrid)

sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker')

sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker', style='time')

sns.relplot(x='total_bill', y='tip', hue='size', data=tips)

sns.relplot(x='total_bill', y='tip', hue='size', data=tips, palette='ch:r=-0.8,l=0.95')

sns.relplot(x='total_bill', y='tip', data=tips, size='size')




