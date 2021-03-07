nums = [12, 13, 14, 15, 8, 10]
# for loop
for num in nums:
    if num % 5 == 0:
        print('Divisble by 5')
    elif num % 2 == 0:
        print('Divisible by 2')
    else:
        print('Not Divisible by 2 or 5')

# >>list
# 0, 1, 2, 3, 4, 5
# -5, -4, -3, -2, -1, 0
simple_list = ['Sai', 2, 3, 4, 'hello', 2.2145]
print(simple_list)
print(type(simple_list))
print(type(simple_list[0]))
# simple_list[0] is same as simple_list[-5]
print(simple_list[-1])  # Negative index points the number from right to left: -1 is the first right index
print(type(simple_list[-1]))

# >>Lists operations

simple_list[3] = 52
print(simple_list)

# append() add the element at the end
simple_list.append('added at the back')
print(simple_list)

# len to get length
print(len(simple_list))

# remove elements with pop with an index
simple_list.pop(4)
print(simple_list)

# >> Initialize a whole list with same value
repeated_list = [5] * 4
print('repeated_list', repeated_list)

# >> Have list inside a list
simple_list[1] = [1, 2, 3]
print('simple_list in a simple_list', simple_list)
print('simple_list in a simple_list item', simple_list[1][1])

# >> Copying lists
print('>> Copying lists: Gotcha, lists carry references')

list2 = simple_list
print('list2', list2)
print('simple_list', simple_list)
list2[1] = 0
print('list2', list2)
print('simple_list', simple_list)

# >> List copy using copy(), it clones the original

print('\n >> List copy using copy() \n')
list3 = simple_list.copy()
print('list3', list3)
print('simple_list', simple_list)
list3[0] = 'Veer'
print('list3', list3)
print('simple_list', simple_list)

# >> Tuple, it's an immutable, you cannot change it, still there's a work around
print('\n>> Tuple, it\'s an immutable list, you cannot change it\n')
simple_tuple = (12, 42, 34, 67, 45)
print('simple_tuple', simple_tuple)
print('simple_tuple[1]', simple_tuple[1])
# Gives an error when you try and change it
# simple_tuple[0] = 123 # TypeError: 'tuple' object does not support item assignment
# There's a work around though!
dummy = list(simple_tuple)
dummy[0] = 123
simple_tuple = tuple(dummy)
print('simple_tuple', simple_tuple)

# >> Set is a data structure like list, it doesn't allow duplicates and it's un ordered
print('\n>> Set is a data structure like list, it doesn\'t allow duplicates and it\'s un ordered\n')
simple_set = {11, -2, 'sai', -2}  # outputs {11, 'sai', -2}
print('simple_set', simple_set)
# simple_set[1]  #  TypeError: 'set' object is not subscriptable, as there's no order or indexing
# How to get the elements in Set?
print('sai' in simple_set)
# Add elements
simple_set.add(75)
print('simple_set.add(75)', simple_set)
# Remove elements
simple_set.remove('sai')
print('simple_set.remove(sai)', simple_set)

# >> Dictionary is a data structure like a javascript's Object
print('\n>> Dictionary is a data structure like a javascript\'s Object\n')
simple_dict = {
    'brand': 'Apple',
    'product': 'iPhone',
    'model': '12'
}
print('simple_dict', simple_dict)
print('I bought an', simple_dict['product'], 'model', simple_dict['model'], 'from', simple_dict['brand'])
# Change dictionary value using assignment
simple_dict['model'] = '12 Max Pro'
print('I bought an', simple_dict['product'], 'model', simple_dict['model'], 'from', simple_dict['brand'])
# Add new entries in the dictionary
simple_dict['color'] = 'Red'
print('I bought an', simple_dict['product'], 'model', simple_dict['model'], 'from', simple_dict['brand'], 'in',
      simple_dict['color'], 'color')

