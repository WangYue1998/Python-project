
import string, calendar, pylab
MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

import csv

def open_file():
    '''This function returns a file pointer. 
    It repeatedly prompts for a file until one is successfully opened. 
   '''
    filename = input("Input a filename: ")
    while True:
        try:
            fp = open(filename,'r')
            break
        except FileNotFoundError:
            print("Error in input filename. Please try again.")
            filename = input("Input a filename: ")
    return fp

def validate_hashtag(s):
    '''check the hashtag is valid or not'''
    if s.find('#') == 0:
        if len(s[1:])==1 and s[1].isdigit():
            return False
        else:
            for ch0 in s[1:]:
                if ch0 in string.punctuation:
                    return False
        return True
                


def get_hashtags(s):
    '''This function has one parameter, a string which is a tweet, 
    and returns a list of valid hashtags in the tweet string'''
    beginning = s.find('#')
    list_of_hashtags=[]
    while beginning != -1 :
        end = s.find(' ',beginning) #look for end of word since start
        if end == -1 :                                                
            ht = s[beginning: ]
            ht = ht.strip()
            if validate_hashtag(ht):
               list_of_hashtags.append( ht )
               break
        ht = s[beginning:end]
        ht = ht.strip()                                              
        if s[beginning] == '#' and validate_hashtag(ht):
            list_of_hashtags.append( ht )
        beginning = s.find('#',end) #look for next word since last end
        
        
    return list_of_hashtags


def read_data(fp):
    ''' read the data in fp collecting 3 things from each row.
    This function return a list of 3-entry lists, where there is 
    a 3-entry list for each line of the csv file: 
        [username, month, list_of_hashtags].'''
   
    fp_csv = csv.reader(fp)
    lis=[]
    
    for line in fp_csv:
        line_lis=[]
        username= line[0]
        month= int(line[1])
        tweet= line[2]
        #print(tweet)
        list_of_hashtags = get_hashtags(tweet)
        #print(list_of_hashtags)
        count=0
        if '#SpartansWill' in list_of_hashtags:
            count+=1
        print(tweet,':', count)
        line_lis=[username, month, list_of_hashtags]
        lis.append(line_lis)
        
    return lis

filepointer= open_file()
    # Read the data from the file
dat= read_data(filepointer)
    # Create username list from data
#user = get_user_names(dat)