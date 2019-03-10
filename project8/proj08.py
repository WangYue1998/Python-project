###############################################################################
# Computer Project #8
# extract all the hurricanes that occurred in a year 
# print the peak wind speed of each hurricane with their coordinates and dates,
# plot the trajectory of each hurricane, 
# and plot a line chart with the peak wind speeds 
# and show the category each hurricane reached
# use open_file() to read a file
# use update_dictionary(dictionary, year, hurricane_name, data) to return a 
#   a dictionary with year as the key and whose value is another dictionary. 
#    The nested dictionary will have the name of the hurricane as its key 
#    and a list of tuples as the value.
# use create_dictionary(fp) to creates the dictionary 
#    containing the hurricane records
# use display_table(dictionary, year) to display table
# use get_years(dictionary) to return the oldest year and most recent year
# use prepare_plot(dictionary, year) to return the three lists in a tuple: 
#    (names,coordinates,max_speed)
# use plot_map(year, size, names, coordinates) to plot hurricanes 
#     for the specified year
# use plot_wind_chart(year,size,names,max_speed) to plot wind speed chart 
#    for each hurricane name
# use main() to call the previous functions to get result
###############################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as py
from operator import itemgetter

def open_file():
    '''prompts the user to enter a filename containing the hurricane data. 
    The program will try to open a file. 
    An error message should be shown if the file cannot be opened. 
    This function will loop until it receives proper input 
    and successfully opens the file. It returns a file pointer.'''
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
    '''receives the dictionary, the year, the name of the hurricane, 
    and the tuple (data) with the coordinates, date, wind speed, and pressure.
    The updated dictionary is returned. 
    a dictionary with year as the key and whose value is another dictionary. 
    The nested dictionary will have the name of the hurricane as its key 
    and a list of tuples as the value.'''
    # If the dictionary[year] is not defined, 
    # assign an empty dictionary to this entry
    if year not in dictionary:
        dictionary[year]={}
        if hurricane_name not in dictionary[year]:
            dictionary[year][hurricane_name]=[]
            dictionary[year][hurricane_name].append(data)
        else:
            dictionary[year][hurricane_name].append(data)
    #If the dictionary[year] is defined, append dictionary
    else:
        if hurricane_name not in dictionary[year]:
            dictionary[year][hurricane_name]=[]
            dictionary[year][hurricane_name].append(data)

        else:
            dictionary[year][hurricane_name].append(data)
 
    
def create_dictionary(fp):
    '''takes one parameter fp, the file pointer, reads the file, 
    and creates the dictionary containing the hurricane records. 
    All the work of updating the dictionary is done 
    in the update_dictionary function.'''
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
        datatup = (lat, lon, date, wind, pressure)
        #call the update_dictionary function to add the tuple to the dictionary
        update_dictionary(datadic, year, hurricane_name, datatup)
    return datadic


def display_table(dictionary, year):
    '''This function receives a dictionary and a year value 
    for every hurricane in that year it displays the name of the hurricane,
    the coordinate, date, and value where the hurricane reached the peak wind 
    speed. If two data points have the same peak wind speed, 
    print the one with the larger lat value. '''
    # list of name
    sorted_keys = sorted(dictionary[year].keys())
    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + year))
    print("{:15s}{:>15s}{:>20s}{:>15s}".format("Name","Coordinates",\
          "Wind Speed (knots)","Date"))
    for hur_name in sorted_keys:
        # sort all record for each hurrican
        new_lst = sorted(dictionary[year][hur_name],key= itemgetter(3,0,1))#, \
                         #reverse = True)
        lat= new_lst[-1][0]
        lon= new_lst[-1][1]
        date= new_lst[-1][2]
        wind= new_lst[-1][3]
        coord = "( {:2.2f},{:2.2f})".format(lat, lon)
        print("{:15s}{:>15s}{:>20.2f}{:>15s}".format(hur_name, coord,wind,date))
   

def get_years(dictionary):
    '''Returns the oldest year and most recent year (min and max year) 
    in the dictionary. Return a tuple (min_year, max_year).'''
    sorted_keys = sorted(dictionary.keys())
    min_year = sorted_keys[0]
    max_year = sorted_keys[-1]
    tup = (min_year, max_year)
    return tup
    
    