# >> Accessing data in lists
print('\n>> Accessing data in lists using startIndex(inclusive):endIndex(not_inclusive)\n')
simple_list = [1, 5, 2, 6, 7, 8, 9, 10]
print('simple_list', simple_list)
# [startIndex(inclusive):endIndex(not_inclusive)]
print('simple_list[2:5]', simple_list[2:5])
# More like lists, we can give negative numbers as well
print('simple_list[-5:-2]', simple_list[-5:-2])

# >> Loops

print('\n>> For Loop\n')

counter = 0
simple_list = [0, 1, 2, 3, 'x', 5, 6, 7, 8, 9, 10]

# Basic for loop
for i in simple_list:
    print('i', i)
    counter += 1

# For loop with limited set of list elements
for i in simple_list[0:4]:
    for j in simple_list[4:]:
        print('> J loop i*j', i * j)
    print('> i loop')

# Using range()
print('range(6)', range(6))

# Using for and range() together
# range is [0, 1, 2, 3, 4, 5] total 6 elements
for i in range(6):
    print('i in range', i)

# specify start and end in a range(start_InclusiveIndex, end_not_inclusiveIndex)
for i in range(2, 10):
    print('i in range(2, 10)', i)

# increment range index with a number
for i in range(2, 10, 2):
    print('i in range(2, 10, 2)', i)

# covert a range of numbers to a list
print('list(range(2, 15, 3))', list(range(2, 15, 3)))

# >> While Loop
i = 4
while i < 10:
    print('i< 10', i) 
    i += 1

# >> Conditionals

# if, else and elif conditions

for i in range(25):
    if i < 10:
        print(i, 'is less than 10')
    elif i < 20:
        print(i, 'is less than 20')
    else:
        print(i, 'is neither less than 10 or 20')

a = 1

# Check if given string is in upper case or not
nameString = 'My Name is Adam'
print(nameString.isupper())

# Get the length of the string
nameString = 'My Name is Adam'
print(len(nameString))

# Write code in a for loop to print sum of all elements in a list
listToSum = [6, 5, 3, 8, 4, 2, 5, 4, 11, 43]
valueToSum = 0
for i  in listToSum:
    valueToSum += i
print(i)

# Write a python code( using only while loop) which will only print the even numbers from 2 to 12.
# Quirky way without using an index to retrieve the list items
rangeList = list(range(2, 13))
rangeList.reverse()  # To get items from 2 to 12
while len(rangeList) != 0:
    poppedValue = rangeList.pop();
    if poppedValue % 2 == 0:
        print('even', poppedValue)
        
inRangeList = list(range(2, 13, 2))
index = 0
while index < len(inRangeList):
    print(inRangeList[index])
    index += 1
        
# Write a code( using if-else statement), which will print the minimum of the below given numbers. x=50,y=30,z=40        
x = 50
y = 30
z = 10

if x < y and  x < z:
        print(x, 'is the smallest')
elif y < z and y < x:
        print(y, 'is the smallest')
elif z < x and z < y:
        print(z, 'is the smallest')
        
if (x < y) and (x < z):
    print("x is the smallest number")
elif (y < z):
    print("y is the smallest number")
else: 
    print("z is the smallest number")       
    
# Find square root from Math library

import math

print('math.sqrt(25)', math.sqrt(25))
print('math.floor(25.234545)', math.floor(25.234545))
print('math.ceil(25.234545)', math.ceil(25.234545))
print('math.pow(3, 2)', math.pow(3, 2))  # or 3**2
print('math.pi', math.pi)
print('math.epsilon', math.e)

import math as m  # Aliases

print(m.sqrt(25))

# import just what you need
from math import sqrt, pow

print('sqrt(25)', sqrt(25))
print('pow(4, 5)', pow(4, 5))

# Expecting a client input
# input always gives value in 'str'

# x = int(input('Enter first number\n'))
# y = int(input('Enter second number\n'))
# print('x+y', x + y)

# evaluate expression 

#print(eval(input('enter an expression\n')))

