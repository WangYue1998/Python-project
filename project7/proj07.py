###############################################################################
# Computer Project #7
# determine the country of origin of the IP addresses that attacked the network
# use open_file(message) to prompt the user for one filename
# use read_ip_location(file) to read a range of IP addresses corresponding to 
#    a specific two-digit country code
# use read_ip_attack(file) to reads detected IP addresses corresponding to 
#    an attack to a network. 
# use read_country_name(file) to read the country code and its corresponding 
#    full name.
# use locate_address(ip_list, ip_attack) to searches for the IP address of one 
#    attack in the list of IP addresses 
# get_country_name(country_list, code)return the name corresponding to the code
# bar_plot(count_list, countries) dispalys the bar plot
# use main() to call previous fnctions and get result
###############################################################################


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pylab
from operator import itemgetter

def open_file(message):
    ''' has one parameter: message, a string. This function prompts the user
    to enter a filename displaying the message provided. The program will try 
    to open a file. An error message will be shown if the file cannot be 
    opened. This function will loop until it receives proper input and 
    successfully opens the file. It returns a file object.'''
    file_name = input(message)
    # while loop
    while True:
        try:
            file_pointer = open(file_name,'r',encoding="latin1")
            break
        except FileNotFoundError:
            print("File is not found! Try Again!")
            file_name= input(message)
    return file_pointer
            
def read_ip_location(file):
    '''receives a file object as parameter (such as returned from open_file()) 
    and reads a range of IP addresses corresponding to a specific two-digit 
    country code. This function returns a list of 3-tuple items, 
    where each tuple contains (start_ip, end_ip, country_code). 
    Both start_ip and end_ip should be 12-digit integer numbers. '''
    file_csv = csv.reader(file)
    ip_data=[]
    for line in file_csv:
            # for start_ip
            #First split the ip address at periods
            ch_split= line[0].split('.')
            startip_digit=""
            start_ip=0
            for ch in ch_split:
                #add leading zeros to each number to make each of them 
                #three digits
                ch= ch.zfill(3)
                startip_digit+=ch  
            #convert to an int after the whole number has been built. 
            start_ip= int(startip_digit)
            
            # for end_ip
            ch_split= line[1].split('.')
            endip_digit=""
            end_ip=0
            for ch in ch_split:
                ch= ch.zfill(3)
                endip_digit+=ch
            end_ip= int(endip_digit)
            tup=(start_ip,end_ip,line[2])
            ip_data.append(tup)
            
    return ip_data   
        

def read_ip_attack(file):
    '''receives a file object as a parameter(such as returned from open_file())
    and reads detected IP addresses corresponding to an attack to a network.
    This function returns a list of tuples, where each tuple (ip_int,ip_str) 
    includes a 12-digit integer number representing the IP address,
    and a string of the IP address with .xxx appended to the end of the 
    IP address. 
    '''
    
    attack_data=[]

    for line in file:
             #a string of the IP address with .xxx appended
            line=line.strip()
            ch =line+'.xxx'
            ip_str = ch
            
            ipint=""
            charc=line.split('.')
            # a 12-digit integer number representing the IP address
            for ch in charc:
                ch=str(ch.zfill(3))
                ipint+=ch
            ipint=ipint+'000'
            ipint=int(ipint)
            tup= (ipint,ip_str)
            attack_data.append(tup)
    return attack_data
    
    
def read_country_name(file):
    '''receives a file object as parameter and reads the country code and
    its corresponding full name. This function returns a list of 2-tuples, 
    where each tuple contains (country_code, full name). '''
    full_code=[]
    for line in file:
       line=line.strip()
       line= line.split(';')
       full_name=line[0]
       country_code= line[1]
       full_code.append((country_code,full_name))
    return full_code
 
    

def locate_address(ip_list, ip_attack):
    '''This function searches for the IP address of one attack 
    (ip_attack, an int) in the list of IP addresses (ip_list).
    If the IP attack address is found in the list, 
    return the country code (string). 
    '''
    # the ip_list is the list of tuples returned by the 
    # read_ip_location() function
    for line in ip_list:
        start=line[0]
        end=line[1]
        countrycode=line[2]
        # An IP attack address is found, if all the numbers from the address 
        #are between the start address and end address.
        if start<= ip_attack <=end:
            return countrycode
     
    
    
def get_country_name(country_list, code):
    '''This function searches for a country_code (string) in the list of 
    countries (country_list) and return the name corresponding to the code 
    (string). '''
    #country_list is the list of tuples returned by the read_country_name().
    for line in country_list:
        cod=line[0]
        full=line[1]
        if code == cod:
            return full

def bar_plot(count_list, countries):
    '''use top 10 countries' list and their count list to  make a plot'''
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():
    '''The main function calls the three functions to read the files, 
    each returning a list. Then the program loops to determine the countries 
    that attacks came from. Next the program determines the top ten countries 
    with respect to the number of attacks. 
   The best way to handle this is to 
   '''
    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file)
    
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)
    # mirmir format
    print()
    
    # dispaly all attack data if answer yes
    ans= input("Do you want to display all data? ")
    if ans.lower()=='yes':
        countertup=[]
        codetup=[]
        for line in attack_data:
            x= line[1]
            ccode= locate_address(ip_data, line[0])
            y= get_country_name(country_data, ccode)
            print("{:<s}{:<19s}{:<6s}{:<s}".format("The IP Address: ",x,\
                  "originated from ",y))
   
   #create a list of tuples with two items in 
   # each tuple: the country code and the attack count for that country.          
    countertup=[]          
    codetup=[]
    for line in attack_data:
        # get countrycode
        countrycode= locate_address(ip_data, line[0])
                
        if countrycode in codetup:
            a=codetup.index(countrycode)
            countertup[a]+=1   
        else: 
            codetup.append(countrycode)
            countertup.append(1)
              
    tup= []
    for i in range(len(codetup)):
        tup.append( (codetup[i],countertup[i]))
    # If two countries have the same number of attacks, 
    # the countries will be listed in reverse alphabetical order
    new_lst = sorted(tup,key= itemgetter(1,0), reverse = True)
    # get top 10
    top10 = new_lst[:10]
    
    # print top 10 countries in mirmir formatting
    print()   
    print("Top 10 Attack Countries")
    print("Country  Count")
    for ch in top10:
        countrycode= ch[0]
        count= ch[1]
        print("{:<s} {:>11d}".format(countrycode, count))
    
    # make a dictionary with top10 countries to get country list and 
    # counter list to get a bar plot
    top10_dic= dict(top10)
    key_lis=[]
    value_lis=[]
    for key, value in top10_dic.items():
        key_lis.append(key)
        value_lis.append(value)        
    answer = input("\nDo you want to plot? ")
    # display bar plot
    if answer.lower()=='yes':
        bar_plot(value_lis, key_lis)
    
if __name__ == "__main__":
    main()
    

