#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:20:42 2017

@author: wy
"""
EUROS_PER_DOLLARS=0.74957
dollars_str=input("Input dollars:")
print(dollars_str)

dollars_flt=float(dollars_str)
print( "Euros:" ,round(dollars_flt*EUROS_PER_DOLLARS,2)) 