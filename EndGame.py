from Player import *
from tkinter import *


class EndGame:
    def __init__(self, player1, player2, root):
        self.player1 = player1
        self.player2 = player2
        self.root = root

    def bestPlayer(self):        # checking which player won
        score1 = self.player1.getScore()
        score2 = self.player2.getScore()
        if score1 > score2:
            return self.player1  # returning Player() object
        else:
            return self.player2

    def endWindow(self):            # window appears when the game is over
        endWindow = Toplevel()      # creating a Toplevel window
        winner = self.bestPlayer()  # Player() object
        endMsg = Message(endWindow, text="GAME OVER!\n" + "CONGRATULATIONS" + str(winner.name).upper())
        exitB = Button(endWindow, text="EXIT")
        exitB["command"] = lambda: self.root.destroy()  # destroys root (whole game window)
        endMsg.grid(column=1, row=1)                    # placing objects inside the window
        exitB.grid(column=2, row=2)
