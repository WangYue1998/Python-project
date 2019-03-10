###############################################################################
#  Computer Project #4
#  Implement FSM to recognize whether a given string conforms to the specific
#  pattern or not
#  3 functions in the skeleton :
#   (1)Prompts for a character and returns it if it’s an empty string or a
#      single character. Prints an error message and re-prompts if the input
#      length is more than 1
#   (2)Take two parameters: current state and input character. Then find the
#      next state
#   (3)Calls the other two functions in a loop and keeps track of the entered
#      character and the state. Prints the results when the returned value of
#      get_char is empty string. And print whether it's laughing or not
###############################################################################


# first function
def get_ch():
    # prompt for the input in a loop
    ch = input("Enter a character or press the Return key to finish: ")
    # if input is not empty string or a single character
    while len(ch)>1:
    # in case of invalid input, print the following error message
        print("Invalid input, please try again.")
        # continue asking input
        ch = input("Enter a character or press the Return key to finish: ")
    # return the ch at the end
    return ch

# second function
def find_state(state, ch):
    # if current state = 1, only input charcater which is 'h' can go to state 2
    if state == 1:
        if ch == 'h':
            state = 2
        # all other characters go to state 5
        else:
            state = 5


    # if current state = 2, only input charcater which is 'a' or 'o'
    # can go to state 2
    elif state == 2:
        if ch == 'a' or 'o':
            state= 3
        # all other characters go to state 5
        else:
            state = 5
            

    # if current state = 3
    elif state == 3:
        # if input is "h", go to state 2
        if ch=='h':
            state = 2
        # if input is "!', go to state 4
        elif ch == '!':
            state = 4
        # all other characters go to state 5
        else:
            state = 5

    # if state == 4, only input is "", success
    elif state == 4:
        state = 5

    # if state is 5, failure
    elif state == 5:
        state = 5
        
    return state

# third function
def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    # initialize the variables
    string = "" 

    # call the functions in a loop
    state = 1
    ch = get_ch()
    while ch != "":
        state = find_state(state, ch)
        string+=ch
        ch = get_ch()
        

    # when user enters an empty string, print the results
    print("\nYou entered", string)
    if state == 4:
        print("You are laughing.")
    # if failure
    elif ch =="" or state == 5:
        print("You are not laughing.")
 
main()
