###############################################################################
# Computer Project #10
# allow the user to play Nine Men’s Morris according to the rules outlined 
# The program will use the instructor supplied NMM.py module to model the board 
#   and assist with adjacency and mills. 
# The program will repeatedly display the current state of the game 
# prompt the user to enter a command, alternating players 
# until someone wins the game or enters q, whichever comes first.
# The program will detect, report, and recover from invalid commands. 
###############################################################################

import NMM #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""


MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
        
def count_mills(board, player):
    """
        count_mills takes in the current state of the board and one player, 
        counts how many of the mills are held by the player, 
        and returns the count. This can be used to determine if a player 
        has formed a new mill by calling it before and after.
    """
    count=0
    for ch in board.MILLS:
        if board.points[ch[0]]==player and board.points[ch[1]]==player \
        and board.points[ch[2]]== player:
            count+=1
    return count
      

            
def place_piece_and_remove_opponents(board, player, destination):
    """
        This function is used place a piece for player and 
        if a mill is created, it removes an opponent’s piece 
        (by calling remove_piece specified below). 
        Mills created can be determined by calling count_mills before and after
        the move.
    """
    beforecount= count_mills(board, player)
    #if a placement is invalid 
    if board.points[destination] != " ":
        print("Point is in a mill")
        print("Try again.")
    elif board.points[destination] == " ":
        #If the placement is valid, it needs to place the piece at the destination 
        board.assign_piece(player,destination)
        
        aftercount= count_mills(board, player) 
        #if a new mill is created, remove an opponent’s piece 
        if aftercount > beforecount:
            #if a new mill is created, remove an opponent’s piece 
            print('A mill was formed!')
            print(board)
            player= get_other_player(player)
            remove_piece(board, player)
            
            
     
def move_piece(board, player, origin, destination):
    """
        This function is used to move a piece. 
        It takes in board, player, origin, and destination. 
        It needs to raise a RuntimeError if a movement is invalid.
        If a movement is valid, it needs to check adjacency (if necessary), 
        remove the player’s piece from the origin point, 
        and call the appropriate functions to place the piece for player 
        at the destination point and remove any opponent pieces 
        if new mills were formed (by calling place_piece_and_remove_opponents).
    """
    #  if a movement is invalid
    if board.points[origin] != player:
        raise RuntimeError ("Invalid command: Origin point does not belong to player")
        #If a movement is valid, it needs to check adjacency 
    elif board.points[origin] == player:
        if destination not in board.ADJACENCY[origin]:
            raise RuntimeError("Invalid command: Not a valid point")
        else:
            board.clear_place(origin)
            place_piece_and_remove_opponents(board, player, destination)
    


    
def points_not_in_mills(board, player):
    """
        This function will find all points belonging to player that are 
        not in mills, and return them as a set. This is used by the remove_piece 
        function.

    """
    collection_of_points = placed(board,player)
    in_mills = set()
    # Use the list “mills” in the Board class. 
    # one piece can be part of horizontal mill, 
    # but not in a complete mill that is vertical. 
    for ch in board.MILLS:
            if board.points[ch[0]] == player and board.points[ch[1]] == player\
            and board.points[ch[2]]== player:
                in_mills.add(ch[0])
                in_mills.add(ch[1])
                in_mills.add(ch[2])
    not_in_mills = collection_of_points ^ in_mills
    return not_in_mills 


def placed(board,player):
    """
        Return points where player's pieces have been placed. 
        As with the previous function, return a set.
    """
    collection_of_points=set()
    for key, value in board.points.items():
        if value == player:
            collection_of_points.add(key)
            
    return collection_of_points


    
def remove_piece(board, player):
    """
        This function will remove a piece belonging to player from board. 
        It needs to determine which points are valid to remove, 
        loop and get input until a valid piece is removed, 
        and handle the removal of the piece from the board 
        (by calling the board clear_place method in the Board class).
    """

    while True:
        point= input("Remove a piece at :> ")
        notmills_points = points_not_in_mills(board, player)
        collection_of_points = placed(board,player)
        if len(notmills_points)==0:
            if point in collection_of_points:
                 board.clear_place(point)
                 break
        elif len(notmills_points)!=0:
            if len(point)> 2:
                print("Invalid command: Not a valid point")
                print("Try again.")
            elif point not in collection_of_points:
                    print("Invalid command: Point does not belong to player")
                    print("Try again.")
            else:
                if point not in notmills_points:
                    print("Invalid command: Point is in a mill") 
                    print("Try again.")
                else:
                    board.clear_place(point)
                    break
                
                
                
           
def is_winner(board, player):
    """
        This function will be used to decide if a game was won. 
        A game has been won if the opposing player has been reduced to 
        fewer than three pieces.
    """
    count=0
    otherplayer = get_other_player(player)
    for value in board.points.values():
        if value == otherplayer:
            count+=1
    if count < 3:
        return True
    return False
        
        
   
def get_other_player(player):
    """
    Get the other player.  
    """
    return "X" if player == "O" else "O"
    
def main():
    '''show the results of two phases of game '''
    
    #Loop so that we can start over on reset
    a = False
    while not a:        
        #Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        # total of pieces placed by "X" or "O", 
        #includes pieces placed and then removed by opponent  
        placed_count = 0 
        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
       
        #Until someone quits or we place all 18 pieces...
        while command != 'q'and command != 'r' and placed_count != 18 :
            try:
                if command =='h':
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                if command != 'r':
               
                    place_piece_and_remove_opponents(board, player, command)
                    placed_count += 1
            
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            #Prompt again
            print(board)
            player= get_other_player(player)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
                
            print()
            
        #Go back to top if reset
        if command == 'r':
            continue
        
        
        # PHASE 2 of game
         
        while command != 'q':
            # commands should have two points
            command = command.split( )
            if len(command)!=2:
               print("Invalid number of points")
               print("Try again.")
               print()
               
                
            if len(command) == 2:
                try:
                    source = command[0]
                    destination = command[1]
                    
                    move_piece(board, player, source, destination)
                    winner = is_winner(board, player)
                    if winner == True:
                        print(BANNER)
                        a= True
                        break
                    
                    player= get_other_player(player)
                except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))         
            #Display and reprompt              
            print(board) 
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()            
        #If we ever quit we need to return
        if command == 'q':
            return

            
if __name__ == "__main__":
    main()
