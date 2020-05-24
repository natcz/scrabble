from Rack import *
from Sack import *
from Word import *

class Player:
    def __init__(self,sack,max_l):
        self.rack = Rack(sack,max_l)
        self.score = 0

    def getScore(self):
        return self.score

    def incScore(self,word):
        w = Word(word)
        plus_scr = w.score()
        self.score += plus_scr



