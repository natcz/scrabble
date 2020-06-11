from Letters import *
from random import shuffle

class Sack:

    def __init__(self):
        self.sack=[]
        self.bag = Letters()
        self.intitSack()
        self.sack.shuffle()


    def initSack(self):
        for elem in self.bag:
            for _ in range(self.bag[elem][1]):
                self.sack.append(elem)

    def left_letters(self):
        return len(self.sack)

    def take_letter(self):
        return  self.sack.pop()






