###############################################################################
# Computer Project #11
# implement a game called Gomoku in Python using classes.
# The black plays first if white did not win in the previous game, 
#   and players alternate in placing a stone of their color on an empty 
#   intersection. 
# The winner is the first player to get an unbroken row of five stones 
#   horizontally, vertically, or diagonally. 
###############################################################################

class GoPiece(object):
    ''' It represents black or white pieces used in the game.'''
    def __init__(self,color='black'):
        ''' this method creates a Gomoku piece. 
        It has an attribute named ‘color’ which is either 'black'or 'white'. 
        The attribute must be private. 
        Raise MyError('Wrong color.') for a color that is not black or white. 
        Set the default value to 'black' '''  
        self.__color = color
        if  self.__color != 'black' and  self.__color != 'white':
            raise MyError("Wrong color.")
       
    def __str__(self):
        ''' this method displays the black piece as ‘ ● ’, 
        and white piece as ‘○’ .'''
        if self.__color == 'black':
            return ' ● ' 
        elif self.__color == 'white':
            return ' ○ '
        
    def get_color(self):
        ''' this method returns the color of the piece as a string 
        'black'or 'white'.'''
        return str(self.__color)
    
       
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value



class Gomoku(object):
    ''' It contains methods for setting up the game, displaying the game board,
    and playing the game. '''
    def __init__(self,board_size = 15,win_count=5,current_player= 'black'):
        '''with four attributes, three have defaults, all must be private.'''
        
        #i. board_size : the size of the game board, which by default is 15 
        #(representing a 15x15 board). Check that the value is an int 
        #so it will raise a ValueError if not.
        self.__board_size = board_size
        if type(self.__board_size)!= int:
            raise ValueError
            
        #ii. win_count : the number of pieces in an unbroken row that a player
        #must get to win, which by default is 5. Check that the value is an int 
        #so it will raise a ValueError if not.
        self.__win_count = win_count
        if type(self.__win_count)!= int:
            raise ValueError
        
        #iii.current_player : the color of the current player. 
        #Default is 'black'. Raise MyError('Wrong color.') for color that
        #is not black or white.
        self.__current_player= current_player
        if self.__current_player != 'black' and self.__current_player != 'white':
            raise MyError('Wrong color.')   
            
        #iv.go_board: a list of lists to represent the game board. 
        #Specifically, it is a list of row-lists.
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] \
                             for i in range(self.__board_size)]
             
            
    def assign_piece(self,piece,row,col):
        ''' it places the piece (a GoPiece object) at the specified position 
        on the game board. Row 1 is the top row, column 1 is the left-most 
        column. Raise MyError('Invalid position.') if the specified row or 
        column is too big or too small to be on the game board. 
        Raise MyError('Position is occupied.') if the space is already 
        occupied by a piece.'''
        if row > self.__board_size or col > self.__board_size or \
                row < 1 or col < 1:
            raise MyError('Invalid position.') 
    
        if self.__go_board[row-1][col-1] != ' - ':
            raise MyError('Position is occupied.')
        self.__go_board[row-1][col-1]= piece

    def get_current_player(self):
        ''' it returns the current player as a string 'black'or 'white'.'''
        if self.__current_player == 'black':
            return 'black'
        elif self.__current_player == 'white':
            return 'white'
        
    
    def switch_current_player(self):
        '''  it returns the ‘other’ player as a string, that is, 
        if the current_player is 'white'it returns the string 'black'
        otherwise it returns 'white'.'''
        if self.__current_player == 'black':
            self.__current_player = 'white'
        elif self.__current_player == 'white':
            self.__current_player = 'black'
            
        
    def __str__(self):
        '''returns a string that represents the board for printing. '''
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
        
    def current_player_is_winner(self):
        ''' This method returns True when current_player is a winner, 
        otherwise False. It will check all rows and columns to check 
        if there is an unbroken sequence of size win_count 
        (default is five-in-a-row). '''
        # self.__board_size - self.__win_count+2=11
        
        # horizontal
        for row in range(1, self.__board_size+1): 
            k=[0,1,2,3,4]
            for col in range(1, self.__board_size - self.__win_count+2):
                if type(self.__go_board[row-1][col-1])== GoPiece:
                    piece= str(GoPiece(self.__current_player))
                    if str(self.__go_board[row-1][col-1]) == piece:
                        count = 0
                        for i in range(len(k)):
                            if str(self.__go_board[row -1][col -1 + k[i]]) == piece:
                                count+=1
                                if count== self.__win_count:
                                    return True 
        # vertical
        for col in range(1, self.__board_size+1): 
                k=[0,1,2,3,4]
                for row in range(1, self.__board_size - self.__win_count+2):
                    if type(self.__go_board[row-1][col-1])== GoPiece:
                        piece= str(GoPiece(self.__current_player))
                        if str(self.__go_board[row-1][col-1]) == piece:
                            count = 0
                            for i in range(len(k)):
                                if str(self.__go_board[row-1 +k[i]][col-1]) == piece:
                                    count+=1
                                    if count== self.__win_count:
                                        return True 
                            
        # diagonals (row+k, col+k)        stopping point both 11  
        for row in range(1, self.__board_size - self.__win_count+2):
            k=[0,1,2,3,4]
            for col in range(1, self.__board_size - self.__win_count+2):
                if type(self.__go_board[row-1][col-1])== GoPiece:
                    piece= str(GoPiece(self.__current_player))
                    if str(self.__go_board[row-1][col-1]) == piece:
                        count = 0
                        for i in range(len(k)):
                                if str(self.__go_board[row-1+k[i]][col-1+k[i]]) == piece:
                                    count+=1
                                    if count== self.__win_count:
                                        return True 
            
        # diagonals (row+k, col-k)                
        for row in range(1, self.__board_size - self.__win_count+2):
            k=[0,1,2,3,4]
            for col in range(self.__win_count-1, self.__board_size+1):
                if type(self.__go_board[row-1][col-1])== GoPiece:
                    piece= str(GoPiece(self.__current_player))
                    if str(self.__go_board[row-1][col-1]) == piece:
                        count = 0
                        for i in range(len(k)):
                                if str(self.__go_board[row-1+k[i]][col-1-k[i]]) == piece:
                                    count+=1
                                    if count== self.__win_count:
                                        return True 
                      
    
        return False
        
    
                

             
def main():
    '''it creates an instance of the class Gomoku, It will alternatively let 
    the black and white players place their piece on the game board, 
    until there is a winner, or until a player inputs ‘q’ to quit. 
    Each time a player places a piece on the game board, this function will 
    check whether a winner is generated using the method 
    current_player_is_winner, and display the current game board.
    check the row and column are ints. If anywhere in the 
    program a ValueError is raised, catch it in the main'''
    
    
    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        try:
            if len(play_list)!= 2:
                raise MyError("Incorrect input.")
            for ch in play_list:
                try:
                    ch = int(ch)
                except ValueError:
                    raise MyError("Incorrect input.")
                    
            
            row = int(play_list[0])
            col = int(play_list[1])
            piece= GoPiece(board.get_current_player())
            board.assign_piece(piece,row,col)
            if board.current_player_is_winner():
                
                print(board)
                print("{} Wins!".format(board.get_current_player()))
                break
            board.switch_current_player()
        except ValueError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
     
        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':  
    main()
