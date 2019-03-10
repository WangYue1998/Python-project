###############################################################################
#  Computer Project #5
#  prompt the user for one filename
#  identify which ads for what products are performing best, 
#  and identify, for each product, the ad that gives the best ROI
#  use function open_file() to open file
#  use function revenue(num_sales, sale_price) to return revenue
#  use function cost_of_goods_sold(num_ads, ad_price, num_sales, 
#      production_cost) to return cost of goods sold
#  use calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
#      to return ROI
#  use main function to print each product's best selling ad sales number, 
#      and best ROI
###############################################################################

# Check for filename errors and keep prompting until a file is found.
def open_file():
    '''prompt for file name, open file, return file pointer'''
    filename = input("Input a file name: ")
    while True:
        try:
            # executed if no error
            file_pointer = open(filename, 'r') 
            break
        # Use try-except and FileNotFoundError.
        except FileNotFoundError:
            # executed on file open error
            print("Unable to open file. Please try again.")  
            # ask again
            filename = input("Input a file name: ")  
    return file_pointer
    
#Returns a floting point value that is the revenue.    
def revenue(num_sales, sale_price):
    '''revenue = sales * price'''
    rev= int(num_sales) * float(sale_price)
    return rev
        
#Returns a floating point value that is the cost of goods sold.
def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    advertising_total= int(num_ads) * float(ad_price)
    production_total = int(num_sales) * float(production_cost)
    cgs = advertising_total + production_total
    return cgs

#Returns a floating point number that is the return on investment (ROI).
def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    rev= revenue(num_sales, sale_price)
    cgs = cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost)
    ROI= ((rev-cgs)/cgs)
    return ROI

def main():
    ''' Process the data file and produce output.
    Read each line, keeping a running tally of the highest sales count 
    for the product, as well as a running tally of the best ROI found so far
    For each product, output the product name, the ad with the best sales count
    and count (int), and the ad with the best ROI and the ROI as a percent 
    (float to 2 decimal places).
    If the next line is for a different product, reset the running tallies for 
    best ROI and highest sales count.'''
    # read the file
    file_pointer = open_file() 
    # Some print lines to match formatting in Mimir tests
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print() 
    # initialize value 
    ROI_highest = 0
    name=""
    count =0
    Performing_Ad_sales =""
    Performing_Ad_ROI=""
    sales = 0
    # extract the data 
    for line_string in file_pointer:
        num_sales = line_string[70:78].strip()
        sale_price= line_string[78:86].strip()
        num_ads = line_string[54:62].strip()
        ad_price = line_string[62:70].strip()
        production_cost = line_string[86:94].strip()
        Performing_Ad = line_string[27:54].strip()
        product_name= line_string[0:27].strip() 
        
        # If the next line is for a different product, reset the running 
        # tallies for best ROI and highest sales count.
        if count!=0 and name != product_name:
        #print previous product's best selling ad sales number, and best ROI
            print(name)
            print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
            print("  {:27s}{:>11d}".format(Performing_Ad_sales,sales))
            print()
            print("  {:27s}{:>11s}".format("Best ROI","percent"))
            print("  {:27s}{:>11.2f}%".format(Performing_Ad_ROI,ROI_highest))
            print()
            ROI_highest = 0
            name=""
            count =0
            Performing_Ad_sales =""
            Performing_Ad_ROI=""
            sales = 0
        
        #Read first line for a new product, keeping a running tally of the 
        #highest sales count for the product, and best ROI found so far.
        if count == 0:
             name = product_name
             count+=1
        ROI = calculate_ROI(num_ads, ad_price, num_sales, sale_price, \
                            production_cost)
        # find the best ROI
        if ROI_highest < ROI:
            ROI_highest = ROI
            Performing_Ad_ROI = Performing_Ad
        # find the best sales
        if sales < int(num_sales):
                 sales = int(num_sales)
                 Performing_Ad_sales = Performing_Ad
    
    # if the file only has one line            
    # print product's best selling ad sales number, and best ROI 
    print(name)
    print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
    print("  {:27s}{:>11d}".format(Performing_Ad_sales,sales))
    print()
    print("  {:27s}{:>11s}".format("Best ROI","percent"))
    print("  {:27s}{:>11.2f}%".format(Performing_Ad_ROI,ROI_highest))
    print()
    file_pointer.close()

if __name__ == "__main__":
     main()   
