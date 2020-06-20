from collections import defaultdict as dd
from Board import *
from itertools import product
from CheckBoard import *


class Hint:

    def __init__(self, board, eng_dict, rack):
        self.board = board
        self.eng_dict = eng_dict
        self.rack = rack

    def similarLetters(self, word1, word2):


        w1 = dd(lambda: 0)
        w2 = dd(lambda: 0)
        counter = 0
        for letter in word1:
            w1[letter] += 1
        for letter in word2:
            w2[letter] += 1
        print(w1)
        print(w2)
        for key, val in w1.items():
            print(val,w2[key])
            counter += min(val, w2[key])
        return counter

    def freeUp(self, row, col):
        counter = 0
        i = row - 1
        while i >= 0:
            if self.board.board[i][col] == '_':
                counter += 1
            else:
                break
            i -= 1
        return counter

    def freeLeft(self, row, col):
        counter = 0
        i = col - 1
        while i >= 0:
            if self.board.board[row][i] == '_':
                counter += 1
            else:
                break
            i -= 1
        return counter

    def freeDown(self, row, col):
        counter = 0
        i = row + 1
        while i < len(self.board.board):
            if self.board.board[i][col] == '_':
                counter += 1
            else:
                break
            i += 1
        return counter

    def freeRight(self, row, col):
        counter = 0
        i = col + 1
        while i < len(self.board.board):
            if self.board.board[row][i] == '_':
                counter += 1
            else:
                break
            i += 1
        return counter

    def findHint(self):
        list_eng_dict = list(self.eng_dict)
        list_eng_dict.sort(key=lambda x: self.similarLetters(x, self.rack), reverse=True)
        list_eng_dict = [word for word in list_eng_dict if len(word) <= 5 and len(word) >= 2]
        print(len(list_eng_dict))
        print("wooop")
        board_letters_coords = dd()
        s = len(self.board.board)

        for i in range(s):
            for j in range(s):
                if self.board.board[i][j] != '_':
                    up = self.freeUp(i, j)
                    down = self.freeDown(i, j)
                    right = self.freeRight(i, j)
                    left = self.freeLeft(i, j)
                    board_letters_coords[self.board.board[i][j]] = [i, j, up, down, right, left]
        print("wooop2")
        print(board_letters_coords)

        for word in list_eng_dict:
            w = set(word)
            for letter in board_letters_coords.keys():
                if letter in w:
                    rack = self.rack[:]
                    rack.append(letter)
                    print(rack)


                    print("ohno")
                    print(word)
                    print(self.similarLetters(word,rack))
                    if self.similarLetters(word,rack) < len(word):
                        continue
                    else:
                        print("hello")
                        ind = word.index(letter)
                        l_left = ind
                        r_left = len(word) - ind - 1
                        free_up = board_letters_coords[letter][2]
                        free_down = board_letters_coords[letter][3]
                        free_right = board_letters_coords[letter][4]
                        free_left = board_letters_coords[letter][5]
                        x = board_letters_coords[letter][0]
                        y = board_letters_coords[letter][1]
                        horizon_good = l_left == free_left and r_left == free_right
                        vertic_good = l_left == free_up and r_left == free_down
                        w_coords = []
                        print(word)
                        if horizon_good or vertic_good:
                            print("uh")
                            if horizon_good:
                                print("wow")
                                print(x,y)
                                i = 0
                                j = ind
                                while i < len(word):
                                    w_coords.append((x,y-j))
                                    j -= 1
                                    i += 1

                                if CheckBoard(self.board).checkBoard(self.eng_dict, word, w_coords):
                                    return word, w_coords

                            if vertic_good:
                                print("wow")
                                i = 0
                                j = ind
                                while i < len(word):
                                    w_coords.append((x-j, y))
                                    j -= 1
                                    i += 1

                                if CheckBoard(self.board).checkBoard(self.eng_dict, word, w_coords):
                                    return word, w_coords
                        else:
                            continue
        return "", []
