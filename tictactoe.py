import math
import copy

#Me:
rows, cols = (3, 3)
board = [[0]*cols]*rows
#-----------------------------------


#______________________________________________________________________________________________________________________________________#


# 1. Initial State: 
# Every tic-tac-toe game starts with an empty 3x3 matrix.

X = "X"
O = "O"
EMPTY = None
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


#______________________________________________________________________________________________________________________________________#

# 2. Count:
# This will help to keep track of which player to move next. Returns the number of X and O on the board.

def count(board):
    count_x, count_o = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    return count_x, count_o

#______________________________________________________________________________________________________________________________________#

# 3. Player:
# Track the moves. Returns player who has the next turn on board.


def player(board):
    count_x, count_o = count(board)
    if count_o + count_x == 0:
        return X
    elif count_x > count_o and count_x + count_o != 9:
        return O
    elif count_x == count_o and count_x + count_o != 9:
        return X
    elif count_x + count_o == 9:
        return X

#______________________________________________________________________________________________________________________________________#

# 4. Actions:
# In each state, returns the set of all possible actions (i, j) available on the board.

def actions(board):
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append((i, j))
    return action