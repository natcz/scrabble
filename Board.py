from Word import *
class Board:

    def __init__(self,dict,size):
        self.size = size
        self.board = [['_' for columns in range(size)] for rows in range(size)]
        self.dict = dict

    # new word, starting position, direction:right or down
    def boardUpdate(self,new_word, row, column, direction):

        nw = new_word.upper()
        dir = direction.upper()
        if len(nw) > self.size  or row > self.size or column > self.size or direction not in {"right", "down"}:
            raise ValueError("Not a proper coordinates or word length")
        elif dir == "RIGHT":
            for i in range(len(nw)):
                self.board[column+i][row] = nw[i]

        else:
            for i in range(len(nw)):
                 self.board[column][row+i] = nw[i]


    def getBoard(self):
        return self.board

    def checkEmpty(self,word,row,col):
        if dir == "RIGHT":
            for i in range(len(word)):
               if self.board[col+i][row] != '_':
                   return False

        else:
            for i in range(len(word)):
                if self.board[col][row+i] != '_':
                    return False
        return True

    def checkRows(self,dict):
        s = self.size
        for i in range(s):
            for j in range(s):
                new_word = ""
                if (self.board[i][j] != '_'):
                    for x in range(s - j - 1):
                        if (self.board[i][j] != '_'):
                            new_word += self.board[i][j + x]
                        else:
                            j = j + x
                            nw = Word(new_word)
                            if new_word != "":
                                if nw.checkWord(dict) == False:
                                    return False

                            break
        return True

    def checkColumns(self,dict):
        s = self.size
        for j in range(s):
            for i in range(s):
                new_word = ""
                if (self.board[i][j] != '_'):
                    for y in range(s - j - 1):
                        if (self.board[i][j] != '_'):
                            new_word += self.board[i][j + y]
                        else:
                            j = j + y
                            nw = Word(new_word)
                            if new_word != "":
                                if nw.checkWord(dict) == False:
                                    return False

                            break
        return True




    def checkBoard(self,dict,word,row,col,direct):
        temp_board = Board(dict,self.size)
        temp_board.board = self.board
        w = Word(word)
        try:
            temp_board.boardUpdate(word,row,col,direct)
            if w.checkWord(dict)==False:
                return False
            elif self.checkEmpty(word,row,col) == False:
                return False
            elif temp_board.checkRows(dict) == False:
                return False
            elif temp_board.checkColumns(dict) == False:
                return False
            else:
                return True

        except ValueError:
            return False
