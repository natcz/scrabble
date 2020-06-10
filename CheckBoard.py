from Board import *
from Word import *


class CheckBoard:

    def __init__(self, board):
        self.board = board

    def checkEmpty(self, word, row, col):
        if dir == "RIGHT":
            for i in range(len(word)):
                if self.board[col + i][row] != '_':
                    return False

        else:
            for i in range(len(word)):
                if self.board[col][row + i] != '_':
                    return False
        return True

    def checkRows(self, eng_dict):
        s = self.board.size
        for i in range(s):
            for j in range(s):
                new_word = ""
                if self.board[i][j] != '_':
                    for x in range(s - j - 1):
                        if self.board[i][j] != '_':
                            new_word += self.board[i][j + x]
                        else:
                            j = j + x
                            nw = Word(new_word)
                            if new_word != "":
                                if not nw.checkWord(eng_dict):
                                    return False

                            break
        return True

    def checkColumns(self, eng_dict):
        s = self.board.size
        for j in range(s):
            for i in range(s):
                new_word = ""
                if self.board[i][j] != '_':
                    for y in range(s - j - 1):
                        if self.board[i][j] != '_':
                            new_word += self.board[i][j + y]
                        else:
                            j = j + y
                            nw = Word(new_word)
                            if new_word != "":
                                if not nw.checkWord(eng_dict):
                                    return False

                            break
        return True

    def checkBoard(self, eng_dict, word, row, col, direct):
        temp_board = Board(eng_dict, self.board.size)
        temp_board.board = self.board
        w = Word(word)
        try:
            temp_board.boardUpdate(word, row, col, direct)
            temp_board_check = CheckBoard(temp_board)
            if not w.checkWord(eng_dict):
                return False
            elif not self.checkEmpty(word, row, col):
                return False
            elif not temp_board_check.checkRows(eng_dict):
                return False
            elif not temp_board_check.checkColumns(eng_dict):
                return False
            else:
                return True

        except ValueError:
            return False
