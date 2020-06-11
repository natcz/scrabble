from Sack import *
from random import shuffle
class Rack:

    def __init__(self, sack,max_l):
        self.rack = []
        self.sack = sack
        self.max_letters = max_l
        self.initRack()


    def initRack(self):
        for _ in range(self.max_letters):
            if self.sack.left_letters() != 0:
                self.rack.append(self.sack.take_letter())
        self.sack.shuffle()



    def fillRack(self):
        while len(self.rack) < self.max_letters and  self.sack.left_letters() > 0:
                self.rack.append(self.sack.take_letter())


    def exchangeAll(self):
        for letter in self.rack:
            self.sack.append(letter)
            self.rack.remove(letter)
        self.initRack()

    def exchangeOne(self, ind):
        letter = self.rack[ind]
        self.sack.append(letter)
        del self.rack[ind]
        self.rack.append(self.sack.take_letter())



