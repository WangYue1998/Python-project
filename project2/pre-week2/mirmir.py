#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 09:14:51 2017

@author: wy
"""
#question1
num_str = input("Input an int: ")
num_int = int(num_str)
for num_int in range (1,num_int):
    print(num_int)



#question4
n_str = input("Input an int:")
divisor_int = 1
while divisor_int <= int(n_str):
    if int(n_str) % divisor_int ==0:
        print(divisor_int)
    divisor_int+=1

#question2 how to find the sum
'''Given a series of numbers as input, add them up until the input is 10 and print the total.
Do not add the final 10.
 
For example, if the following numbers are input
8
3
11
10
 
The output should be:
22'''
 
Hint: When you don't know the number of repetitions, always use while loop.
num_str = input("Input an int: ")
while num_str !=10:
    the_sum = int(num_str)
    the_sum += int(num_str)
    print(the_sum)



#question3 how to set n
'''Given the number n as input, print the first n odd numbers starting from 1.
For example if the input is
4
The ourput will be:
1
3
5
7'''
n_str = input("Input an int: ")
number=1
counter=1
while counter<=int(n_str):
    if number%2==1:
        counter+=1
        print(number)
    number+=1
       

#question5 how to find the greatest  common divisor
m = input("Input the first integer: ")
n = input("Input the second integer: ")
divisor_int =1 
common_factor =1
while divisor_int<=int(m) and divisor_int<=int(n):
    if int(m)%divisor_int== 0 and int(n)%divisor_int==0:
        common_factor = divisor_int
    divisor_int+=1        
print(common_factor)
#week 2 inner and hereshecomes
        
        




