from random import shuffle
from Letters import *


class Word:
    def __init__(self, word):
        self.bag = Letters()  # Letters() object with attribute bag which is a dict where
        self.word = word      # key: letter - val: [points you get for the letter, number of tiles in the bag]

    def checkWord(self, eng_dict):  # checking if word is in the english dictionary (eng_dict)
        return self.word in eng_dict

    def score(self, coords):  # calculating the score player gets for his move
        scr = 0               # coords is a deafaultdict where key: coordinates of the letter (x,y) val: letter
        for letter in self.word:
            for key, val in coords.items():
                if val == letter:
                    xy = key
            scr += self.bag.bag[letter][0] * self.bonusPoints(xy)  # scr is a score player gets (int)
        return scr

    def bonusPoints(self, xy):  # calculating bonus score for the letter
        mult3 = {(7, 3), (3, 7), (7, 11), (11, 7)}  # xy = (x,y) coordinates of the letter on the board
        mult2 = {(5, 5), (9, 9), (5, 9),
                 (9, 5)}  # multA is a set of coordinates (x,y) on which you get a bonus A*points for letter
        mult4 = {(3, 3), (11, 3), (3, 11), (11, 11)}
        mult5 = {(0, 0), (14, 14), (0, 14), (14, 0)}

        if xy in mult3:
            return 3
        elif xy in mult2:
            return 2
        elif xy in mult4:
            return 4
        elif xy in mult5:
            return 5
        return 1  # neutral element of multiplication
