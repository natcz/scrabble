from tkinter import *
from BoardVisual import *
from Board import *
from StartGame import *
from Sack import *
from Player import *
from BoardVisual import *

class Main:
    startframe: Frame

    def __init__(self):
        self.root = Tk()
        self.startframe = Frame(self.root)
        self.mainframe = Frame(self.root)
        self.sack = Sack()
        self.player1 = Player(self.sack,7,"")
        self.player2 = Player(self.sack,7,"")
        self.startgame = StartGame()

        self.root.title("Scrabble")
        self.root.geometry("1500x900")
        self.startframe.grid(column = 0, row = 0)
        startLabel = Label(self.startframe, text = "Welcome to Scrabble!")
        startLabel.grid(column = 3, row = 0)
        startButton = Button(self.startframe, text = "New game", command = lambda: Main.getNames(self))
        startButton.grid(column = 3, row = 5)
        instrButton = Button(self.startframe, text = "See the instruction", command = lambda: Main.get_instr(self))
        instrButton.grid(column = 3, row = 8)
        self.root.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_instr(self):
        instrWindow =  Toplevel()
        instr = self.startgame.viewInstruct()
        instrmsg = Message(instrWindow, text = instr)
        instrmsg.grid(column = 1, row = 1)
        closeinstrButton = Button(instrWindow, text = "Ok, I get it", command = instrWindow.destroy)
        closeinstrButton.grid(column = 3, row = 3)


    def getNames(self):
        nameWindow = Toplevel()
        name1entry = Entry(nameWindow)
        name1Label = Label(nameWindow, text = "Player1")
        name2entry = Entry(nameWindow)
        name2Label = Label(nameWindow, text="Player2")
        confirmB = Button(nameWindow, text="Confirm" , command = lambda : [saveName(self),nameWindow.destroy(), self.startframe.destroy(),Main.letsPlay(self)])

        name1entry.grid(column = 2,  row = 1)
        name2entry.grid(column = 2, row = 3)
        name1Label.grid(column=1, row=1)
        name2Label.grid(column=1, row=3)
        confirmB.grid(column = 3, row = 3)

        def saveName(self):
            self.player1.name = name1entry.get()
            self.player2.name = name2entry.get()

    def letsPlay(self):
        b = [['' for columns in range(15)] for rows in range(15)]
        board = BoardVisual(self.root,self.mainframe, b)
        



Main()
