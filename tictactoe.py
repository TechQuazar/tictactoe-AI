"""
Tic Tac Toe Player
"""
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def isFull(board):
    """
    Returns true if board is full otherwise returns False
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count =0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]!=EMPTY:
                count=count+1
    if count%2==0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves =[]
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                pair = (i,j)
                moves.append(pair)
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    turn = player(board)
    if turn==X:
        newboard[action[0]][action[1]] = X
    else:
        newboard[action[0]][action[1]] = O
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check if player X or O wins
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]==X:
                return X
            elif board[i][0]==O:
                return O
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[0][i]==X:
                return X
            elif board[0][i]==O:
                return O
    if board[0][0] == board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]==X:
            return X
        elif board[0][0] == O:
            return O
    if board[2][0] == board[1][1] and board[1][1]==board[0][2]:
        if board[2][0]==X:
            return X
        elif board[2][0] == O:
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X or winner(board)==O or (winner(board) == None and isFull(board)):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # X maximizes, O minimizes
    user = player(board)
    maxVal=-100
    minVal=100
    optAction = (0,0)
    if(terminal(board)):
        return None
    else:
        if user==X:
            for a in actions(board):
                val = minValue(result(board,a))
                if val >= maxVal:
                    maxVal=val
                    optAction=a
        else:
            for a in actions(board):
                val = maxValue(result(board,a))
                if val<=minVal:
                    minVal=val
                    optAction = a
    return optAction


def maxValue(board):
    v=-100 # technically -infinity
    if terminal(board):
        return utility(board)
    for a in actions(board):
        v= max(v,minValue(result(board,a)))
    return v

def minValue(board):
    v=100 # technically infinity
    if terminal(board):
        return utility(board)
    for a in actions(board):
        v= min(v,maxValue(result(board,a)))
    return v
