# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:29:31 2021

@author: 91966
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Example 1

# Traffic management inspector in a certain city wants to understand whether carbon emissions from different cars are different. The inspector has reasons to believe that Fuel type (LPG, Petrol or Petrol (E85-Flex Fuel)) and car manufacturer (Audi, BMW, Ford, Volvo) may be the factors responsible for differences in carbon emission. For this purpose, she has taken random samples from all registered cars on the road in that city and would like to compare the amount of carbon emission release due to fuel type and/or manufacturers.
# This problem is essentially a problem of identification of the source(s) of variation in the data. ANOVA will be applied to see whether
#  Carbon emission depends on fuel type only (One-way ANOVA)
#  Carbon emission depends on manufacturer only (One-way ANOVA)
#  Carbon emission depends on both fuel type and manufacturer both (Two-way ANOVA)

# Solution: The objective is to determine whether CO2 emission from cards depend on manufacturer, fuel or both

aovdf = pd.read_csv('./AOVData.csv')

print(aovdf.shape)
print(aovdf.head())

# Factor 1: Fuel Type
# Factor 2: Manufacturer
# Response: CO_Emissions

print(aovdf['co_emissions'].describe())





