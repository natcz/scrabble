from random import shuffle
from Letters import *

class Word:
    def __init__(self,word):
        self.bag = Letters()
        self.word = word

    def makeDict(self):
        try:
            d_file = open('dictionary')
            eng_dict = set()
            for line in d_file:
                line = line.strip()
                eng_dict.add(line.upper())
            return eng_dict
        except IOError:
            print("No such a file found")
       
           

    def checkWord(self, eng_dict):
        return self.word in eng_dict

    def makeupWord(self,rack,eng_dict):
        new_word = rack.shuffle()
        search_tries =  100
        while new_word not in eng_dict and search_tries > 0:
            new_word = rack.shuffle()
            search_tries -= 1
        if new_word not in eng_dict:
            s = "Cannot find a good word"
            return s
        else:
            return new_word

    def score(self):
        scr = 0
        for letter in self.word:
            scr += self.bag[letter][0]
        return scr


