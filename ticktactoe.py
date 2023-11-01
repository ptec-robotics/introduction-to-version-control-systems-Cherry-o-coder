BOARD_W = 3
BOARD_H = 3

NONE =" "
X = "X"
O = "O"

board = [ NONE ] * BOARD_W *BOARD_H

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
    pass

draw(board)