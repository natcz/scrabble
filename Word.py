class Word:

    def __init__(self, w):
        self.word = w

    def makeDict(self):
        try:
            d_file = open('dictionary.txt')
        except IOError:
            print("No such a file found")
        with d_file:
            eng_dict = set()
            for line in d_file:
                line = line.strip()
                eng_dict.add(line.upper())

    def checkWord(self, word, dict):
        return word in dict
