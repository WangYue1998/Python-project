#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:50:33 2017

@author: wy
"""

# Laboratory Exercise #1 (Part A)

AAA=input("Please enter the value of AAA:")
BBB=input("Please enter the value of BBB:")
CCC=input("Please enter the value of CCC:")
DDD=input("Please enter the value of DDD:")
EEE=input("Please enter the value of EEE:")
FFF=input("Please enter the value of FFF:")

str1_float=float(AAA)
str2_float=float(BBB)
str3_float=float(CCC)
str4_float=float(DDD)
str5_float=float(EEE)
str6_float=float(FFF)

# Give the value displayed by each of the calls to "print" below.

A = str2_float // str1_float

print( "\nValue of A: ", A )     # Value of A: _2___________

B = str2_float % str1_float

print( "\nValue of B: ", B )
C = str4_float * 3 + str6_float

print( "\nValue of C: ", C )     # Value of C: _38___________

D = str5_float - str6_float * 4

print( "\nValue of D: ", D )     # Value of D: _-7___________

E = str5_float // str6_float+ str3_float

print( "\nValue of E: ", E )     # Value of E: __3__________

F = str5_float// (str6_float + str3_float)

print( "\nValue of F: ", F )     # Value of F: __2__________

G = str6_float // 2 * 2

print( "\n2Value of G: ", G )     # Value of G: _4___________
