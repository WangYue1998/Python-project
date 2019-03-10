#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:05:50 2017

@author: wy
"""
int1 = 10
int2 = 20
print("int1 less than int2:", int1<int2)
print("int1 equal int2:", int1==int2)
print("int1 grater than int2:", int1>int2)
print("int1 not equal int2:", int1!=int2)

my_int=10
print("Chained compare 1:",0<= my_int<=5)
print("Chained compare 2:",0<= my_int<=11)

result_float=2/2.0000000000000000001
# shoud be true on video question
print("Equality results:", result_float==1.0)
print("Better way:", 0.99<= result_float<=1.01)

my_int =1000
if my_int<100:
    print("Yes it is")
print("Moving on")

value_float=1.0
if 0<= value_float <=1.0:
    percent_float =value_float*100
    print("Percent:", percent_float)
print("Moving on")

my_int =27
divisor_int =0
if divisor_int ==0:
     print("Can't divide by zero")
else:
    print("Result:", my_int/divisor_int)
print("Moving on")


num=36
if num<0:
    print("Only positive, try again")
elif num%2==0:
    if num ==0:
        print("It's two:even and prime")
    elif num==0:
        print("It's zero:even, not prime, not composite")
    else:
        print("The value", num, end="")
        print(" is even")
else:
    if num==1:
        print("Number was one:odd, not prime, not composite")
    else:
        print("The value",num, end="")
        print("is odd")
print("Thanks for playing")

#while loop
count_int=5
while count_int>0:
    print("Counting integer is:", count_int)
    count_int = count_int -1
print("Moving on")

orig_value =5
count = orig_value
factorial_result =1

while count>1:
    factorial_result = factorial_result*count
    count=count-1
print("The factorial of", orig_value,"is",factorial_result)

num_int=11
divisor_int = num_int-1
while divisor_int>1:
    if num_int% divisor_int ==0:
        print(num_int,"has a vector",divisor_int)
        break
    divisor_int-=1
else:
    print(num_int,"is prime")
print("Thanks for playing")
    
num_int=10
divisor_int = num_int-1
while divisor_int>1:
    if num_int% divisor_int ==0:
        print(num_int,"has a vector",divisor_int)
        break
    divisor_int-=1
else:
    print(num_int,"is prime")
print("Thanks for playing")    


outer_limit =3
inner_limit =3
counter =0
outer=0
while outer < outer_limit: #0<3
    inner=0
    print("outer:", outer,"inner:", end="")
    while inner < inner_limit:
        print(inner, end=',')
        inner+=1
        counter +=1
    outer +=1
    print()
print("Total iterations:", counter)
print("Outer:", outer, "Inner:", inner)

outer_limit =3
inner_limit =3
counter =0
outer=0
inner=0
while outer < outer_limit: #0<3
    #inner=0
    print("outer:", outer,"inner:", end="")
    while inner < inner_limit:
        print(inner, end=',')
        inner+=1
        counter +=1
    outer +=1
    print()
print("Total iterations:", counter)
print("Outer:", outer, "Inner:", inner)

#  HERE
# + SHE
# -----
# COMES

A=0
while A<=9:
    B=0
    while B<=9:
        C=0
        while C<=9:
            print("ABC",A,B,C)
            C+=1
        B+=1
    A+=1
    
A=0
while A<=9:
    B=0
    while B<=9:
        C=0
        while C<=9:
            if A!=B and A!=C and B!=C:
                print("ABC",A,B,C)
            C+=1
        B+=1
    A+=1

C = 1
while C <= 9:
    E = 0
    while E <= 9:
        H = 1
        while H <= 9:
            M = 0
            while M <= 9:
                O = 0
                while O <= 9:
                    R = 0
                    while R <= 9:
                        S = 1
                        while S <= 9:
                            #print("CEHMORS:",C,E,H,M,O,R,S)
                            if ((H*1000 + E*100 + R*10 + E) + (S*100 + H*10 + E) == C*10000 + O*1000 + M*100 + E*10 + S)\
                               and C != E and C != H and C != M and C != O and C != R and C != S \
                               and E != H and E != M and E != O and E != R and E != S \
                               and H != M and H != O and H != R and H != S \
                               and M != O and M != R and M != S \
                               and O != R and O != S \
                               and R != S:
                                print("SOLUTION CEHMORS:",C,E,H,M,O,R,S)
                                C,E,H,M,O,R,S = 10,10,10,10,10,10,10
                            else:
                                S += 1
                        R += 1
                    O += 1
                M += 1
            H += 1
        E += 1
    C += 1
    #print(C)

 # Write a program that prints the numbers from 1 to 100.
# But for multiples of three print â€œFizzâ€ instead of the number and
# for the multiples of five print â€œBuzzâ€.
# For numbers which are multiples of both three and five print â€œFizzBuzzâ€

n = 1
while n <= 100:
    if n%3 == 0 and n%5 == 0:
        print("FIZZBUZZ", end = ',')
    elif n%3 == 0:
        print("Fizz", end = ',')
    elif n%5 == 0:
        print("Buzz", end = ',')
    else:
        print(n, end=',')
    n += 1   
print ()    
A,B,C,D = 0,0,0,0

while A <= 10:
    A += 2
    if A%3 == 0:
        B += 1
    else:
        C += 1
    D += 1

print( "A =", A )  # Line 1
print( "B =", B )  # Line 2
print( "C =", C )  # Line 3
print( "D =", D )  # Line 4
print("")

A,B,C = 0,0,0

for N in range(11):
    if N%2 == 0:
        A += 1
    elif N%3 == 0:
        B += 1
    else:
        C += 1

print("A =", A)  # Line 1
print("B =", B)  # Line 2
print("C =", C)  # Line 3
print("N =", N)  # Line 4

num_str = input("Input an int: ")
while num_str !=10:
    the_sum
    print()

print(num_int)
