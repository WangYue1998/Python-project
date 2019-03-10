#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:12:00 2017

@author: wy
"""
#first program in python
#input two numbers, add them together, print them out
#wfp,9/1/07
#wfom 1/1/13, to py3

num_str1=input('Please enter an integer:') #hi mom
num_str2=input('Please enter a floating point number:')

str1_int=int(num_str1)
str2_float=float(num_str2) #this is a comment

print('The numbers are:',str1_int,'and',str2_float)
print('Their sum is:', str1_int+str2_float,'and their product is',str1_int*str2_float)