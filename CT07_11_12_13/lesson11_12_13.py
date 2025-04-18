# **Task 1a**: Initialise board
# Create an 'initialise_board()' function that returns a 3x3 Tic
# Tac Toe board using nested lists. Each item in each of the list
# holds a space (' ').

# The 3x3 nested list visualised:
# [[' ', ' ', ' '],
#  [' ', ' ', ' '],
#  [' ', ' ', ' ']]

# 1. Create an 'initialise_board()' function that does the
#    following
# 2. Create an empty list, 'board'
# 3. Using 'for' loop to iterate 3 times,
#         a. Create an empty list, 'row'
#         b. Using 'for' loop to iterate 3 times,
#                 i. Using '.append()', add a space (' ') into
#                    the list, 'row'.
#         c. Append ('.append()') the list, 'row' into the list,
#            'board' to create a nested list.
# 5. Return 'board'

# **Test case**
# Input:
#     print(initialise_board())
# Expected output:
#     [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]




# Task 2 Pseudocode
# for row in board:
#   for cell in row:
#     if cell is NOT space:
#       print content of cell
#     else:
#       print cell_number
#     if cell_number is not a multiple of 3:
#       print "|"
#     increase cell_number by 1
#   if cell number <= 9
#     print "----------"


## Task 12.3a (get_player_move)
# Using the algorithm provided, create a 'get_player_move'
# function with 1 parameter, 'board'.

# **Algorithm**
# move = int(move_input) - 1
# row = move // 3
# col = move % 3

# When called, the function must:
# 1. Ask player for a number between 1 and 9 (stored in
#    'move_input')
# 2. Apply the above algorithm to calculate the row and column
#    number
# 3. Assign 'X' to the selected cell

# **Main game loop**
# 1. Initialise a game board
# 2. Print the game board
# 3. Ask the user for a move
board = []
def initaliseBoard():
    for i in range(3):
        row = []
        for i in range(3):
            row.append(' ')
        board.append(row)
def printBoard(board) :
    cell_number = 0
    for row in board:
        for cell in row:
            cell_number += 1
            if cell != ' ':
                print(" " + str(cell) + " ", end="")
            else:
                print(" " + str(cell_number) + " " , end="")
            if (cell_number % 3)  != 0:
                print("|" , end="")
        if cell_number < 9:
            print("\n----------")
    print("\n")
def getPlayerMove(board) :
    move =  input("where do you want to place?(1-9) ")
    if move.isdigit():
        move = int(move)
        move -= 1
        row = move //3
        col = move % 3
        if board[row][col] == " " :
            board[row][col] = "X"
        else:
            print("This spot is taken, take a different one. ")
            getPlayerMove(board)
    else:
        print("Invalid input. Please enter a number.")
        getPlayerMove(board)

initaliseBoard()
while True:
    printBoard(board)
    getPlayerMove(board)

## Task 12.3c (get_player_move)
# Modify your 'get_player_move' function to:
# 1. Check if the user's input contains only digits before
#    processing the user's input.
# 2. Else, print "Invalid input. Please enter a number."

## Task 12.3d (get_player_move)
# Modify your 'get_player_move' function to:
# 1. Also check if the user's input is more than or equal to 1
#    and less than or equal to 9
# 2. Else, print "Please enter a number between 1 and 9"

## Task 12.3e (get_player_move)
# Modify your 'get_player_move' function to:
# 1. Check if the chosen cell is empty before assigning 'X' to
#    the cell.
# 2. Else, print "That spot is already taken or invalid. Please
#    choose another."