def prepare_plot(dictionary, year):
    '''This function should create the following lists. 
    Each list should be ordered by hurricane name, 
    (1) names : a sorted list of all the names of the hurricanes 
    in that year—sorted alphabetically, 
    (2) max_speed : a list of maximum speeds of all the hurricanes. 
    (3) coordinates: a list of coordinate paths (list of lists) 
    for the trajectory of the hurricanes.
    Each hurricane path is a list of tuples that hold a (latitude, longitude). 
    Finally return the three lists in a tuple: (names,coordinates,max_speed).
'''
    # create everything that is required for plotting
    #return names, coordinates, max_speed
    names = sorted(dictionary[year].keys())
    max_speed = []
    # List containing all the tuples of coordinates each hurricane has
    coordinates = [] 
    for hur_name in names:
        new_lst = sorted(dictionary[year][hur_name],key= itemgetter(3), \
                         reverse = True)
        max_speed.append(new_lst[0][3])
        hurricane_path = [] 
        for item in new_lst:
            # All the coordinates of a single hurricane
            hurricane_path.append((item[0], item[1]))
        # The master list contains all the coordinates of a single hurricane. 
        coordinates.append(hurricane_path)
    return (names,coordinates,max_speed)
    
    
def plot_map(year, size, names, coordinates):
    '''plot hurricanes for the specified year'''
    
    # The the RGB list of the background image
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    # Set the corners of the map to cover the Atlantic Region
    xshift = (50,190) 
    yshift = (90,30)
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude+xshift[0],max_longitude-xshift[1]))
    py.ylim((-max_latitude+yshift[0],max_latitude-yshift[1]))
	
    # Generate the colormap and select the colors for each hurricane
    cmap = py.get_cmap('gnuplot')
    colors = [cmap(i/size) for i in range(size)]
    
    
    # plot each hurricane's trajectory
    for i,key in enumerate(names):
        lat = [ lat for lat,lon in coordinates[i] ]
        lon = [ lon for lat,lon in coordinates[i] ]
        py.plot(lon,lat,color=colors[i],label=key)
    

     # Set the legend at the bottom of the plot
    py.legend(bbox_to_anchor=(0.,-0.5,1.,0.102),loc=0, ncol=3,mode='expand',\
              borderaxespad=0., fontsize=10)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Hurricane Trayectories for {}".format(year))
    py.show() # show the full map


def plot_wind_chart(year,size,names,max_speed):
    '''plot wind speed chart for each hurricane name'''
    
    # Set the value of the category
    cat_limit = [ [v for i in range(size)] for v in [64,83,96,113,137] ]
    
    
    # Colors for the category plots
    COLORS = ["g","b","y","m","r"]
    
    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size),cat_limit[i],COLORS[i],label="category-{:d}".format(i+1))
        
    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.),loc=2,\
              borderaxespad=0., fontsize=10)
    
    py.xticks(range(size),names,rotation='vertical') # Set the x-axis to be the names
    py.ylim(0,180) # Set the limit of the wind speed
    
    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size),max_speed) # plot the wind speed plot
    py.show() # Show the plot
    

def main():
    '''The main function call the previous functions to get result'''
    
    filepointer = open_file()
    dicti = create_dictionary(filepointer)
    print("Hurricane Record Software")
    yearstup= get_years(dicti)
    min_year= yearstup[0]
    max_year= yearstup[1]
    print("Records from {:4s} to {:4s}".format(min_year, max_year))
    while True:
        answer= input("Enter the year to show hurricane data or 'quit': ")
        if min_year <= answer <=max_year:
            display_table(dicti, answer)
            ans= input("\nDo you want to plot? ")
            if ans.lower()== 'yes':
                names, coordinates, max_speed = prepare_plot(dicti, answer)
                size= len(names)
                plot_map(answer, size, names, coordinates)
                plot_wind_chart(answer, size, names, max_speed)
        elif answer.lower()=='quit':
            break
        else:
            print("Error with the year key! Try another year")
    
       
if __name__ == "__main__":
     main()

