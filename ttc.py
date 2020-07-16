# TIC TAC TOE
#REQUIREMENTS
#board , display board , play game,check tie, flip X->0 , hamdle turns
#check win---> rows , columns , diagonals

board = ["-","-","-",           #list
         "-","-","-",
         "-","-","-"]

game_still_going=True

winner=None

current_player ="X"
def display_board():
    print(board[0] + "|" + board[1] +"|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

        if winner=="X" or winner=="O":
            print(winner+"won.")
        elif winner==None:
            print("tie")

def handle_turn(player):

    print(player + "'s turn")
    position = input("chose a position from  0->8 ")

    if position > 9 and position < 1:
        position = input("invalid input ")

    position = int(position) - 1
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #chck rows, columns , diah\gonal

    global winner #was defined outside of the f(x)

    row_winner = check_rows
    column_winner = check_columns
    diagonal_winner= check_diagonals

    if row_winner:
        #victory
        winner = row_winner()
    elif column_winner:
        #victoy
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1= board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:     #flaggging a victory
        game_still_going=False
    if row_1:               #returning winnerrr
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:  # flaggging a victory
        game_still_going = False
    if column_1:  # returning winnerrr
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2 :  # flaggging a victory
        game_still_going = False
    if diagonal_1:  # returning winnerrr
        return board[0]
    if diagonal_2:
        return board[3]

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
        return

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

    return

play_game()