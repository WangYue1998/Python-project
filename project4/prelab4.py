def total( start, end ):

   tot = 0

   for n in range(start,end):
       tot += n

   return tot

A = total( 0, 10 ) # )+1+2+3+4+5+6+7+8+9
print(A)

def total( start, end ):

   tot = 0

   for n in range(start,end):
       tot += n

   return tot

B = total( 8, 12 )# 8-11
print(B)

def total( start, end ):

   tot = 0

   for n in range(start,end):
       tot += n

   return tot

C = total( 15, 15 )
print(C)

def total( start, end ):

   tot = 0

   for n in range(start,end):
       tot += n

   return tot

D = 3 * total( 4, 7 ) + 10
print(D)

def total( start, end ):

   tot = 0

   for n in range(start,end):
       tot += n

   return tot

X = 5
E = total( 2*X, 12 )
print(E)

def test( a, b ):
   ''' Parameters a and b are in the namespace of the function 'test' '''
   a = 7

   print( "In test, value of a:", a ) # Line 1 #7

   print( "In test, value of b:", b ) # Line 2 #2

   # x is not in the function's namespace so this is a global reference
   # Global references such as this are NOT allowed in CSE 231!
   print( "In test, value of x:", x ) # Line 3 #5

a = 1
b = 2
x = 5
y = test( a, b )

print( "In main, value of a:", a ) # Line 4 #1

print( "In main, value of b:", b ) # Line 5 # 2

print( "In main, value of x:", x ) # Line 6 #5

print( "In main, value of y:", y ) # Line 7

def test( a, b ):
   ''' Parameters a and b are in the namespace of the function 'test' '''
   a = 7

   print( "In test, value of a:", a ) # Line 1 #7

   print( "In test, value of b:", b ) # Line 2 #2
   # x is not in the function's namespace so this is a global reference
   # Global references such as this are NOT allowed in CSE 231!
   print( "In test, value of x:", x ) # Line 3 #5

   return a   # THIS LINE ADDED FOR THIS QUESTION a=7

a = 1
b = 2
x = 5
y = test( a, b )

print( "In main, value of a:", a ) # Line 4 #1

print( "In main, value of b:", b ) # Line 5 #2

print( "In main, value of x:", x ) # Line 6 #5

print( "In main, value of y:", y ) # Line 7 #7