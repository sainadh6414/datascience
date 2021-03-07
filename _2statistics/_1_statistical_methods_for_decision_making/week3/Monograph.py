# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:27:23 2021

@author: 91966
"""

import random
import math
import numpy as np
import statistics as stat
from numpy.random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats

# Q1

random.seed(573)

population1 = np.random.normal(5.5, 2.4, 10000)
print('Population parameters')
print(stat.mean(population1))
print(stat.stdev(population1))

# Generate 500 samples each of size 1000

sample_list = [sum(random.sample(list(population1), 1000))/1000 for _ in range(500)]
print('Sample1 parameters')
print(stat.mean(sample_list))
print(stat.stdev(sample_list))

sample_list2 = [sum(random.sample(list(population1), 1000))/1000 for _ in range(500)]
print('Sample2 parameters')
print(stat.mean(sample_list2))
print(stat.stdev(sample_list2))

fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(12,5))

plt.rcParams.update({'font.size': 14})

ax1.hist(population1, 15, color='blue', rwidth=0.85)
ax1.set_xlabel('Distribution of N(5.5, 2.4) Population')
ax1.set_ylabel('Frequency')

ax2.hist(sample_list, 15, color='red', rwidth=0.85)
ax2.set_xlabel('Distribution of First Sample average from N(5.5,2.4) population')

ax3.hist(sample_list, 15, color='green', rwidth=0.85)
ax3.set_xlabel('Distribution of Second Sample average from N(5.5,2.4) population')

plt.tight_layout()
ax1.grid(axis='y', alpha=0.75)
ax2.grid(axis='y', alpha=0.75)
ax3.grid(axis='y', alpha=0.75)

plt.show()

# Q2
# Generate data from a Chi-Square distribution

random.seed(573)
population2 = np.random.chisquare(3, 10000)
print('Chi Square Parameters')
print(stat.mean(population2))
print(stat.stdev(population2))

# Generate 500 samples of each size 1000 from population2

sample1 = [sum(random.sample(list(population2), 1000))/1000 for _ in range(500)]
print('Sample1 Parameters')
print(stat.mean(sample1))
print(stat.stdev(sample1))

sample2 = [sum(random.sample(list(population2), 1000))/1000 for _ in range(500)]
print('Sample2 Parameters')
print(stat.mean(sample2))
print(stat.stdev(sample2))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,5))
plt.rcParams.update({'font.size': 14})

ax1.hist(population2, 15, color='blue', rwidth=0.85)
ax1.set_xlabel('ChiSQ Distribution of N(5.5, 2.4) Population')
ax1.set_ylabel('Frequency')

ax2.hist(sample1, 15, color='red', rwidth=0.85)
ax2.set_xlabel('Distribution of First Sample average from N(5.5,2.4) population')

ax3.hist(sample_list, 15, color='green', rwidth=0.85)
ax3.set_xlabel('Distribution of Second Sample average from N(5.5,2.4) population')

plt.tight_layout()
ax1.grid(axis='y', alpha=0.75)
ax2.grid(axis='y', alpha=0.75)
ax3.grid(axis='y', alpha=0.75)

# CENTRAL LIMIT THEOREM

# Q1

# The baggage limit for an airline is set at 50 kg per person. The weight of the baggage
# of an individual passenger follows a normal distribution with a mean of 45 kg and a
# standard deviation of 17 kgs. What is the probability that a randomly chosen
# passenger’s baggage will be over the limit?

# Probabliity of the baggage greater than 50Kgs
# Create a normal distrubution for 50kgs avg NORM.DIST(50, 45, 17, 1)
# P[X] ~ N(45,17)
# To get greater than P[X > 50Kgs] => 1 - NORM.DIST(50, 45, 17, 1)

p = stats.norm(45,17).cdf(50)
1-p


# Q2

# When in a hurry, the airline does not weigh each passenger’s baggage, but check
# whether average baggage weight of 100 passengers is within the limit. What is the
# probability that average baggage weight of 100 passengers will be over the limit?

p = stats.norm(45,1.7).cdf(50)
1-p


# Confidence Interval

# Q1

# The caffeine content (in mg) was examined for a random sample of 50 cups of black coffee
# dispensed by a new machine. The mean of the sample is found to be 110 mg. It is known that
# the standard deviation from all the machines of that manufacturer is 7 mg. Construct a 95%
# confidence interval for μ, the mean caffeine content for cups dispensed by the machine.

n = 50
xbar = 110
sigma = 7
# 95% confidence interval for normal mean mu

# xbar +/- 1.96 * sigma/sqrt(n)

# [109.01, 110.99]



# i) Refer to Experiment I. Take the set of 500 independent random samples, which has
# already been created. Recall that each sample is of size n = 1000 and is generated from
# a normal population with given parameters (μ = 5.5, σ = 2.4).
# ii) Convert this into a problem of construction of confidence interval for a normal mean.
# Assume μ is unknown, but σ = 2.4 is known.
# iii) Compute sample average from each sample.
# iv) Apply the formula x̅ ±1.96
# σ
# √n
# , where x̅ is computed from each of the 500 samples of
# size 1000.
# v) Count how many of these intervals actually contain μ = 5.5, and divide it by 500 to get
# the proportion of intervals that contains the population mean.

sampleVector = [sum(random.sample(list(population1), 1000))/10001 for _ in range(500)]
print('mean', stat.mean(sampleVector))
print('stdev', stat.stdev(sampleVector))

conflimit = np.zeros((500, 2))
counter = 0

for i in range(0, conflimit.shape[0]):
    conflimit[:,0] = sample_list[i] - 1.96 * 2.4/math.sqrt(1000)
    conflimit[:,1] = sample_list[i] + 1.96 * 2.4/math.sqrt(1000)
    
    if((conflimit[:,0] < 5.5).any() & (conflimit[:,1]>5.5).any()):
        counter = counter + 1
        
counter
countcoeff = counter/500
countcoeff   


# STUDENT's T Distribution

# The caffeine content (in mg) was examined for a random sample of 50 cups of black coffee
# dispensed by a new machine. The mean of the sample is found to be 110 mg and the sample
# standard deviation is estimated to be 7 mg. Construct a 95% confidence interval for μ, the mean
# caffeine content for cups dispensed by the machine.
 
sampleMean_xBar = 110
sampleSize_n = 50
sample_stdev = 7
degOfFreedom = 50 - 1

# t(n-1) = xBar - mU / sigma/sqrt(n) 
# mU = xBar +/- sigma/sqrt(n)

# construct 95% confidence interval, i.e 0.025 Alpha on either side
# i.e for 1 - Aplha 0.975, the t statistic would be

from scipy.stats import t

pp_f = t.ppf([0.975], degOfFreedom)
pp_f[0]

# 95% CI of population mean mu is xBar +/- ppf[0] * s/sqrt(n)

print("[",sampleMean_xBar - pp_f[0] * sample_stdev/math.sqrt(sampleSize_n),",",
sampleMean_xBar + pp_f[0] * sample_stdev/math.sqrt(sampleSize_n), "]")



# Examples

# Example 1. A certain food aggregator ZYX is facing stiff competition from its main rival SWG
# during Corona period. To retain business, ZYX is advertising that, within a radius of 5 km from
# the restaurant where the order is placed, it can deliver in 40 minutes or less on the average. The
# delivery times in minutes of 30 deliveries are given in the file fastfood.csv. Assuming the
# delivery distribution is approximately normal, is there enough evidence that ZYX’s claim is
# true?

# It is clearly a one-sided hypothesis testing problem, concerning population mean μ, the average
# delivery time.


# Null Hypothesis
# (mU0 <= 40 and mUA > 40) and  Level of significance α = 0.05

from scipy import stats
from scipy.stats import ttest_1samp

fastFoodDf = pd.read_csv('./MonographDatasets/FastFood.csv')
mean = fastFoodDf.Time.mean()

print('The Mean delivery time is {}'.format(round(mean, 3)))

t_statistics, p_value = stats.ttest_1samp(fastFoodDf['Time'], popmean=40)

print('t statistic = {} and pValue = {}'.format(round(t_statistics, 3), round(p_value/2, 7)))

alpha = 0.05

if(p_value/2 < alpha) :
    print("We reject Null hyp, Wait minutes is higher than {}".format(40))
else:
    print('We fail to reject null hyp')
    
    
    
# Example 2. Do you feel frustrated when your favourite TV program is interrupted by
# commercials? Faced by criticisms in consumers’ forums, major channels published a report
# that as per their policy, maximum duration of commercials is 7 minutes per 30-minute slot.
# That means in that slot, actual programming minutes is 23 or more. Consumers’ Forum took
# an independent sample of 20 30-minute programs and measured the number of programming
# minutes in each of them. The data is given in program.csv. Assuming that the population
# distribution is normal, is there enough evidence that the channels’ official policy is being
# followed?

# It is clearly a one-sided hypothesis testing problem, concerning population mean μ, the average
# programming minute in a 30-minute slot on TV.

# H0 is Actual programming minutes 23 or more
# H0: mU >= 23 against HA: mU < 23

tvDf = pd.read_csv('./MonographDatasets/Program.csv')

mean = tvDf.mean()

print('The mean Program Minutes is {}'.format(round(mean, 3)))

t_statistics, p_value_2sided = stats.ttest_1samp(tvDf['Minutes'], popmean = 23)

p_value_1sided = p_value_2sided/2

print('t_statistic={} and pValue = {}'.format(round(t_statistics, 3), round(p_value_1sided, 3)))

alpha = 0.05

if(p_value_1sided >= alpha):
    print('We fail to reject null hypothesis')
else:
    print('Reject null hypothesis as the p_value {} is less than alpha 0.05'.format(round(p_value_1sided, 3)))

# Example 3(a). The cost of a certain high-quality diamond is $5600 per carat in mid-west USA.
# A jeweller contacted New York City jewellers to understand whether mean price there differs
# significantly from mid-west. He contacted 25 jewellers and the price per carat for the same
# type of diamond is given in diamonds.csv. Is there any reason to believe that price of diamond
# is different in two places?

# This is a two-sided alternative since the jeweller wants to check whether prices differ in two
# places.

# The null hypothesis is H0: mU = 5600 against H1: mU != 5600

# Level of significance alpha = 0.05

mU0 = 5600
alpha = 0.05
sampleSize = 25

diamondDf = pd.read_csv('./MonographDatasets/Diamonds.csv')
xBar = diamondDf['Price'].mean()

print('xBar for diamons of 25 jewellers is {}'.format(round(xBar,3)))

t_statistic, p_value_2sided = stats.ttest_1samp(diamondDf['Price'], popmean=5600)

print('t_statistic {} and pValue_2sided {}'.format(round(t_statistic, 3), round(p_value_2sided, 3)))

if(p_value_2sided < alpha):
    print('Null Hypothesis is rejected, True mean not equal to 5600')
else:
    print('We fail to reject null hypothesis')
    
# Example 3(b). Construct a 95% confidence interval for average price of diamonds in NYC.
# Based on this confidence interval, can you conclude whether H0: μ = 5600 may be rejected in
# favour of HA: μ ≠ 5600.    

def mean_confidence_interval(data, confidence):
    a = 1.0 * np.array(data)
    n = len(a)
    m = np.mean(a)
    se = stats.sem(a)
    h = se * stats.t.ppf((1+confidence)/2, n-1) # 0.975 is alpha for t-test-statistic
    return print('The lower and upper confidence interval values are [{}, {}]'.format(round(m-h, 2), round(m+h, 2)))

mean_confidence_interval(diamondDf['Price'], 0.95)

print('Interval does not contain null Hypothesis mean of 5600, hence its rejected')

# Example 3(c). Construct a 99% confidence interval for average price of diamonds in NYC.
# Based on this confidence interval, can you conclude whether H0: μ = 5600 may be rejected in
# favour of HA: μ ≠ 5600.

mean_confidence_interval(diamondDf['Price'], 0.99)

print('Interval contains null Hypothesis mean of 5600, hence we fail to reject null hypothesis')


# Example 4. SAT verbal scores of two groups of students are given in SATVerbal.csv. The first
# group, College, contains scores of students whose parents have at least a bachelor’s degree and
# the second group, High School, contains scores of students whose parents do not have any
# college degree. The Education Department is interested to know whether the sample data
# support the hypothesis that students show a higher population mean verbal score on SAT if
# their parents attain a higher level of education.

satScoreDf = pd.read_csv('./MonographDatasets/SATVerbal.csv')
x1Mean = satScoreDf['College'].mean()
x2Mean = satScoreDf['High School'].mean()

t_statistic, p_value_2sided = stats.ttest_ind(satScoreDf['College'], satScoreDf['High School'], nan_policy="omit")
t_statistic1, p_value_2sided1 = stats.ttest_ind(satScoreDf['High School'], satScoreDf['College'], nan_policy="omit")

alpha = 0.05
pvalue = p_value_2sided/2

print('Pvalue is ', pvalue)
print('Pvalue is ', p_value_2sided1/2)

if(pvalue < alpha):
    print('Null Hypothesis is rejected')
else:
    print("We fail to reject null hypothesis")

# Example 5. Typical prices of single-family homes in Florida are given for a sample of 15
# metropolitan areas (in 1000 USD) for 2002 and 2003. Data is provided in Florida.csv. Is there
# any significant evidence that the increase in price is more than 10,000 USD in one year?

# This is a problem of paired sample, since two observations are taken on each sampled unit.

# mUd = mU2003 - mU2002. Noting that the prices are given in 1000USD, the null and alternative
# Hypothesis are formed as H0: mUd <=10 against Ha: mUd > 10


florida = pd.read_csv('./MonographDatasets/Florida.csv')
diff = florida['Jan_2003'] - florida['Jan_2002']
florida['diff'] = diff
mean = florida['diff'].mean()   

print('The mean of the difference in house price from 2003 to 2002 is', mean)

t_statistic, p_value1 = stats.ttest_1samp(florida['diff'], popmean=10)

print('Tstat and pvalue with 1samp', t_statistic, p_value1/2)
if(p_value1/2 < alpha):
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')

# Example 6. In the lockdown period, because of working from home and increased screen time,
# many opted for listening to FM Radio for entertainment rather than watching Cable TV. An
# advertisement agency collected data (TVRadio.csv) on both types of users and would like to
# know whether there is any difference between TV and Radio usage..

# This is a 2 sample problem with sample sizes equal

# H0: mUTV = mURadio against HA: mUTV != mURadio

tvRadio = pd.read_csv('./MonographDatasets/TVRadio.csv')
x1_mean = tvRadio['Cable_TV'].mean()
x2_mean = tvRadio['FM_Radio'].mean()

print('Cable TV mean and Radio Mean are', x1_mean, x2_mean)

t_statistic, p_value = stats.ttest_ind(tvRadio['Cable_TV'], tvRadio['FM_Radio'], equal_var=True)

print('T_statistic and pvalue', t_statistic, p_value)

if(p_value < alpha):
    print('Null hypothesis is rejected')
else:
    print('Fail to reject null hypothesis')
    
    
# Example 7. Among professional drivers sleep deprivation is a serious work hazard. A research
# paper claims that more than half of the night-time drivers drive even when they feel drowsy. A
# sample of 500 night-time drivers were asked whether they ever driven when drowsy, and the
# data is given in Drowsy.csv. Is there evidence that the research paper’s claim is justified?    

# This is a problem of proportions
# The null and alternative hypothesis are H0: Pi <= 0.5 against Ha: Pi > 0.5

drowsy = pd.read_csv('./MonographDatasets/Drowsy.csv')
drowsy['Drive While Drowsy?'].replace(['Yes', 'No'], [1,0], inplace=True)

drowsyYesSum = drowsy.sum()
proportionYes = drowsyYesSum/drowsy.size

print('Drowsy yes sum', drowsyYesSum)
print('Drive while drowsy percentage?', proportionYes)

from statsmodels.stats.proportion import proportions_ztest

z_statistic, p_value = proportions_ztest(drowsyYesSum, drowsy.size, value=0.5, alternative='larger', prop_var=False)

print('t_statistic, pValue are ',z_statistic, p_value)

if(p_value < alpha):
    print('Null hypothesis is rejected')
else:
    print('We fail to reject the null hypothesis')
    
    
    
# CHI SQUARE DISTRIBUTION    

# Example 8. The following table summarizes beverage preference (Beverage.csv) across
# different age-groups. Does beverage preference depend on age?

# Beverage Preference

# Age Tea/Coffee Soft Drink Others
# 21 - 34 25 90 20
# 35 - 55 40 35 25
# > 55 24 15 30
# Table-5 (Beverage Preference)

# H0: Beverage performance is independent of the age against HA: Beverage performance depends on age.

# this is a 3x3 contingency table with df (c-1)(r-1) => (3-1)(3-1) = 4

beverage = pd.read_csv('./MonographDatasets/Beverage.csv')
beverage = beverage.drop('Age', axis=1) # dropping age column as the expected values cannot be determined for the range and it's the null hyp

from scipy.stats import chi2
from scipy.stats import chi2_contingency
chi_2, p, dof, exp_freq = chi2_contingency(beverage)
print('chi2, p, dof, exp_freq', chi_2, round(p,3), dof, exp_freq)

if(p < alpha):
    print('Null Hypothesis is rejected')
else:
    print('We fail to reject the null hypothesis')
    
# Example 9. The following table summarizes the number of hypertensive persons among males
# and females (Hypertension.csv) sampled from a certain population. Is there any evidence that
# the distribution is different among males and females?

# Male Female
# Normal 35 40
# High normal 84 65
# Mild hypertensive 73 75
# Moderate hypertensive 91 87
# Severe hypertensive 60 50
# Total 343 317
# Table-6 Distribution of Hypertension among males and females

# This is also a problem of goodness of fit test. In fact, goodness of fit test statistic has an
# extensive number of applications and testing equivalency of two (or more) distributions is also
# included among them.    
    
# H0: Distribution of hypertension is identical among male and female : against: HA: Distribution of hypertension is not identical


hypertension = pd.read_csv('./MonographDatasets/Hypertension.csv')
hypertension.drop('Type', axis=1, inplace=True)
chi_2, p, dof, exp_freq = chi2_contingency(hypertension)

print('chi2, p, dof, exp_freq', chi_2, round(p,3), dof, exp_freq)

if(p < alpha):
    print('Null Hypothesis is rejected')
else:
    print('We fail to reject the null hypothesis')

# Population variances equality test    
    
# Example 10. The variance of a process is an important quality of the process. A large variance
# implies that the process needs better control and there is opportunity to improve. The data
# (Bags.csv) includes weights for two different sets of bags manufactured from two different
# machines. Consider a statistical test to determine whether there is a significant difference
# between the bag weights for the two machines. Which machine, if any, provides a greater
# opportunity for quality improvement?    

# H0: Ratio of two population variances is equal, HA: unequal

# H0: sigma1^2 = sigma2^2 against HA: sigma1^2 != sigma2^2, sigma1^2/sigma2^2 = 1, HA = sigma1^2/sigma2^2 != 1

def f_test(x,y):
    mach1 = np.array(x)
    mach2 = np.array(y)
    f= np.var(x, ddof=1)/np.var(y, ddof=1)
    degFrMach1 = mach1.size - 1
    degFrMach2 = mach2.size - 1
    pvalue = (1 - stats.f.cdf(f, degFrMach1, degFrMach2))
    pvalue2sided = pvalue * 2
    print('f_statistic, pvalue is ', round(f, 3), round(pvalue2sided,8))
    if(pvalue2sided < alpha):
        print('Null Hypothesis is rejected')
    else:
        print('We fail to reject null hypothesis')

bags = pd.read_csv('./MonographDatasets/Bags.csv')    
f_test(bags.dropna()['Machine 1'], bags.dropna()['Machine 2'])    


