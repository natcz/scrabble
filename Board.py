class Board:

    def __init__(self):
        self.board = [['_' for columns in range(10)] for rows in range(10)]

    # new word, starting position, direction:right or down
    def boardUpdate(self,new_word, row, column, direction):

        nw = new_word.upper()
        dir = direction.upper()
        if len(nw)>9  or row>9 or column>9 or direction not in {"right", "down"}:
            raise ValueError("Not a proper coordinates or word length")
        elif dir == "RIGHT":
            for i in range(len(nw)):
                self.board[column+i][row] = nw[i]

        else:
            for i in range(len(nw)):
                 self.board[column][row+i] = nw[i]


    def getBoard(self):
        return self.board
