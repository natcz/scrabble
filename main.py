from tkinter import *
from BoardVisual import *
from StartGame import *
from Sack import *

from BoardVisual import *
class Main:
    startframe: Frame

    def __init__(self):
        self.root = Tk()
        self.startframe = Frame(self.root)
        self.mainframe = Frame(self.root)
        self.sack = Sack()
        self.startgame = StartGame(self.sack,"pl1", "pl2")

        self.root.title("Scrabble")
        self.root.geometry("1500x900")
        self.startframe.grid(column = 0, row = 0)
        startLabel = Label(self.startframe, text = "Welcome to Scrabble!")
        startLabel.grid(column = 3, row = 0)
        startButton = Button(self.startframe, text = "New game", command = print("clicked!"))
        startButton.grid(column = 3, row = 5)
        instrButton = Button(self.startframe, text = "See the instruction", command = lambda: Main.get_instr(self))
        instrButton.grid(column = 3, row = 8)
        self.root.mainloop()



    def get_instr(self):
        instrWindow =  Toplevel()
        instr = self.startgame.viewInstruct()
        instrmsg = Message(instrWindow, text = instr)
        instrmsg.grid(column = 1, row = 1)
        closeinstrButton = Button(instrWindow, text = "Ok, I get it", command = instrWindow.destroy)
        closeinstrButton.grid(column = 3, row = 3)


    def getPlayersNames(self):
        self.name1entry = Entry(self.startframe, validate="key", validatecommand=(vcmd, '%P'))


Main()