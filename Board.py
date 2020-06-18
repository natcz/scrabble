from Word import *
class Board:

    def __init__(self,eng_dict,size):
        self.size = size
        self.board = [['_' for columns in range(size)] for rows in range(size)]
        self.dict = eng_dict

    # new word, starting position, direction:right or down
    def boardUpdate(self,new_word,coords):

        nw = new_word.upper()
        for i in range(len(coords)):
            self.board[coords[i][0]][coords[i][1]] = nw[i]



    def getBoard(self):
        return self.board





