from Word import *


class Board:

    def __init__(self, size):
        self.size = size                                                         #size of the board (int)
        self.board = [['_' for columns in range(size)] for rows in range(size)]  #representation of the board


    def boardUpdate(self, new_word, coords):    #adding new_word(string) on the board
        nw = new_word.upper()                   # coords is a deafaultdict where key: coordinates of the letter (x,y) val: letter
        for i in range(len(coords)):
            self.board[coords[i][0]][coords[i][1]] = nw[i]

    def getBoard(self):
        return self.board
