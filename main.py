# -------- Global Variable ------ 

# Game Board
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

# If game is still going
game_still_going = True

#who won? or tie?
winner = None

#Whos turn is it 
current_player = "X"

def display_board():
    print(board[0]+ ' | ' + board[1]+ ' | ' + board[2])
    print(board[3]+ ' | ' + board[4]+ ' | ' + board[5])
    print(board[6]+ ' | ' + board[7]+ ' | ' + board[8])


#play tictactoe game
def play_game():
    display_board() ## display board 

    #while the game is still going 
    while game_still_going:

        # handle a single turn of an arbitrary Player
        handle_turn(current_player)

        #Check if the game h as ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    #The Game is over
    if winner ==  "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


# Handle a single turn of a arbitrary player
def handle_turn(player):
    print(' \'' + current_player + '\' turn.')
    position = input('choose a position from 1-9 :')
    input_filter = ['1','2','3','4','5','6','7','8','9']

    valid = False
    while not valid:
        
        while position not in input_filter:
            position = input("Invalid input . Chooose a position from 1-9 :")

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("You can't go there , Go again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #set the global variable
    global winner
    #check row 
    row_winners = check_rows()
    #check columns
    columns_winner = check_columns()
    #check diagonals
    diagonals_winner = check_diagonals()
    if row_winners:
        winner = row_winners
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

def check_rows():
    #set up the global veriable 
    global game_still_going
    #check if any of the rows have all the same value (and is not empty)
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    #if any row does have a match , flag that there is a win
    if row1 or row2 or row3:
        game_still_going = False
    #return the winner (X or O)
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3: 
        return [board[6]]
    return

def check_columns():
    #setup the Global veriable
    global game_still_going
    #check if any of the columns have all the same value and (is not empty)
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    #if any column does have a match , flag that there is a win
    if column1 or column2 or column3:
        game_still_going = False
    # Return the winner (X or O)
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[3]
    return

def check_diagonals():
    #setup the Global veriable
    global game_still_going
    #check if any of the diagonal have all the same value and (is not empty)
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    #check if diagonal has a  match , flag that there is a win
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return


def check_if_tie():
    #setup the Global veriable
    global game_still_going
    #check if there any '-' matches
    if '-' not in board:
        game_still_going = False
    return

def flip_player():
    #set global veriable
    global current_player
    #if the current_player was X then chnage it O and vice versa
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return 

#check if the want to play again this game
def play_again():
    #setup global 
    global game_still_going
    global board

    valid = True
    while valid:
        again = input("Want to play again ? Yes or No : ")
        if again == "yes":
            game_still_going = True
            board = ["-","-","-",
            "-","-","-",
            "-","-","-",]
            play_game()
        elif again == "no":
            valid = False
        else:
            valid = False
    
play_game()
play_again()
