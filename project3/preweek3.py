#A
A = 3 * "125"
print( "Value of A:", A )            # Value of A: ____________

B = 3 * int( "125" )
print( "Value of B:", B )            # Value of B: ____________

C = 3 * str( 125 )
print( "Value of C:", C )            # Value of C: ____________

D = "a" + "bc" * 2
print( "Value of D:", D )            # Value of D: ____________

E = ("A" + "BC") * 2
print( "Value of E:", E )            # Value of E: ____________

F = "a" in "aardvark"
print( "Value of F:", F )            # Value of F: ____________

G = "ad" in "aardvark"
print( "Value of G:", G )            # Value of G: ____________

ZZZ = "Arthur, King of the Britons"

H = ZZZ[:4]
print( "Value of H:", H )            # Value of H: ____________

I = ZZZ[-3:]
print( "Value of I:", I )            # Value of I: ____________

J = ZZZ[-6:-2]
print( "Value of J:", J )            # Value of J: ____________
print()
#B
S1 = "Tiger"
S2 = "tiger"

A = S1 == S2
print( "Value of A:", A )            # Value of A: ____________

B = S1 > S2
print( "Value of B:", B )            # Value of B: ____________

C = S1[0] != S2[0]
print( "Value of C:", C )            # Value of C: ____________

D = S1[-1] == S2[-1]
print( "Value of D:", D )            # Value of D: ____________

S3 = "aardvark"
S4 = "anteater"

E = S3 == S4
print( "Value of E:", E )            # Value of E: ____________

F = S3 < S4
print( "Value of F:", F )            # Value of F: ____________

G = len(S3) == len(S4)
print( "Value of G:", G )            # Value of G: ____________

S5 = "ants"
S6 = "anteater"

H = S5 < S6
print( "Value of H:", H )            # Value of H: ____________

I = len(S5) < len(S6)
print( "Value of I:", I )            # Value of I: ____________

J = S5[0] != S6[0]
print( "Value of J:", J )            # Value of J: ____________

K = S5[-1] == S6[-1]
print( "Value of K:", K )            # Value of K: ____________
print()
#C
AAA = "Python"
BBB = "1345 Engineering"
CCC = "Sequence"

A = AAA.isupper()
print( "Value of A:", A )            # Value of A: ____________

B = AAA.isalpha()
print( "Value of B:", B )            # Value of B: ____________

C = BBB.isdigit()
print( "Value of C:", C )            # Value of C: ____________

D = BBB.isalnum()
print( "Value of D:", D )            # Value of D: ____________

E = CCC.lower().upper()
print( "Value of E:", E )            # Value of E: ____________

F = CCC.count( "e" )
print( "Value of F:", F )            # Value of F: ____________

G = CCC.find( "e" )
print( "Value of G:", G )            # Value of G: ____________

H = CCC.find( "en" )
print( "Value of H:", H )            # Value of H: ____________

I = CCC.rfind( "e" )
print( "Value of I:", I )            # Value of I: ____________

J = CCC.replace( "e", "X" )
print( "Value of J:", J )            # Value of J: ____________

K = CCC.replace( "qu", "ZZZ" )
print( "Value of K:", K )            # Value of K: ____________
print()
#D
message = "Values {} and {}."

A = message.format( 25, -37 )

print( "A:", A )                         # A: _____________________

B = message.format( 1.25, "Zero" )

print( "B:", B )                         # B: _____________________

pattern = "|{:5d}| |{:4d}|"

C = pattern.format( 175, -93 )

print( "C:", C )                         # C: _____________________

pattern = "|{:>+5d}| |{:<-4d}|"

D = pattern.format( 175, -93 )

print( "D:", D )                         # D: _____________________

E = pattern.format( -87, 26 )

print( "E:", E )                         # E: _____________________

pi = 3.141592653589793

F = "{:.4f}".format( pi )

print( "F:", F )                         # F: _____________________

G = "{:8.4f}".format( pi )

print( "G:", G )                         # G: _____________________

min_flt = 2.2250738585072014e-308

H = "{:.4e}".format( min_flt )

print( "H:", H )                         # H: _____________________

I = "{:.4f}".format( min_flt )

print( "I:", I )                         # I: _____________________

max_flt = 1.7976931348623157e+308

J = "{:.4e}".format( max_flt )

print( "J:", J )                         # J: _____________________

K = "{:.4f}".format( max_flt )

print( "K:", K )                         # K: _____________________