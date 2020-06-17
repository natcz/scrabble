from tkinter import *
from BoardVisual import *
from Board import *
from StartGame import *
from Sack import *
from Player import *
from BoardVisual import *
from GameController import *

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
        skipB = Button(self.mainframe,text="SKIP",command= lambda: GameController.skip(self.player1,self.player2,PScoreLabel,ScoreLabel,TurnLabel,PRackButtons))
        exchangeAllB = Button(self.mainframe,text="EXCHANGE ALL",command= lambda: GameController.exchangeAll(self.player1,self.player2,PRackButtons))
        exchangeOneB = Button(self.mainframe, text="EXCHANGE ONE",command= lambda: GameController.exchangeOne(self.player1,self.player2,PRackButtons))
        hintButton = Button(self.mainframe,text="HINT")
        endMoveButton = Button(self.mainframe, text="END MOVE")
        skipB.grid(column = 20, row = 10)
        exchangeAllB.grid(column = 20, row = 11)
        exchangeOneB.grid(column = 20, row = 12)
        hintButton.grid(column = 20, row = 13)
        endMoveButton.grid(column = 20, row = 14)
        TurnLabel = Label(self.mainframe, text="IT'S " + str(self.player1.name).upper() + "'S TURN")
        PScoreLabel = Label(self.mainframe, text=str(self.player1.name).upper() +"'S SCORE:")
        ScoreLabel = Label(self.mainframe, text=str(self.player1.score))
        TurnLabel.grid(column=21, row=2)
        PScoreLabel.grid(column=21, row=3)
        ScoreLabel.grid(column=22, row=3)
        PRackButtons = []
        playerRack = self.player1.rack.getRack()

        for i in range(len(playerRack)):
            button = Button(self.mainframe, height=3, width=3, bg="bisque", fg="gray1", text=str(playerRack[i]))
            button.grid(column=22+i, row=6)
            PRackButtons.append(button)












a=Main()
a.root.mainloop()
