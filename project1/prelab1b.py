#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:26:09 2017

@author: wy
"""

AAA=input("please enter the value of AAA:")
BBB=input("please enter the value of BBB:")
str1_float=float(AAA)
str2_float=float(BBB)
A = 5
A += 1
print("\nValue of A:", A)
B = 8
B += str1_float

print( "\nValue of B: ", B )     # Value of B: ____________

C = 10
C *= str2_float

print( "\nValue of C: ", C )     # Value of C: ____________

D = 10
D *= (str2_float + 3)

print( "\nValue of D: ", D )     # Value of D: ____________

E = 10
E *= str2_float + 3

print( "\nValue of E: ", E )     # Value of E: ____________

F = 14
F -= str2_float

print( "\nValue of F: ", F )     # Value of F: ____________

G = 25
G -= str2_float + 3

print( "\nValue of G: ", G )     # Value of G: ____________

H = 25
H %= 3

print( "\nValue of H: ", H )     # Value of H: ____________

J = I = 36

print( "\nValue of I: ", I )     # Value of I: ____________

print( "\nValue of J: ", J )     # Value of J: ____________