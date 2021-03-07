# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# Line Plot
x = np.arange(1,11)
print(x)

y1 = 2* x
y2 = 3* x

plt.plot(x, y1, color='g', linestyle=':', linewidth=2)
plt.plot(x, y2, color='r', linestyle='-.', linewidth=3)
plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.show()


# sub plots
x = np.arange(1, 11)
y1 = 2*x
y2 = 3*x

plt.subplot(1,2,1)
plt.plot(x, y1, color='g', linestyle=':', linewidth=2)

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='r', linestyle='-.', linewidth=2)

plt.show()

# Scatter Plot

x = np.arange(10, 91, 10)
a = np.arange(9)
np.random.shuffle(a)

plt.scatter(x,a)
plt.show()

# change aesthetics

plt.scatter(x, a, marker='*', c='orange', s=200)
plt.show()

plt.scatter(x, a, marker='*', c='orange', s=200)
b=np.arange(9)
np.random.shuffle(b)
plt.scatter(x, b, marker='.', c='green', s=200)
plt.show()

plt.subplot(1,2,1)
plt.scatter(x, a, marker='*', c='orange', s=200)

plt.subplot(1,2,2)
plt.scatter(x, b, marker='.', c='green', s=200)
plt.show()


# Bar plot

student = {'Bob': 57, 'Matt': 56, 'Sam':27}

names = list(student.keys())
values = list(student.values())

plt.bar(names, values)
plt.show()

# Aesthetics

plt.bar(names, values, color='r')
plt.title('Bar Plot')
plt.xlabel('Names')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

plt.barh(names, values)
plt.title('Bar Plot')
plt.xlabel('Marks')
plt.ylabel('Names')
plt.grid(True)
plt.show()

# Histogram

data = [1,1,3,3,3,3,3,9,9,4,4,4,8,8,8,8,6,7]
plt.hist(data, color='g')
plt.grid(True)
plt.show()

# Box plot and Violin Plot
one = [1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,8,7,6,5,4]

data = [one,two,three]
plt.boxplot(data)
plt.show

plt.violinplot(data,showmedians=True)
plt.show()


# Pie Chart and Doughnut Chart

fruit=['Apple', 'Orange', 'Mango', 'Guava']
quantity = [67, 34, 100, 29]

plt.pie(quantity, labels=fruit)
plt.show()

# colors and show value in decimals
plt.pie(quantity, labels=fruit, autopct='%0.1f%%', colors=['yellow', 'grey', 'blue', 'black'])
plt.show()

# Doughnut chart is achieved through radious mentioned for inner pie and outer pie
plt.pie(quantity, labels=fruit, autopct='%0.1f%%', colors=['yellow', 'grey', 'blue', 'black'], radius=3)
plt.pie([1], colors=['g'], radius=1)
plt.show()