# send input from command prompt to python using 'argv'
# from sys import argv
# x = argv[1]
# y = argv[2]
# print(x+y)

# Arrays in Python are definitely typed

from array import *

vals = array('i', [5, 9, 8])
print(vals)

# define a function

def greet() :
    print('Greet function called')
    return 1,2 # Yes function can return multiple values
    
result1, result2 = greet()
print('result1, result2', result1, result2)    


# Anonymous functions

anonyyF = lambda x: x*2

print(anonyyF(10))

# __name__
print(__name__)



# global variables

a = 10 
b = 12
def something():
    global a
    a = 15
    b = globals()['b']
    print('in fun', a)
    print('in fun b', b + 1)
something()
print('outside a', a)    
print('outside b', b)    

# Use globals()['a'] and get the value assign it to local variable


# def calculateEMI():
#     principal = float(input('Enter principal amount\n'))
#     rateOfInterest = float(input('Enter rate of interest\n'))
#     tenure = int(input('Enter tenure in months\n'))
#     powRateOfInterest = (1 + rateOfInterest)**tenure
#     emi = (principal * rateOfInterest * powRateOfInterest)/(powRateOfInterest - 1)
#     print('EMI to be paid for the principal of', principal, 'at a rate of interest', rateOfInterest, 'for', tenure, 'months is', emi)
# 
# calculateEMI()


def findLoveAndWarCount():
    trumpMessage = "We want to achieve a stable, peaceful world with less conflict and more common ground. I am proposing a new foreign policy focused on advancing America's core national interests -- so important -- promoting regional stability and producing and easing the tensions within our very troubled world. This will require rethinking the failed policies of the past. We can make new friends, rebuild old alliances and bring new allies into the fold. And we can do that. I'm proud to have the support of war-fighting generals, active duty military and top experts who know both how to win and how to avoid endless wars that we're caught up in, like the one we have right now that just never ever ends, our longest war. Just yesterday, 88 top generals and admirals endorsed my campaign. And these people are fantastic. TRUMP: In a Trump administration, our actions in the Middle East will be tempered by realism. The current strategy of toppling regimes with no plan for what to do in the day after only produces power vacuums that are filled simply by terrorists. Gradual reform, not sudden and radical change, should be our guiding objective in that region. We should work with any country that shares our goal of destroying ISIS and defeat radical Islamic terrorism. TRUMP: And we're going to form new friendships and partnerships based on this mission and this mission alone. We now have an administration and a former secretary of State who refuse to say radical Islamic terrorism. And unless you're going to say the words, you're never going to solve the problem. It's very simple. TRUMP: Immediately after taking office, I will ask my generals to present to me a plan, within 30 days, to defeat and destroy ISIS. TRUMP: This will require military warfare, but also cyber warfare, financial warfare and ideological warfare, as I laid out in my speech on defeating radical Islamic terrorism several weeks ago. Instead of an apology tour, which you saw President Obama give over and over again, I will proudly promote our system of government and our way of life as the best in the world, just like we did in our campaign against communism during the cold war. TRUMP: We will show the whole world how proud we are to be Americans. TRUMP: At the same time, immigration security is a vital part of our national security. We only want to admit people to our country who will support our values and love our people. They have to love our people. TRUMP: These are, in fact, the pillars of a sound national security strategy. Unlike my opponent, my foreign policy will emphasize diplomacy, not destruction. Hillary Clinton's legacy in Iraq, Libya, Syria has produced only turmoil and suffering and death. Her destructive policies have displaced millions of people. Then she has invited these refugees into the West with no plan to screen them, including veteran health care costs -- and this was just announced and read over the last number of weeks -- the price of the wars in Iraq and Afghanistan will total approximately $6 trillion. We could have rebuilt our country over and over and over again. Yet after all this money was spent and lives lost, Clinton's policies as secretary of State have left the Middle East in more disarray than ever before. Not even close. Had we done nothing, we would have been in a far better position. Meanwhile, China has grown more aggressive and North Korea more dangerous and belligerent than ever. Russia has defied this administration at every single turn. Putin has no respect for President Obama and has absolutely no respect for Hillary Clinton. Sometimes it seemed like there wasn't a country in the Middle East that Hillary Clinton didn't want to invade, intervene in or topple. She's trigger happy and very unstable. Whether we like it or not, that's what's going on.".replace('.', '').replace(',', '').upper()
    messageList = trumpMessage.split()
    loveCount = 0
    warCount = 0
    for message in messageList:
        if message.find('LOVE') != -1:
            loveCount += 1
        elif message.find('WAR'):
            warCount += 1
