from Letters import *
from random import shuffle

class Sack:

    def __init__(self):
        self.sack = []          #list of letters available in the game
        self.bag = Letters()    #Letters() object with attribute bag which is a dict where
        self.initialize()       #key: letter - val: [points you get for the letter, number of tiles in the bag]

    def initialize(self):       #initializing the sack
        bag = self.bag.bag
        for elem in bag:
            for _ in range(bag[elem][1]):
                self.sack.append(elem)

    def leftLetters(self):     #number of letters left in the sack
        return len(self.sack)

    def takeLetter(self):      #getting random letter out of the sack
        shuffle(self.sack)      #using shuffle to randomize the output
        return self.sack.pop()  #returning char

    def getSack(self):
        return self.sack

    def remove(self,letter):
        if letter in set(self.sack):
            self.sack.remove(letter)

    def append(self,letter):
        self.sack.append(letter)








