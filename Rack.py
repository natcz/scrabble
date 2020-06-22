from Sack import *
from random import shuffle


class Rack:

    def __init__(self, sack, max_l):
        self.rack = []               # list of letters available to the player
        self.sack = sack             # sack of all the letters
        self.max_letters = max_l     # max number of letters in the rack
        self.initRack()

    def initRack(self):                      # initializing rack by getting out random letters from the sack
        sack = self.sack.getSack()
        shuffle(sack)                        # randomizing letters in the sack by shuffling them
        for i in range(self.max_letters):
            if self.sack.leftLetters() != 0:  # making sure sack isn't empty
                self.rack.append(sack[i])
                self.sack.remove(sack[i])

    def fillRack(self):  # refilling the rack to make sure it always contains max_l letters
        sack = self.sack.getSack()
        shuffle(sack)
        while len(self.rack) <= self.max_letters and self.sack.leftLetters() > 0:
            self.rack.append(sack[0])
            self.sack.remove(sack[0])

    def exchangeAll(self):             # exchanging all the letters in the rack
        rack = self.rack[:]
        for i in range(len(rack)):
            self.rack.remove(rack[i])  # removing letters from the rack
            self.sack.append(rack[i])  # adding letters back to the sack
        self.initRack()                # initializing the rack again

    def exchangeOne(self, ind):             # exchanging one particular letter
        letter = self.rack[ind]             # getting the info from the index
        self.sack.append(letter)
        new_letter = self.sack.takeLetter()  # taking new letter out of the sack
        self.rack[ind] = new_letter
        self.sack.remove(new_letter)
        return new_letter

    def getRack(self):
        return self.rack

    def remove(self, letter):  # removing letter out of the rack
        self.rack.remove(letter)