#     print('Trump used "Love" for', messageList.count('LOVE'), 'times and "War" for', messageList.count('WAR'), 'times')
    print('Trump used "Love" for', loveCount, 'times and "War" for', warCount, 'times')

findLoveAndWarCount()


def showProductQuantities():
    branch1ProductList = ['soap', 'detergent', 'chocolate', 'toothpaste', 'soap', 'cornflakes', 'detergent', 'chocolate', 'maggi', 'toothpaste', 'soap', 'detergent', 'chocolate', 'toothpaste', 'soap', 'detergent', 'chocolate', 'toothpaste', 'toothpaste', 'maggi', 'maggi', 'cornflakes']
    branch2ProductList = ['soap', 'detergent', 'brush', 'comb', 'toothpaste', 'soap', 'detergent', 'chocolate', 'toothpaste', 'soap', 'cornflakes', 'detergent', 'chocolate', 'maggi', 'toothpaste', 'soap', 'detergent', 'chocolate', 'toothpaste', 'soap', 'detergent', 'chocolate', 'toothpaste', 'toothpaste', 'maggi', 'maggi', 'cornflakes']
    branch3ProductList = ['juice', 'cake', 'brush', 'comb', 'chips', 'coca-cola', 'pepsi', 'maggi', 'maggi', 'maggi', 'cornflakes', 'cheese', 'maggi', 'pepsi', 'horlicks']
    
    branch1ProductList.extend(branch2ProductList)
    branch1ProductList.extend(branch3ProductList)
    
    productDictionary = {}
    
    for product in branch1ProductList:
        if product in productDictionary:
            productDictionary[product] += 1
        else:
            productDictionary.update({product: 1})
            
    print('Products sold in a day from all 3 branches', productDictionary)

    
showProductQuantities()

# numpyyyy

from numpy import *

# creating array - one way
arr = array([1, 2, 3, 4, 5.0])
print(arr.dtype)
print('numpy array', arr)

# linspace - crazy there's parts here
arr = linspace(0, 100, 5)
print('linspace', arr)

#arange
arr = arange(1, 15, 2)
print('arange', arr)

#logspace
arr = logspace(1, 40, 5)
print('logspace', arr)

#zeros
arr = zeros(5, int)
print('zeros', arr)

#ones
arr = ones(5)
print('ones', arr)

x = [1, 2, 4, 5, 6]

for i in x:
    print('Square of {} is {}'.format(i, i*i))
    

def gstAmount(originalCost, gst):
    return originalCost + ((originalCost * gst) / 100)

    
def calculateGST():
    productDict = {
        'Product1': {'cost': 1000, 'slab': 18 },
        'Product2': {'cost': 250, 'slab': 18 },
        'Product3': {'cost': 125, 'slab': 5 },
        'Product4': {'cost': 345, 'slab': 18 },
        'Product5': {'cost': 820, 'slab': 12 },
        'Product6': {'cost': 980, 'slab': 5 },
        'Product7': {'cost': 500, 'slab': 12 }
        }
    
    for key in productDict:
        product = productDict[key]
        print('GST amount for the product', key, 'is', gstAmount(product['cost'], product['slab']))
    
calculateGST()    
c= {
"fruit": "Apple",
"vegetable": "Tomato",
"flower": "Rose"
}
print(type(c))

