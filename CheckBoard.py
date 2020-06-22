from Board import *
from Word import *


class CheckBoard:

    def __init__(self, board):
        self.board = board  # Board() object

    def checkRows(self, eng_dict):      #checking if all of the words placed in rows of the board are in the eng_dict set
                                        #returning boolean
        s = self.board.size
        b = self.board
        row = 0
        while row < s:
            col = 0                 #column (int)
            while col < s:
                if b.board[row][col] != '_':
                    new_word = ""
                    counter = 0
                    for i in range(col, s):     #searching for a whole word
                        if b.board[row][i] != '_':
                            new_word += b.board[row][i]
                            counter += 1
                        else:
                            if new_word != "" and len(new_word) > 1:   #if we found whole word
                                nw = Word(new_word)                    #we are checking if it appears in the eng_dict set
                                if not nw.checkWord(eng_dict):         #using Word() method
                                    return False
                            col += counter
                            break
                col += 1
            row += 1
        return True

    def checkColumns(self, eng_dict): #checking if all of the words placed in columns of the board are in the eng_dict set
                                      # returning boolean
        s = self.board.size
        b = self.board
        col = 0
        while col < s:
            row = 0
            while row < s:
                if b.board[row][col] != '_':
                    new_word = ""
                    counter = 0
                    for i in range(row, s):     #searching for a whole word
                        if b.board[i][col] != '_':
                            new_word += b.board[i][col]
                            counter += 1
                        else:
                            if new_word != "" and len(new_word) > 1:  #if we found whole word
                                nw = Word(new_word)                   #we are checking if it appears in the eng_dict set
                                if not nw.checkWord(eng_dict):        #using Word() method
                                    return False
                            row += counter
                            break
                row += 1
            col += 1
        return True

    def checkBoard(self, eng_dict, word, coords): #checking if we can place the word with letter coordinates (coords) on the board
                                                  #returnning boolean
        temp_board = Board(self.board.size)       #temporary board on which we test the placing
        board = self.board.getBoard()
        temp_board.board = board[:]

        try:
            temp_board.boardUpdate(word, coords)        #using board updating method from Board()
            temp_board_check = CheckBoard(temp_board)
            if not temp_board_check.checkRows(eng_dict):
                return False
            elif not temp_board_check.checkColumns(eng_dict):
                return False
            else:
                return True

        except ValueError:
            return False
