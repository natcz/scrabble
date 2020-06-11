from Player import *


class StartGame:

    def __init__(self, sack, name1, name2):
        self.instruction = "Welcome to Scrabble"
        self.player1 = self.newPlayer(sack, name1)
        self.player2 = self.newPlayer(sack, name2)

    def newPlayer(self, sack, name):
        max_num = 7
        return Player(sack, max_num, name)

    def viewInstruct(self):
        return self.instruction
