from random import shuffle
from Letters import *


class Word:
    def __init__(self, word):
        self.bag = Letters()
        self.word = word


    def checkWord(self, eng_dict):
        return self.word in eng_dict



    def score(self,coords):
        scr = 0
        for letter in self.word:
            for key,val in coords.items():
                if val == letter:
                    xy = key
            scr += self.bag.bag[letter][0] * self.bonusPoints(xy)
        return scr

    def bonusPoints(self,xy):
        mult3 = {(7,3), (3,7), (7,11), (11,7)}
        mult2 = {(5,5), (9,9), (5,9), (9,5)}
        mult4 = {(3,3), (11,3), (3,11), (11,11)}
        mult5 = {(0,0), (14,14), (0,14), (14,0)}

        if xy in mult3:
            return 3
        elif xy in mult2:
            return 2
        elif xy in mult4:
            return 4
        elif xy in mult5:
            return 5
        return 1
