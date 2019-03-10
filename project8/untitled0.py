#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def open_file():
    '''Remember to put a docstring here'''
    filename= input("Input a file name: ")
    while True:
        try:
            fp = open(filename,'r')
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            filename = input("Input a file name: ")
    return fp


def update_dictionary(dictionary, year, hurricane_name, data):
    '''Remember to put a docstring here'''
    if year not in dictionary:
        dictionary[year]={}
        if hurricane_name not in dictionary[year]:
            dictionary[year][hurricane_name]=[]
            dictionary[year][hurricane_name].append(data)
        else:
            dictionary[year][hurricane_name].append(data)
    else:
        if hurricane_name not in dictionary[year]:
            dictionary[year][hurricane_name]=[]
            dictionary[year][hurricane_name].append(data)

        else:
            dictionary[year][hurricane_name].append(data)
        
    return dictionary
        
    
    
    
def create_dictionary(fp):
    '''Remember to put a docstring here'''
    datadic={}
    for line in fp:
        line=line.split()
        datatup=()
        year = line[0]
        hurricane_name = line[1]
        lat = float(line[3])
        lon = float(line[4])
        date = line[5]
        #if the value is a number, 0 otherwise
        try:
            wind = float(line[6])
        except:
            wind=0
        try:
            pressure = float(line[7])
        except:
            pressure= 0
        datatup=(lat, lon, date, wind, pressure)
        datadic= update_dictionary(datadic, year, hurricane_name, datatup)
    return datadic
def display_table(dictionary, year):
    '''Remember to put a docstring here'''
    #x is the peak wind speed index in the tuple
    #y is the latitude index in the tuple
    #sorted_list = sorted(data, key = itemgetter(x,y), reverse = True)
    #tup=[]
    sorted_keys = sorted(dictionary[year].keys())
    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + year))
    print("{:15s}{:>15s}{:>20s}{:>15s}".format("Name","Coordinates","Wind Speed (knots)","Date"))
    for hur_name in sorted_keys:
#        name= key
#        tup.append(value)
        new_lst = sorted(dictionary[year][hur_name],key= itemgetter(3,0), reverse = True)
        lat= new_lst[0][0]
        lat= round(lat,2)
        lon= new_lst[0][1]
        lon=round(lon,2)
        #coord=(lat, lon)
        date= new_lst[0][2]
        wind= new_lst[0][3]
        coord = "( "+ str(lat) + ", " + str(lon) + ")"
        print("{:15s}{:>15s}{:>20f}{:>15s}".format(hur_name, coord,wind,date))
   
fp= open_file()
d=create_dictionary(fp)
year= input(":")
e=display_table(d, year)
print(e)
