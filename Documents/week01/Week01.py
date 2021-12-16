#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:31:49 2021

@author: andreacortes
"""

#print('Hello, World!')

#Step 7: **Use code completion**

#1 + 2 * 3
#(1 + 2) * 3

#for i in range(1,10):
 #   print(i)
    
#Variables in Python:

#Variables store values, they can be looked at or changed within the code. 

   
#total = 0
#for i in range(1,10):
    #total = total + i
    #print(total)
#print ("Final Total: ", total)

#Functions in Python:

#Functions are needed to encapsulate functionalities and make them resusable.
#def say_hello_to(name):
   # print("Hello " + name)

#say_hello_to("Cagatay")
#say_hello_to("Fred")

#Conditionals in Python:

#Conditions are also central to programming to model the logical flow of the code. Change the value variable to see how the if-conditions behave:

#value = 5
#if value > 0:
   # print("This is positive!")
#elif value < 0:
    #print("This is negative!")
#else:
   # 
    
 #Comments in Python:

#Any line that starts with a # is ignored.

#Please ignore me.   

#Data types in Python:
#Basic types:

#x = 3          # numbers  
#a = "gorillas" # strings  
#t = True       # booleans

#Lists:

#What if you have several of the same sort of things? You can use lists to store collections of things. An empty list is declared as []. And we can add elements with append.

#myFavouriteParks = []
#myFavouriteParks.append("Victoria")
#myFavouriteParks.append("Hampstead Heath")
#myFavouriteParks.append("Richmond")
#print (myFavouriteParks)
#print ("-----------------------------------")
#print ("Now the same with a for-loop:")
#for value in myFavouriteParks:
#    print (value)

#Dictionaries

#The other main data type is the dictionary. The dictionary allows you to associate one piece of data (a "key") with another (a "value"). The analogy comes from real-life dictionaries, where we associate a word (the "key") with its meaning. Declare an empty dictionary with {}

#foods = {}
#foods["banana"] = "Yellow"
#foods["avocado"] = "green"
#foods
#foods["banana"]
#print ("now trying with a non-existent key:")


#Loading packages in Python: As we will be making use of several packages and libraries in Python. We need to load them before we use them. This is where import comes into play.
#print ("We need to load the package first:")
#import numpy as np
#myArray = np.arange(10)
#print (myArray)


import csv     # imports the csv module
import sys      # imports the sys module

f = open('TB_burden_countries_2021-10-12.csv') # opens the csv file
for row in csv.reader(f):
    print(row)


import pandas as pd

data = pd.read_csv('TB_burden_countries_2021-10-12.csv')
data

#4272 rows × 50 columns

#Count the number of rows in the csv file you've chosen

rows= len(data)
print("Number of Rows: ", rows)

#Number of Rows:  4272
#Pick one of the columns with numeric data and calculate the average value usinga 
#loop (not a library function such as avg(), we'll come to those soon). One candidate
# is the column with the name "e_prev_num_lo" which is 
#"Estimated prevalence of TB (all forms), low bound" according to the dictionary

total=0
for i in range(len(data['e_inc_num_hi'])):
    try:
        total=total+float(data['e_inc_num_hi'][i])
    except:
        continue
average= total/rows
print("Average= ", average)

#***Now, repeat step-2 above but this time find the averages for years 1990 and

#Have you observed any difference?***
#In 
# As the data starts from 2001, So use 2001 instead of 1991.


df_2001= data[data['year']==2001] 
df_2001.head()

total=0
for i in range(len(df_2001['e_inc_num_hi'])):
    try:
        total=total+float(df_2001['e_inc_num_hi'][i])
    except:
        continue
average= total/len(df_2001)
print("Average for 2001 = ", average)


#Average for 2001 =  852.9431279620853


df_2011= data[data['year']==2011] 
df_2011.head()


total=0
for i in range(len(df_2011['e_inc_num_hi'])):
    try:
        total=total+float(df_2011['e_inc_num_hi'][i])
    except:
        continue
average= total/len(df_2011)
print("Average for 2011 = ", average)

#Average for 2011 =  1221.3534883720931
#Exercise 2: Create an array of int ranging from 5-15

#-*- coding: utf-8 -*-
import numpy as np

np.arange(start=5, stop=15)

c = np.linspace(0, 23, 7)
c



uniform_dist = np.random.uniform(-1,1,1000)
uniform_dist

#Visualise the array in an histogram in matplotlib.


import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(uniform_dist, 15)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()


#Create two random numpy arrays with 10 elements. Find the Euclidean 
#distance between the arrays using arithmetic operators, hint: numpy has
# a sqrt function

f = np.random.rand(10)
g= np.random.rand(10)
def euclidean_distance(a,b):
    return np.sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))
print(euclidean_distance(f,g))







    
    
    
    
    
    
    