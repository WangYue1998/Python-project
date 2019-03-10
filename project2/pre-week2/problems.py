# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




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

print()
print("")

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

#  HERE
# + SHE
# -----
# COMES

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
                                #C,E,H,M,O,R,S = 10,10,10,10,10,10,10
                            else:
                                S += 1
                        R += 1
                    O += 1
                M += 1
            H += 1
        E += 1
    C += 1

