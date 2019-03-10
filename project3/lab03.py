###############################################################################
#  Computer Lab #3
# repeatedly prompt the user to enter a word
# First convert the word to lower case
# The word will be converted to Pig Latin using the following rules:
# If the word begins with a vowel: 
#    append “way” to the end of the word
# If the word begins with a consonant:
#    remove all consonants from the beginning of the word
#    and append them to the end of the word 
#    Then, append “ay” to the end of the word
###############################################################################
#all possible vowels
VOWELS = "aeiou"
# prompt input
word = input("Enter a word ('quit' to quit): ")
# change the word to lower case
word= word.lower()
    
# convert word to Pig Latin form
while word!= 'quit':
    
     # if there is only one character which is consonant
    if len(word)==1:
        for ch in word:
            if ch not in VOWELS:
                print(word+'ay')
                break
            
    
    for i, ch in enumerate(word):
        #If the word begins with a vowel, append “way” to the end of the word
        if i == 0 and ch in VOWELS:
            print(word[:]+'way')
            break
        # If the word begins with a consonant,
        if i == 0 and ch not in VOWELS:
            for i, ch in enumerate(word):
                    if ch in VOWELS:
                         # find the position of vowel
                         vowels = i
                         #append “ay” to the end of the word and priint it  
                         print(word[i:]+word[0:i]+'ay')
                         break
      
    word = input("Enter a word ('quit' to quit): ")
    word= word.lower() 
    
    
        

