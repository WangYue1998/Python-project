###############################################################################
# Computer Project #6
# prompt the user for one filename
# keep track of water usage in the United States across different areas in file
# read file on State, Population, County, Public, Domestic, Industrial, 
# Irrigation of crops, and Livestock
# use extract function to return one state's water usage
# use compute usage function to compute water usage in the county for one state
# use display_data function to display information for each county 
# use plot_water_usage to create a pie chart
# use main function to call the previous function and get results
###############################################################################
import pylab

STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', \
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',\
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', \
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', \
          'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]

# open a file
def open_file():
    '''prompts the user to enter a filename. 
    The program will try to open a csv file. 
    An error message will be shown if the file cannot be opened. 
    This function will loop until it receives proper input 
    and successfully opens the file. 
    It returns a file pointer.'''
    filename = input("Input a file name: ")
    while True:
        try:
            file_pointer = open(filename,'r')
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            filename = input("Input a file name: ")
    return file_pointer
        
# reading each line from file except first line    
def read_file(fp): 
    '''receives a file pointer of the data file. 
    return a list of tuples for one state's data'''
    data_list=[]
    fp.readline()
    for line in fp:
        line= line.split(',')
        state = line[0].strip().upper()
        county = line[2]
        #Convert population which is in thousand to its actual value. 
        population = float(line[6])*1000
        #Convert number strings to float.
        fresh_water = float(line[114])
        salt_water = float(line[115])
        public = float(line[18])
        domestic = float(line[26])
        #If a value is missing, use 0 as the value.
        if line[35] != "":
            industrial = float(line[35])  
        else:
            industrial= 0
        if line[45] != "":
            irrigation= float(line[45]) 
        else:
            irrigation= 0
        if line[59] != "":
            livestock = float(line[59]) 
        else:
            livestock= 0 
        # This function returns a list of tuples:
        tup = (state, county, population, fresh_water, salt_water,public, \
              domestic, industrial, irrigation, livestock)
        data_list.append(tup)
    return data_list
    
        
# get a specific state's data    
def extract_data(data_list, state):
    '''Receives, data_list, 
    a list of tuples containing all the U.S water data usage and 
    state, a string containing the name of a state. 
    This function returns a list of tuples containing all water data from state
    If the state is not found in data_list , return an empty list.'''
    statename_list=[]
    for line in data_list:
        if state == line[0]:
            statename_list.append(line) 
    return statename_list


# compute the water usage for each county in a specific state    
def compute_usage(state_list):
    '''this function receives state_list, 
    the list of water usage for a specific state. 
    For each county in state_list compute the total water used (salt and fresh) 
    and compute the fresh water usage per person in the county. 
    The function returns a list of tuples, one tuple for each county 
    in state_list.'''
    lst = []
    for line in state_list:
        county = line[1]
        population = line[2]
        fresh_water = line[3]
        salt_water = line[4]
        total_water= fresh_water+salt_water
        per_person_water= fresh_water/population  
        # Put above values in a tuple:
        tup_county = (county, population, total_water, per_person_water)
        lst.append(tup_county)
    return lst
   
     
#display a table    
def display_data(state_list, state):
    '''This function displays the following information for each county 
    in the state_list: county name, population, total water usage per person, 
    total water used by the county. 
    use string formatting to properly display the table.'''
# Some strings useful for Mimir testing
    title = "{:^88s}".format("Water Usage in " + state + " for 2010")
    header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
    "Population", "Total (Mgal/day)", "Per Person (Mgal/person)")
    print(title)
    print(header)
    #Call the compute_usage function to get values. 
    tuple_county = compute_usage(state_list)
    for line in tuple_county:
        county= line[0]
        population= line[1]
        total= line[2]
        per_person = line[3]
        print("{:22s} {:>22,.0f} {:>22.2f} {:>22.4f}".format(county, \
    population, total, per_person ))
 
    
# display plot
def plot_water_usage(some_list, plt_title):
    '''
        Creates a list "y" containing the water usage in Mgal/d of all counties.
        Y should have a length of 5. The list "y" is used to create a pie chart
        displaying the water distribution of the five groups.
        This function is provided by the project.
    '''
    # accumulate public, domestic, industrial, irrigation, and livestock data
    y =[ 0,0,0,0,0 ]

    for item in some_list:

        y[0] += item[5]
        y[1] += item[6]
        y[2] += item[7]
        y[3] += item[8]
        y[4] += item[9]

    total = sum(y)
    y = [round(x/total * 100,2) for x in y] # computes the percentages.

    color_list = ['b','g','r','c','m']
    pylab.title(plt_title)
    pylab.pie(y,labels=USERS,colors=color_list)
    pylab.show()
    pylab.savefig("plot.png")  # uncomment to save plot to a file

    
def main():
    '''call the previous function to get final results'''
# Some strings to help with Mimir testing
    print("Water Usage Data from the US and its States and Territories.\n")
    file= open_file()
    data_list= read_file(file)
    while True:
            state_name = input("\nEnter state code or 'all' or 'quit': ")
            if state_name.upper() in STATES:
                data_state= extract_data(data_list, state_name.upper())
                display_data(data_state, state_name.upper())
                answer = input("\nDo you want to plot? ")
                if answer.lower() == "yes":
                    title= "Water usage in "+state_name+" for 2010(Mgl/day)"
                    plot_water_usage(data_state, title)
            elif state_name== "all":
                    display_data(data_list, state_name.upper() )
                    answer = input("\nDo you want to plot? ")
                    if answer.lower() == "yes":
                        title= "Water usage in "+state_name+" for 2010 (Mgl/day)"
                        plot_water_usage(data_state, title)
            elif state_name == "quit":
                break
            else:
                print("Error in state code.  Please try again.")
             
    file.close()
    

if __name__ == "__main__":
    main()

