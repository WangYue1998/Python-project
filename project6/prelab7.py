A = 3 * list("25")
print( A )

C = "a" in ["aardvark"]
D = "a" in ["a","n","t"]
print( C, D ) 

E = ["Arthur", "King", "of", "the", "Britons"]

print(E[1])
print(E[1][2])
print(E[:2])


F = []
F.append( 45 )
for n in range(4):
    F.append( 10*n-3 )

print( F ) 


G = [ 10, 20, 30, 40, 20 ]
H = G.pop()
print(H,G)

G = [ 10, 20, 30, 40, 20 ]
I = G.index( 40 )
J = G.count( 20 )
print( I, J )


K = [ 15, -7, 12, -4, 14 ]
print(sorted(K))
print(K)
K.sort()
print(K)

L = " to be, or not to be "

M = L.split()
print( M ) 
N = L.split( "," )
print( N ) 

P = [ "One", "Two", "Three" ]

Q = " ".join( P )
print( Q ) 

R = ", ".join( P )
print( R )

S = "Hello World"
T = S.split()

for item in T:
    print(item)
print("----------") 
for a,b in enumerate(T):
    print(a,b)