from Player import *
from tkinter import  *
class EndGame:
    def __init__(self,player1,player2,root,frame):
        self.player1 = player1
        self.player2 = player2
        self.root = root
        self.frame = frame



    def best_play_score(self):
        score1 = self.player1.getScore()
        score2 = self.player2.getScore()
        if score1 > score2:
            return self.player1
        elif score2 > score1:
            return self.player2
        else:
            return False     #remis

    def endWindow(self):
        endWindow = Toplevel()
        winner = self.best_play_score()
        endMessage = Message(endWindow, text = "GAME OVER!\n" + "CONGRATULATIONS" + str(winner.name).upper())
        endB = Button(endWindow, text = "EXIT")
        endB["command"] = lambda: self.root.destroy()
        endMessage.grid(column = 1, row = 1)
        endB.grid(column = 2, row = 2)




