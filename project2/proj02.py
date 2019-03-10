###############################################################################
#  Computer Project #2
#   Algorithm
#   prompt for price for an item in cents until price input is not equal to 'q'
#   prompt for payment for an item in cents 
#   when payment less than price, display error message
#   when payemnt equal to price, no change
#   if payment greater tahn price:
#      calculating the numbers of coins of each denomination to dispense 
#      display results of the coins to be dispensed as change
###############################################################################

# assume a stock of 10 nickels, 10 dimes, 10 quarters, and 10 pennies
# the number of coins in stock will change
quarters_int = 10
dimes_int = 10
nickels_int = 10
pennies_int = 10

#display welcome to change_makiing program 
print("\nWelcome to change-making program.")

#display all of the coins remaining in the stock
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters_int, dimes_int, nickels_int, pennies_int))

#prompt for price in dollars
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

# repeatedly request the price and payment for an item to be purchased if user 
# not quit
while in_str != 'q':
    
    # If the price entered is negative 
    while float(in_str)<0:
        #print an error message 
        print("Error: purchase price must be non-negative.")
        #display all of the coins remaining in the stock
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies". \
              format(quarters_int, dimes_int, nickels_int, pennies_int))
        #start over requesting either a new price or to quit
        in_str=(input("Enter the purchase price (xx.xx) or 'q' to quit: "))
    
    #Prompt for the number of dollars in payment. 
    paid_float = float(input("Input dollars paid (int): "))
    #convert string to floats
    price_float = float(in_str)
    # assignment 
    change_float = paid_float-price_float
    
    #if  payment is less than price
    while change_float<0:
        print("Error: insufficient payment.")
        #repeatedly request payment for an item
        paid_float=float(input("Input dollars paid (int): "))
        change_float=paid_float-price_float
    
    #if payment is equal to price
    if change_float==0:
        #display No change
        print("No change.")
        #display all of the coins remaining in the stock
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies". 
              format(quarters_int, dimes_int, nickels_int, pennies_int))
        #display the price
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        change_float=paid_float-price_float
        
    
    #if payment is greater than price
    if change_float>0:
        # purchase price and payment will be kept in cents
        change_cents_int=round(change_float*100)
        # the value for each coin
        QUARTERS_VALUE = 25
        DIMES_VALUE = 10
        NICKELS_VALUE = 5
        PENNIES_VALUE = 1
        
        #initialize value for number of coins  we can dispense
        quarters_needed_int = 0
        dimes_needed_int = 0
        nickels_needed_int = 0
        pennies_needed_int = 0
       
        #determine the coins to be dispensed as change
        
        # quarters in stock and we need quarters
        if quarters_int>0 and change_cents_int > QUARTERS_VALUE:
            #deterimine how many quarters we need
            quarters_needed_int= (change_cents_int//QUARTERS_VALUE)
            # if the number of quarters is greater than number of quarters \
            #in stock
            if quarters_needed_int > quarters_int:
                # the quarters to be dispended as change eauql to the number \
                # of quarters in stock
                quarters_needed_int=quarters_int
            # the cents we still need to dispense
            change_cents_int= change_cents_int - (quarters_needed_int*
                                                  QUARTERS_VALUE )
            # number of quarters left in the stock
            quarters_int-=quarters_needed_int
           
            
        # dimes in stock and we need dimes    
        if dimes_int>0 and change_cents_int > DIMES_VALUE:
            #deterimine how many dimes we need
            dimes_needed_int= (change_cents_int//DIMES_VALUE)
            # if the number of dimes is greater than number of dimes in stock
            if dimes_needed_int > dimes_int:
                # the dimes to be dispended as change eauql to the number of\
                # dimes in stock
                dimes_needed_int=dimes_int
            # the cents we still need to dispense
            change_cents_int= change_cents_int - (dimes_needed_int * \
             DIMES_VALUE )
            # number of dimes left in the stock
            dimes_int-=dimes_needed_int
         
            
        # nickels in stock and we need nickels     
        if nickels_int>0 and change_cents_int > NICKELS_VALUE:
            #deterimine how many nickels we need
            nickels_needed_int= (change_cents_int//NICKELS_VALUE) 
            #if the number of nickels is greater than number of nickels \
            #in stock
            if nickels_needed_int > nickels_int:
                # the nickels to be dispended as change eauql to the number \
                # of nickels in stock
                nickels_needed_int=nickels_int
            # the cents we still need to dispense
            change_cents_int = change_cents_int - (nickels_needed_int * \
            NICKELS_VALUE )
            # number of nickels left in the stock
            nickels_int-=nickels_needed_int
            
        
        # pennies in stock and we need pennies
        if pennies_int>0 and change_cents_int > PENNIES_VALUE:
            #deterimine how many pennies we need
            pennies_needed_int= change_cents_int
            # if the number of pennies is greater than number of pennies \
            # in stock
            if pennies_needed_int > pennies_int:
                # the pennies to be dispended as change eauql to the number \
                # of pennies in stock
                pennies_needed_int=pennies_int
            # the cents we still need to dispense
            change_cents_int -= pennies_needed_int
            # number of pennies left in the stock
            pennies_int-=pennies_needed_int
            
    # when out of stock, the change cannot be made up with the coins remaining
        if quarters_int <=0 and dimes_int<=0 and nickels_int<=0 \
and pennies_int<=0:
            #dispaly an error message 
            print("Error: ran out of coins.")
            break
        
        #display the numbers of the coins to be dispensed as change and \
        #their denominations 
        else:
            print()
            print("Collect change below: ")
       #Omit a denomination if no coins of that denomination will be dispensed
            if quarters_needed_int != 0 :
                print("Quarters:", quarters_needed_int) 
            if dimes_needed_int != 0 :
                print("Dimes:", dimes_needed_int)
            if nickels_needed_int != 0:
                print("Nickels:", nickels_needed_int)
            if pennies_needed_int != 0 :
                print("Pennies:", pennies_needed_int)
            
            # dispaly number of coins left in the stock
            print("\nStock: {} quarters, {} dimes, {} nickels, \
     and {} pennies".format(quarters_int, dimes_int, nickels_int, pennies_int))
    
            #repeatedly request the price for an item or quit
            in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")