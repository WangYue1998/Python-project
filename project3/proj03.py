###############################################################################
#  Computer Project #3
#   repeat prompt for words
#   collect vowels and consonants
#   until collected all possible vowels or at least five different consonants
#   only consonants collected are those after the final vowel in a word
#   display results of vowels and consonants
###############################################################################

# all possible vowels(a, e, i, o, u)
VOWELS = "aeiou"

# initialize the vowels and consonants to be empty string
vowels_count_str=""
consonants_count_str=""

#keep looping while not having enough vowels and not having enough consonants
while len(vowels_count_str)<5 and len(consonants_count_str)<5:
    # assume a word has at least one vowel
    in_str= input("Input a word: ")
    in_str = in_str.lower()
    # initialize the final vowel's index in a word is -1
    last_vowels = -1
    # find the vowels in word
    for i, ch in enumerate(in_str):
        if ch in VOWELS:
            # change the index of last value
            last_vowels=i 
            # if this vowel is a new vowel for output
            if ch not in vowels_count_str:
                # update the vowels of output
                vowels_count_str += ch
                
    #find the consonants in a word after the final vowel in the word
    consonants_str= in_str[last_vowels+1:]
    #check the consonant is empty or not
    if consonants_str:
        for ch in consonants_str:
            # if this consonants is a new consonant for output
            if ch not in consonants_count_str:
                #update the consonants of output
                consonants_count_str+=ch             
                            
#here are three lines of the output
#display the results of vowels and consonants
print("\n"+"="*12)               
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels","length","consonants", \
"length"))
print("{:8s}{:<7d} | {:12s}{:<7d}".format(vowels_count_str,\
      len(vowels_count_str),consonants_count_str,len(consonants_count_str)))