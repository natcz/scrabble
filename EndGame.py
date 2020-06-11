from Player import *
class EndGame:
    def __init__(self,player1,player2,best_word):
        self.player1 = player1
        self.player2 = player2
        self.best_word = best_word


    def best_play_score(self):
        score1 = self.player1.getScore()
        score2 = self.player2.getScore()
        if score1 > score2:
            return self.player1
        elif score2 > score1:
            return self.player2
        else:
            return False     #remis


    def best_word_score(self):
        max_scr = max(self.best_word, key=lambda x: self.best_word[x])
        word = list(self.best_word.keys())[list(self.best_word.values()).index(max_scr)]
        return [word, max_scr]

