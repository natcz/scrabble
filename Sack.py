from Letters import *
from random import shuffle

class Sack:

    def __init__(self):
        self.sack = []
        self.bag = Letters()
        self.intitalize()

    def initialize(self):
        for elem in self.bag:
            for _ in range(self.bag[elem][1]):
                self.sack.append(elem)

    def left_letters(self):
        return len(self.sack)

    def take_letter(self):
        shuffle(self.sack)
        return  self.sack.pop()

    def intitalize(self):
        bag = self.bag.getLetters()
        for elem in bag:
            for _ in range(bag[elem][1]):
                self.sack.append(elem)


    def getSack(self):
        return self.sack

    def remove(self,letter):
        if letter in set(self.sack):
            self.sack.remove(letter)
    def append(self,letter):
        self.sack.append(letter)





