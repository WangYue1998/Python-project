###############################################################################
# Computer Project #9
# investigate the most common Twitter hashtags used by a few MSU-related
#    Twitter accounts, and the similarity of hashtag-use between accounts.
# Use dictionaries to help count frequency of hashtags,
#   and sets to easily answer questions about shared hashtags between users.
# The question need to answer:
# “What are the most common hashtags used by users collectively?”
# “What are the most common hashtags used by users as individuals?”
# “How does hashtag similarity between two users vary over time?”
# use different functions to get the the final answer and show result
###############################################################################


'''Skeleton file with all strings for Mimir testing'''

import string, calendar, pylab
MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]



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
    #if there's no hashtag in the string
    if '#' not in s: 
        return False 
    #looking at all the punctuation in #string.punctuation
    for ite in string.punctuation: 
        #if there's punctuation in #the string, not including #
        if ite in s and ite != '#': 
                return False 
    #looking at numbers 0-9
    for i in range (0,10):
        #if there's a number in the string
        if str(i) in s[1]: 
                    return False 
    #if not of those things are False, return True
    return True 


                    
def get_hashtags(s):
    '''This function has one parameter, a string which is a tweet, 
    and returns a list of valid hashtags in the tweet string'''
    #create and empty list for the hashtags 
    ha_list = [] 
    #split up the string at the spaces
    stri = s.split() 
    #iterate through each word in the string
    for item in stri: 
        #if there's a hashtag in the word
        if '#' in item: 
            #check to make sure it's a valid #hashtag
            if validate_hashtag(item): 
                #if it is, append it to hash_list
                ha_list.append(item) 
    return ha_list 


def read_data(fp):
    ''' read the data in fp collecting 3 things from each row.
    This function return a list of 3-entry lists, where there is 
    a 3-entry list for each line of the csv file: 
        [username, month, list_of_hashtags].'''
    #create an empty list of all the data
    dat_list = []
    #create and empty list containing the hashtags
    hash_list = [] 
     #iterate through each line in the file
    for line in fp:
        #create an empty list that will go into the data_list
        line_list = [] 
        #strip the spaces and split it at #the commas
        line = line.strip().split(',') 
         #user is line at index 0
        user = line[0]
        #append all the users to line_list
        line_list.append(user) 
        #turn the month from a strig to an int
        month = int(line[1]) 
        #append the month to line list
        line_list.append(month) 
      #call get_hashtags function to get# a list of all the hashtags in a tweet
        hash_list = get_hashtags(line[2])
        #put the list of hashtags in line_list
        line_list.append(hash_list) 
        #put line_list in dat list
        dat_list.append(line_list) 
    return dat_list 
    


def get_histogram_tag_count_for_users(data,usernames):
    '''This function creates a histogram of hashtags for how often they occur.
    The key is the hashtag; the value is the count of occurrences of the 
    hashtag.This function return the histogram as a dictionary.'''
    word_count_dict= {}
    for ch2 in data:
        if ch2[0] in usernames:
            for word in ch2[2]:
      
                if word in word_count_dict:
                    word_count_dict[word] +=1
                else:
                    word_count_dict[word] = 1

    return word_count_dict
    

    
def get_tags_by_month_for_users(data,usernames):
    
    '''this function builds a set of unique hashtags grouped by the month 
    in which they are used. This function returns a lists of tuples: 
        specifically a sorted list of (key,value) tuples where each key 
        is a month (int), and each associated value is a set of hashtags 
        used by usernames in that month.'''
    dic=dict()
    dic[1]=set()
    dic[2]=set()
    dic[3]=set()
    dic[4]=set()
    dic[5]=set()
    dic[6]=set()
    dic[7]=set()
    dic[8]=set()
    dic[9]=set()
    dic[10]=set()
    dic[11]=set()
    dic[12]=set()
    for h in data:
        if h[0] in usernames:
            month=h[1]
            taglis = h[2]
            for charac in taglis:
                tag = charac
                dic[month].add(tag)
    l= sorted ((k,v) for k,v  in dic.items())
    return l
    

def get_user_names(L):
    
    '''Return a sorted list of user names that are in the Twitter data '''
    lis=[]
    for t in L:
         if t[0] not in lis:
             lis.append(t[0])
    return sorted(lis)
    
    
    
def three_most_common_hashtags_combined(L,usernames):

    '''Answers the question “What are the most common hashtags used by users 
    collectively?” Return an ordered list of three (count, hashtag) tuples 
    where count is the count of all occurrences of hashtag across all 
    users in usernames.'''
    count_dic= get_histogram_tag_count_for_users(L,usernames)
    
    li=[]
    for k, v in count_dic.items():
        t=tuple()
        tag= k
        count=v
        t=(count,tag)
        li.append(t)
    li= sorted(li,reverse=True)
    l=[]
    l.append(li[0])
    l.append(li[1])
    l.append(li[2])
    return l
        

