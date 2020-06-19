from random import randint, choice

class Letters:

    def __init__(self):
        self.bag = dict()
        self.startLetters()

    # letter - points - number of tiles in the bag
    def startLetters(self):
        self.bag['A'] = [1,9]
        self.bag['B'] = [3,2]
        self.bag['C'] = [3,2]
        self.bag['D'] = [2,4]
        self.bag['E'] = [1,12]
        self.bag['F'] = [4,2]
        self.bag['G'] = [2,3]
        self.bag['H'] = [4,2]
        self.bag['I'] = [1,9]
        self.bag['J'] = [8,1]
        self.bag['K'] = [5,1]
        self.bag['L'] = [1,4]
        self.bag['M'] = [3,2]
        self.bag['N'] = [1,6]
        self.bag['O'] = [1,8]
        self.bag['Q'] = [10,1]
        self.bag['P'] = [3,2]
        self.bag['R'] = [1,6]
        self.bag['S'] = [1,4]
        self.bag['T'] = [1,6]
        self.bag['U'] = [1,4]
        self.bag['W'] = [4,2]
        self.bag['V'] = [4,2]
        self.bag['X'] = [8,1]
        self.bag['Y'] = [4,2]
        self.bag['Z'] = [10,1]

    def getLetters(self):
        return self.bag

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






