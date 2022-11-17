# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:34:50 2021

@author: Rahul
"""

import numpy as np

# Declare Numpy array
numpy_array  = np.array([[1,2,3],[4,6,7]])

np1 = np.array([[1,3],[4,5]])

np2 = np.array([[3,4],[5,7]])


# Multiply Numpy array
mnp = np1 @ np2
mnp2 = np.dot(np1,np2)

mnp3 = np1 * np2
mnp4 = np.multiply(np1,np2)


# Sum and Sub
sum1 = np1 + np2
sub1 = np1 - np2
sub2 = np.subtract(np1,np2)


#Add all cells
element_sum = np.sum(np1)


#BroadCasting
broad_num = np1 + 3

np3 = np.array([[3,4]])
broad_num2 = np1 + np3


#Divide
div = np.divide([12,14,16],5)
div2 = np.floor_divide([12,14,16],5)


#Square Root
sqrt = np.math.sqrt(10)


#Distribution
normal_dist = np.random.standard_normal((3,4))
uniform_dist = np.random.uniform(1,12,(3,4))


#Generate random numbers
random_floatarr = np.random.rand()
random_intarr = np.random.randint(1,50,(2,5))


#Zero and One Array
zero_arr = np.zeros((3,4))
one_arr = np.ones((3,4))


#Filter
filter_ar = np.logical_and(random_intarr>30, random_intarr<50)

f_random_ar = random_intarr[filter_ar]


#Statistics
data = np.array([1,3,4,5,7,9])
#Mean
mean = np.mean(data)
#Median
median = np.median(data)
#Variance
var = np.var(data)
#standard deviation
sd = np.std(data)

numpy_array  = np.array([[1,2,3],[4,6,7]])

var1 = np.var(numpy_array, axis=1)
var2 = np.var(numpy_array, axis=0)
