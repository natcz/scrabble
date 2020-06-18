from random import randint, choice

class Letters:

    def __init__(self):
        self.bag = dict()
        self.startLetters()

    # letter - points - number of tiles in the bag
    def startLetters(self):
        self.bag['A'] = [randint(1, 15),randint(1, 3)]
        self.bag['B'] = [randint(1, 15),randint(1, 3)]
        self.bag['C'] = [randint(1, 15),randint(1, 3)]
        self.bag['D'] = [randint(1, 15),randint(1, 3)]
        self.bag['E'] = [randint(1, 15),randint(1, 3)]
        self.bag['F'] = [randint(1, 15),randint(1, 3)]
        self.bag['G'] = [randint(1, 15),randint(1, 3)]
        self.bag['H'] = [randint(1, 15),randint(1, 3)]
        self.bag['I'] = [randint(1, 15),randint(1, 3)]
        self.bag['J'] = [randint(1, 15),randint(1, 3)]
        self.bag['K'] = [randint(1, 15),randint(1, 3)]
        self.bag['L'] = [randint(1, 15),randint(1, 3)]
        self.bag['M'] = [randint(1, 15),randint(1, 3)]
        self.bag['N'] = [randint(1, 15),randint(1, 3)]
        self.bag['O'] = [randint(1, 15),randint(1, 3)]
        self.bag['Q'] = [randint(1, 15),randint(1, 3)]
        self.bag['P'] = [randint(1, 15),randint(1, 3)]
        self.bag['R'] = [randint(1, 15),randint(1, 3)]
        self.bag['S'] = [randint(1, 15),randint(1, 3)]
        self.bag['T'] = [randint(1, 15),randint(1, 3)]
        self.bag['U'] = [randint(1, 15),randint(1, 3)]
        self.bag['W'] = [randint(1, 15),randint(1, 3)]
        self.bag['V'] = [randint(1, 15),randint(1, 3)]
        self.bag['X'] = [randint(1, 15),randint(1, 3)]
        self.bag['Y'] = [randint(1, 15),randint(1, 3)]
        self.bag['Z'] = [randint(1, 15),randint(1, 3)]

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






