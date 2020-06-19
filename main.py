from tkinter import *
from BoardVisual import *
from Board import *
from StartGame import *
from Sack import *
from Player import *
from BoardVisual import *
from GameController import *
from Letters import *

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


    def get_instr(self):
        instrWindow = Toplevel()
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
        GameContr = GameController(self.root,self.mainframe,self.sack)
        board = BoardVisual(self.root,self.mainframe, b)
        emptyLabel = Label(self.mainframe,text="     ").grid(column=19, row = 1)
        skipB = Button(self.mainframe,text="SKIP", width= 12)
        skipB["command"] = lambda: GameContr.skip(self.player1,self.player2,PScoreLabel,ScoreLabel,TurnLabel,PRackButtons)
        exchangeAllB = Button(self.mainframe,text="EXCHANGE ALL", width= 12)
        exchangeAllB["command"] = lambda: GameContr.exchangeAll(self.player1,self.player2,PRackButtons)
        exchangeOneB = Button(self.mainframe, text="EXCHANGE ONE", width= 12)
        exchangeOneB["command"] = lambda: GameContr.exchangeOne(self.player1,self.player2,PRackButtons,board.board)
        hintButton = Button(self.mainframe,text="HINT", width= 12)
        endMoveButton = Button(self.mainframe, text="END MOVE", width= 12)
        endMoveButton["command"] = lambda: GameContr.endTurn(self.player1,self.player2,PScoreLabel,ScoreLabel,TurnLabel,PRackButtons,board.board)
        skipB.grid(column = 20, row = 11)
        exchangeAllB.grid(column = 20, row = 7)
        exchangeOneB.grid(column = 20, row = 8)
        hintButton.grid(column = 20, row = 9)
        endMoveButton.grid(column = 20, row = 10)
        TurnLabel = Label(self.mainframe, text="IT'S " + str(self.player1.name).upper() + "'S TURN")
        PScoreLabel = Label(self.mainframe, text=str(self.player1.name).upper() +"'S SCORE:")
        ScoreLabel = Label(self.mainframe, text=str(self.player1.score))
        TurnLabel.grid(column=20, row=2)
        PScoreLabel.grid(column=20, row=3)
        ScoreLabel.grid(column=21, row=3)
        emptyL =Label(self.mainframe,text= "POINTS\n"
                                           " FOR LETTERS:")
        emptyL.grid(column =30,row=1)
        letters = Letters()
        bag=letters.bag
        i = 0
        for key,val in bag.items():
            if i<=12:
                LettersL = Label(self.mainframe,text=str(key) + " = " + str(val[0]) + "   ")
                LettersL.grid(column=31, row=2+i)

            else:
                LettersL = Label(self.mainframe, text=str(key) + " = " + str(val[0]))
                LettersL.grid(column=32, row=2 + i-13)
            i+=1


        PRackButtons = []
        playerRack = self.player1.rack.getRack()

        emptyL2= Label( self.mainframe, text = "    ").grid(column =22, row= 1)
        for i in range(len(playerRack)):
            button = Button(self.mainframe, height=3, width=3, bg="bisque", fg="gray1", text=str(playerRack[i]))
            button.grid(column=23+i, row=9)
            PRackButtons.append(button)

        for i in range(len(PRackButtons)):
            PRackButtons[i]["command"] = lambda x=i: GameContr.makeMove(self.player1,self.player2,x, board.board,PRackButtons)













a=Main()
a.root.mainloop()
