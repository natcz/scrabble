from Letters import *
from random import shuffle
class Rack:

    def __intit__(self):
        self.rack=[]
        self.intitRack()
        self.rack.shuffle()


    def initRack(self):
        for elem in Letters:
            for _ in range(elem[1]):
                self.rack.add((elem,elem[0]))

    def left_letters(self):
        return len(self.rack)

    def take_letter(self):
        return  self.rack.pop()


