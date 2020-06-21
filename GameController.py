from Rack import *
from Board import *
from Letters import *
from tkinter import *
from CheckBoard import *
from collections import defaultdict as dd
from Word import *
from EndGame import *
from Hint import *

turn = 1
good_first_word = False
Wcoordinates = dd()
coord = []
l = Letters()
eng_dict = l.makeDict()
demoBoard = Board(eng_dict,15)
rack_indx = dd()

class GameController:

    def __init__(self,root,frame,sack):
        self.root = root
        self.sack = sack
        self.frame = frame


    def skip(self,pl1,pl2,scrLabel,scrL,turnLabel,rackButtons):
        global turn
        if turn % 2 == 0:
            scrLabel["text"] = str(pl1.name).upper() +"'S SCORE:"
            scrL["text"] = str(pl1.score)
            turnLabel["text"] = "IT'S " + str(pl1.name).upper() + "'S TURN"
            playerRack = pl1.rack.getRack()
            for i  in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])
            turn += 1


        else:
            scrLabel["text"] = str(pl2.name).upper() + "'S SCORE:"
            scrL["text"] = str(pl2.score)
            turnLabel["text"] = "IT'S " + str(pl2.name).upper() + "'S TURN"
            playerRack = pl2.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])
            turn += 1



    def exchangeAll(self,pl1,pl2,rackButtons):
        global turn

        if turn % 2 != 0:
            pl1.rack.exchangeAll()
            playerRack = pl1.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])
        else:
            pl2.rack.exchangeAll()
            playerRack = pl2.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])


    def exchangeOne(self,pl1,pl2,rackButtons,board):
        def exOne(button,ind,pl1,pl2):
            if turn % 2 != 0:
                new_letter = pl1.rack.exchangeOne(ind)
                button.config(text= str(new_letter).upper())
            else:
                new_letter = pl2.rack.exchangeOne(ind)
                button.config(text=str(new_letter).upper())
        def disableB(self,buttons):
            for i in range(len(buttons)):
                buttons[i]["command"] = lambda x=i: self.makeMove(pl1,pl2,x, board,rackButtons)


        for i in range(len(rackButtons)):
            rackButtons[i].config(command=lambda x=i: [exOne(rackButtons[x], x, pl1, pl2),disableB(self,rackButtons)])





    def makeMove(self,pl1,pl2,ind,board,rackButtons,exAllButton,exOneButton,skipButton):
        global rack_indx
        def placeLetter(button,row,col,letter):
            global coord
            global Wcoordinates
            button["text"] = str(letter).upper()
            Wcoordinates[(row, col)] = letter
            coord.append((row, col))



        if turn % 2 != 0:
            letter = pl1.rack.getRack()[ind]
            rack_indx[letter] = ind


        else:
            letter = pl2.rack.getRack()[ind]
            rack_indx[letter] = ind

        for row in range(15):
            for col in range(15):
                board[row][col]["command"] = lambda c=col, r=row:placeLetter(board[r][c],r,c,letter)
        rackButtons[ind]["state"] = "disabled"
        exAllButton["state"] = "disabled"
        exOneButton["state"] = "disabled"
        skipButton["state"] = "disabled"


    def undoMove(self,coords,board,rackButtons,pl1,pl2):
        global demoBoard
        for i in range(len(coords)):
            board[coords[i][0]][coords[i][1]]["text"] = " "
            demoBoard.board[coords[i][0]][coords[i][1]] = "_"
        for i in range(len(rack_indx)):
            rackButtons[i]["state"] = "normal"


    def makeProperWord(self):
        global Wcoordinates, coord
        sameRow = True
        sameCol = True
        c = coord[0][1]
        r = coord[0][0]
        word = ""
        for pair in coord:
            if pair[0] != r:
                sameRow = False
            if pair[1] != c:
                sameCol = False
        if not sameRow and not sameCol:
            return ""
        elif sameRow:
            coord.sort(key=lambda x: x[1])
            for pair in coord:
                word += Wcoordinates[pair]
            return word
        else:
            coord.sort()
            for pair in coord:
                word += Wcoordinates[pair]
            return word



    def endTurn(self,pl1,pl2,scrLabel,scrL,turnLabel,rackButtons,visualB,hintButton,exAllButton,exOneButton,skipButton):
        global coord,eng_dict,rack_indx,turn
        global Wcoordinates,demoBoard,good_first_word
        checkB = CheckBoard(demoBoard)
        proper_word = self.makeProperWord()
        w = Word(proper_word)

        for i in range(len(rackButtons)):
            rackButtons[i]["state"] = "normal"


        if turn == 1 or not good_first_word:

            if coord[0] == (7,7):
                if w.checkWord(eng_dict):
                    board_ok = True
                    good_first_word = True
                else:
                    board_ok = False
            else:
                board_ok = False
            hintButton["state"] = "normal"
            exAllButton["state"] = "normal"
            exOneButton["state"] = "normal"
            skipButton["state"] = "normal"
        else:
            board_ok = checkB.checkBoard(eng_dict, proper_word, coord)

        if board_ok:
            demoBoard.boardUpdate(proper_word,coord)

            if turn % 2 != 0:
                for xy in coord:
                    l = Wcoordinates[xy]
                    pl1.remove(l)
                    ind = rack_indx[l]
                    rackButtons[ind]["text"] = " "
                pl1.incScore(proper_word,Wcoordinates)

            else:
                for xy in coord:
                    l = Wcoordinates[xy]
                    pl2.remove(l)
                    ind = rack_indx[l]
                    rackButtons[ind]["text"] = " "
                pl2.incScore(proper_word,Wcoordinates)



        else:
            bad_wordWindow = Toplevel()
            if turn % 2 != 0:
                fail_msg = Message(bad_wordWindow,text = "Not a proper move " + str(pl1.name).upper() + ". You've lost your chance")
            else:
                fail_msg = Message(bad_wordWindow,
                                   text="Not a proper move " + str(pl2.name).upper() + ". You've lost your chance")
            fail_msg.grid(row = 1, column = 1)
            ok_Button = Button(bad_wordWindow,text = "OK",command = lambda: bad_wordWindow.destroy())
            ok_Button.grid(row = 2, column = 2)
            self.undoMove(coord,visualB,rackButtons,pl1,pl2)
        if pl1.score >= 50 or pl2.score >= 50 or self.sack.sack == []:
            self.endGame(pl1,pl2)

        Wcoordinates = dd()
        coord = []
        rack_indx = dd()
        if turn % 2 != 0:
            pl1.rack.fillRack()

        else:
            pl2.rack.fillRack()
        self.skip(pl1,pl2,scrLabel,scrL,turnLabel,rackButtons)

    def hint(self,pl1,pl2):

        if turn % 2 != 0:
            h = Hint(demoBoard,eng_dict,pl1.rack.getRack())
            word,w_coord = h.findHint()
        else:
            h = Hint(demoBoard, eng_dict, pl2.rack.getRack())
            word, w_coord = h.findHint()
        if word != "":

            x, y = w_coord[0]
            hint_window = Toplevel()
            hint_msg = Message(hint_window, text = "TRY: " + str(word).upper()+ "\n start at: " + str(x+1) +"," + str(y+1))
            hint_msg.grid(column =1 , row =1)
            close_button = Button(hint_window,text="OK")
            close_button.grid(column=2,row=2)
            close_button["command"]= lambda: hint_window.destroy()
        else:
            hint_window = Toplevel()
            hint_msg = Message(hint_window,
                               text="NO PROPER MOVE FOUND")
            hint_msg.grid(column=1, row=1)
            close_button = Button(hint_window, text="OK")
            close_button.grid(column=2, row=2)
            close_button["command"] = lambda: hint_window.destroy()




    def endGame(self,pl1,pl2):
        endG = EndGame(pl1,pl2,self.root,self.frame)
        endG.endWindow()
