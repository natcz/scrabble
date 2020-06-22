from Rack import *
from Sack import *
from Word import *

class Player:
    def __init__(self,sack,max_l,name):
        self.rack = Rack(sack,max_l)
        self.score = 0
        self.name = name

    def getScore(self):     #returning score (int)
        return self.score

    def incScore(self,word,coords):  #increasing score , word - string
        w = Word(word)               #coords is a deafaultdict where key: coordinates of the letter (x,y) val: letter
        plus_scr = w.score(coords)   #calculating score increase using Word() score method (it returns int)
        self.score += plus_scr





