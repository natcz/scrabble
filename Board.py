from Word import *
class Board:

    def __init__(self,eng_dict,size):
        self.size = size
        self.board = [['_' for columns in range(size)] for rows in range(size)]
        self.dict = eng_dict

    # new word, starting position, direction:right or down
    def boardUpdate(self,new_word, row, column, direction):

        nw = new_word.upper()
        direct = direction.upper()
        if len(nw) > self.size or row > self.size or column > self.size or direct not in {"RIGHT", "DOWN"}:
            raise ValueError("Not a proper coordinates or word length")
        elif direct == "DOWN":
            for i in range(len(nw)):
                self.board[row+i][column] = nw[i]

        else:
            for i in range(len(nw)):
                 self.board[row][column+i] = nw[i]


    def getBoard(self):
        return self.board





