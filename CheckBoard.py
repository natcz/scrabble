from Board import *
from Word import *


class CheckBoard:

    def __init__(self, board):
        self.board = board

    def checkRows(self, eng_dict):
        s = self.board.size
        b = self.board
        row = 0
        while row < s:
            col = 0
            while col < s:
                if b.board[row][col] != '_':
                    new_word = ""
                    counter = 0
                    for i in range(col, s):
                        if b.board[row][i] != '_':
                            new_word += b.board[row][i]
                            counter += 1
                        else:
                            if new_word != "" and len(new_word) != 1:
                                nw = Word(new_word)
                                print(new_word)
                                if not nw.checkWord(eng_dict):
                                    return False
                            col += counter
                            break
                col += 1
            row += 1
        return True






    def checkColumns(self, eng_dict):
        s = self.board.size
        b = self.board

        col = 0
        while col < s:
            row = 0
            while row < s:
                if b.board[row][col] != '_':
                    new_word = ""
                    counter = 0
                    for i in range(row,s):
                        if b.board[i][col] != '_':
                            new_word += b.board[i][col]
                            counter += 1
                        else:
                            if new_word != "" and len(new_word) != 1:
                                print(new_word)
                                nw = Word(new_word)
                                if not nw.checkWord(eng_dict):
                                    return False
                            row += counter
                            break
                row += 1
            col += 1

        return True





    def checkBoard(self, eng_dict, word, coords):
        temp_board = Board(eng_dict, self.board.size)
        board = self.board.getBoard()
        temp_board.board = board[:]


        try:
            temp_board.boardUpdate(word,coords)
            temp_board_check = CheckBoard(temp_board)
            if not temp_board_check.checkRows(eng_dict):
                return False
            elif not temp_board_check.checkColumns(eng_dict):
                return False
            else:
                return True

        except ValueError:
            return False