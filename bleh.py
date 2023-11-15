BOARD_W = 3
BOARD_H = 3

EMPTY =" "
X = "X"
O = "O"

board = [ EMPTY ] * BOARD_W *BOARD_H

def draw(board):
    for row in range(BOARD_H):
        for col in range(BOARD_W):
            i = row * BOARD_W + col

            if BOARD_W - col > 1:
                print(board [i] + "|" , end = "")
            else:
                print(board [i] + "\n" , end = "")
        
        if BOARD_H - row > 1:
            for col in range(BOARD_W):
                if BOARD_W - col > 1:
                    print("-+" , end = "")
                else:
                    print("-\n" , end = "")

def put(board, where, what):
    row = ord(where[1]) - ord("1")
    col = ord(where[0]) - ord("A")
    i = row * BOARD_W + col
    board[i] = what

def count(straight, what):
    count=0
    for s in straight:
        if s == what:
            count +=1
    return count

def at(row, col):
    return row * BOARD_W + col

def check_rows(board, length):
    for row in range(BOARD_H):
        straight = [
              board[at(row, 0)],
              board[at(row, 1)],
              board[at(row, 2)]
          ]
        if count (straight, X) == 3: return X
        if count (straight, O) == 3: return O
    return None

def check_cols(board):
    for col in range(BOARD_W):
        straight = [
            board[at(0, col)],
            board[at(1, col)],
            board[at(2, col)]
        ]
        if count (straight, X) == 3: return X
        if count (straight, O) == 3: return O
    return None
    pass
      





def x_turn():
    pass

def o_turn():
    pass