from Sack import *
from random import shuffle
class Rack:

    def __init__(self, sack,max_l):
        self.rack = []
        self.sack = sack
        self.max_letters = max_l
        self.initRack()


    def initRack(self):
        sack = self.sack.getSack()
        shuffle(sack)
        for i in range(self.max_letters):
            if self.sack.left_letters() != 0:
                self.rack.append(sack[i])
                self.sack.remove(sack[i])





    def fillRack(self):
        sack = self.sack.getSack()
        shuffle(sack)
        while len(self.rack) < self.max_letters and  self.sack.left_letters() > 0:
                self.rack.append(sack[0])
                self.sack.remove(sack[0])



    def exchangeAll(self):
        rack = self.rack[:]
        for i in range(len(rack)):
            self.rack.remove(rack[i])
            self.sack.append(rack[i])
        self.initRack()


    def exchangeOne(self, ind):
        letter = self.rack[ind]
        self.sack.append(letter)
        new_letter = self.sack.take_letter()
        self.rack[ind] = new_letter
        self.sack.remove(new_letter)
        return new_letter

    def getRack(self):
        return self.rack


