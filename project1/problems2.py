#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:18:43 2017

@author: wy
"""

dividend_int =27
divisor_int =3
print("the result is",dividend_int/divisor_int)
print("The result of " , str(dividend_int) , " / " ,  str(divisor_int) ,  " is: ", \
      str(dividend_int / divisor_int)) 

print("The result of " , dividend_int , " / " ,  divisor_int ,  " is: ", \
      dividend_int / divisor_int) 
print("")

print("The result of " + str(dividend_int) + " / " +  str(divisor_int) +  " is: "+ \
      str(dividend_int / divisor_int))


D = 10
D *= (20 + 3)

print( "\nValue of D: ", D )     # Value of D: ____________

E = 10
E *= 20 + 3

print( "\nValue of E: ", E )     # Value of E: ____________

result_float=2/2.0000000000001
# shoud be true on video question
print("Equality results:", result_float==1.0)