def three_most_common_hashtags_individuals(data_lst,usernames):
    
    '''Answers the question “What are the most common hashtags used by users 
    as individuals?” Return an ordered list of three (count, hashtag, username)
    tuples where count is the count of occurrences of hashtag only for a user 
    in usernames.'''
    T=[]
    s=set()
    for chup in data_lst:
        user=chup[0]
        s.add(user)
        
    for cho in s:
        user= cho
        count_dic= get_histogram_tag_count_for_users(data_lst,user)
        for k, v in count_dic.items():
            hashtag= k
            count= v
            t= (count, hashtag, cho)
            T.append(t)
    T= sorted(T, reverse= True)
    
    return T[0:3]    
    
    
    
    
            
def similarity(data_lst,user1,user2):
    
    '''Answers the question “How does hashtag similarity between the users 
    user1 and user2 vary over time?”Compares the hashtags used by each user 
    for each month, and returns the numbers of hashtags which were used by
    both accounts in that month.
    '''
    user1lis = get_tags_by_month_for_users(data_lst,user1)
    user2lis = get_tags_by_month_for_users(data_lst,user2)

    T=[]
    for i in range(0,12):
        month =  user1lis[i][0]
        s =  user1lis[i][1]
        set1=set()
        for chara in s:
            set1.add(chara)
        s2=  user2lis[i][1]
        set2=set()
        for chara in s2:
            set2.add(chara)
        inters= set1 & set2
        t=(month, inters)
        T.append(t)
    return T
            
        
        
     
def plot_similarity(x_list,y_list,name1,name2):

    '''Plot y vs. x with name1 and name2 in the title.'''
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+name1+' and '+name2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    pylab.savefig("plot.png")
    
    
def main():
    
    
    
    '''call the previous function and answer the three questions also show
    the results'''
    # Open the file
    filepointer= open_file()
    # Read the data from the file
    dat= read_data(filepointer)

    # Create username list from data
    user = get_user_names(dat)
   
    # Calculate the top three hashtags combined for all users
 
    topcombined = three_most_common_hashtags_combined(dat,user)
    #print(topcombined)
    # Print them
    print()
    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag"))
    # printing loop goes here
    for ch in topcombined:
        count= ch[0]
        hashtag=ch[1]
        print("{:>6d} {:<20s}".format(count , hashtag))
    # Calculate the top three hashtags individually for all users
    topindivi= three_most_common_hashtags_individuals(dat,user)
    # Print them
    print()
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    # printing loop goes here
    for ch in topindivi:
        count= ch[0]
        hashtag= ch[1]
        user= ch[2]
        print("{:>6d} {:<20s} {:<20s}".format(count , hashtag, user))
    print()
        
    # Prompt for two user names from username list
    usernames_str='MSUnews, WKAR, WKARnewsroom, michiganstateu'
    print("Usernames: ", usernames_str)
    l= usernames_str.split(',')
    userl=[]
    for ch in l:
        c= ch.strip()
        userl.append(c)
    
    while True:  # prompt for and validate user names
        user_str = input("Input two user names from the list, comma separated: ")
        if ',' not in user_str:
            print("Error in user names.  Please try again")
            continue
        else:   
            L= user_str.split(',')
            
            L[0]= L[0].strip()
            L[1]= L[1].strip()
            if L[0] and L[1]  in userl:
                user1= L[0]
                user2= L[1]
                break
            # check to for correct user names goes here           
            else:
                print("Error in user names.  Please try again")
                continue

    # Calculate similarity for the two users
    simi =similarity(dat,[user1],[user2])
    
    # Print them
    print()
    print("Similarities for "+user1+" and "+user2)
    print("{:12s}{:6s}".format("Month","Count"))
    #  printing loop goes here
    # create x_list and y_list
    y_list=[]
    lis=['January','February','March','April','May','June','July','August',\
            'September','October','November','December']
    x_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    for i in range(0,12):
        month=lis[i]
        tag= simi[i][1]
        y_list.append(len(tag)) 
        
        print("{:12s}{:<6d}".format(month,len(tag)))          
    print()
    
    # Prompt for a plot
    # Prompt to plot or not and plot if 'yes'
    choice = input("Do you want to plot (yes/no)?: ")
    if choice.lower() == 'yes':
        plot_similarity(x_list,y_list,user1,user2)        
    
if __name__ == '__main__':
   main()
   

