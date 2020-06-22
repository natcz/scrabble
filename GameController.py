from Rack import *
from Board import *
from Letters import *
from tkinter import *
from CheckBoard import *
from collections import defaultdict as dd
from Word import *
from EndGame import *
from Hint import *
#global
turn = 1  #number of turns
good_first_word = False  #information about first move on the board success
Wcoordinates = dd()     #deafaultdict where key: coordinates of the letter (x,y) val: letter
coord = []              #coordinates of letters in the current placing word list of (x,y)
l = Letters()
eng_dict = l.makeDict() #english dictionary set
demoBoard = Board(15)
rack_indx = dd()        #deafultdict where key:letter    val:index in the rack

class GameController:

    def __init__(self,root,frame,sack,player1,player2):
        self.root = root
        self.sack = sack
        self.frame = frame
        self.pl1 = player1
        self.pl2 = player2


    def skip(self,scrLabel,scrL,turnLabel,rackButtons): #what happens when player hit the button SKIP
        global turn

        if turn % 2 == 0:
            scrLabel["text"] = str(self.pl1.name).upper() +"'S SCORE:"
            scrL["text"] = str(self.pl1.score)
            turnLabel["text"] = "IT'S " + str(self.pl1.name).upper() + "'S TURN"
            playerRack = self.pl1.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])
            turn += 1
        else:
            scrLabel["text"] = str(self.pl2.name).upper() + "'S SCORE:"
            scrL["text"] = str(self.pl2.score)
            turnLabel["text"] = "IT'S " + str(self.pl2.name).upper() + "'S TURN"
            playerRack = self.pl2.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])
            turn += 1



    def exchangeAll(self,rackButtons):   #what happens when player hit the button EXCHANGE ALL
        global turn

        if turn % 2 != 0:
            self.pl1.rack.exchangeAll()  #Rack() method
            playerRack = self.pl1.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])
        else:
            self.pl2.rack.exchangeAll()
            playerRack = self.pl2.rack.getRack()
            for i in range(len(rackButtons)):
                rackButtons[i]["text"] = str(playerRack[i])


    def exchangeOne(self,rackButtons,board,exAllButton,exOneButton,skipButton): #what happens when player hit the button EXCHANGE ONE
        def exOne(button,ind):
            if turn % 2 != 0:
                new_letter = self.pl1.rack.exchangeOne(ind)   # Rack() method
                button["text"] = str(new_letter).upper()
            else:
                new_letter = self.pl2.rack.exchangeOne(ind)
                button["text"] = str(new_letter).upper()
        def disableB(self,buttons,exAllButton,exOneButton,skipButton):     #making the letter button disabled after move
            for i in range(len(buttons)):
                buttons[i]["command"] = lambda x=i: self.makeMove(x, board,rackButtons,
                                                                  exAllButton,exOneButton,skipButton)


        for i in range(len(rackButtons)):
            rackButtons[i].config(command=lambda x=i: [exOne(rackButtons[x], x),disableB(self,rackButtons,
                                                                                         exAllButton,exOneButton,skipButton)])





    def makeMove(self,ind,board,rackButtons,exAllButton,exOneButton,skipButton): #placing tile on the board
        global rack_indx
        def placeLetter(button,row,col,letter):
            global coord
            global Wcoordinates
            button["text"] = str(letter).upper()
            Wcoordinates[(row, col)] = letter
            coord.append((row, col))
        #getting the letter out of the player's rack
        if turn % 2 != 0:
            letter = self.pl1.rack.getRack()[ind]
            rack_indx[letter] = ind
        else:
            letter = self.pl2.rack.getRack()[ind]
            rack_indx[letter] = ind
        #enable to place the letter (board tile text changing into letter)
        for row in range(15):
            for col in range(15):
                board[row][col]["command"] = lambda c=col, r=row:placeLetter(board[r][c],r,c,letter)
        #disable other functionalities
        rackButtons[ind]["state"] = "disabled"
        exAllButton["state"] = "disabled"
        exOneButton["state"] = "disabled"
        skipButton["state"] = "disabled"


    def undoMove(self,coords,board,rackButtons):  #in case of wrong move
        global demoBoard
        for i in range(len(coords)):        #letters out of the board
            board[coords[i][0]][coords[i][1]]["text"] = " "
            demoBoard.board[coords[i][0]][coords[i][1]] = "_"
        for i in range(len(rack_indx)):
            rackButtons[i]["state"] = "normal"


    def makeProperWord(self):  #making word from letters placed in current turn on the board
        global Wcoordinates, coord
        sameRow = True
        sameCol = True
        c = coord[0][1]
        r = coord[0][0]
        word = ""
        for pair in coord:  #checking if letters are in the same column or row
            if pair[0] != r:
                sameRow = False
            if pair[1] != c:
                sameCol = False
        if not sameRow and not sameCol:
            return ""
        elif sameRow:  #all the letters in the same row
            coord.sort(key=lambda x: x[1])
            for pair in coord:
                word += Wcoordinates[pair]
            return word
        else:          #all the letters in the same column
            coord.sort()
            for pair in coord:
                word += Wcoordinates[pair]
            return word



    def endTurn(self,scrLabel,scrL,turnLabel,rackButtons,            #when player hit END TURN button
                visualB,hintButton,exAllButton,exOneButton,skipButton):
        global coord,eng_dict,rack_indx,turn
        global Wcoordinates,demoBoard,good_first_word
        checkB = CheckBoard(demoBoard)
        proper_word = self.makeProperWord()
        w = Word(proper_word)

        for i in range(len(rackButtons)):     #making rack letters buttons enabled
            rackButtons[i]["state"] = "normal"

        if turn == 1 or not good_first_word:   #first word on the board

            if coord[0] == (7,7):               #checking  special placing
                if w.checkWord(eng_dict):
                    board_ok = True
                    good_first_word = True
                else:
                    board_ok = False     #board_ok true if placing the word is possible
            else:
                board_ok = False
        else:
            board_ok = checkB.checkBoard(eng_dict, proper_word, coord)

        if board_ok: #proper move
            demoBoard.boardUpdate(proper_word,coord)

            if turn % 2 != 0:
                for xy in coord:
                    l = Wcoordinates[xy]
                    self.pl1.rack.remove(l)
                    ind = rack_indx[l]
                    rackButtons[ind]["text"] = " "
                self.pl1.incScore(proper_word,Wcoordinates)

            else:
                for xy in coord:
                    l = Wcoordinates[xy]
                    self.pl2.rack.remove(l)
                    ind = rack_indx[l]
                    rackButtons[ind]["text"] = " "
                self.pl2.incScore(proper_word,Wcoordinates)

        else:   #not a proper move
            bad_wordWindow = Toplevel()
            if turn % 2 != 0:
                fail_msg = Message(bad_wordWindow,
                                   text="Not a proper move " + str(self.pl1.name).upper() + ". You've lost your chance")
            else:
                fail_msg = Message(bad_wordWindow,
                                   text="Not a proper move " + str(self.pl2.name).upper() + ". You've lost your chance")
            fail_msg.grid(row=1, column=1)
            ok_Button = Button(bad_wordWindow,text="OK",command=lambda: bad_wordWindow.destroy())
            ok_Button.grid(row=2, column=2)
            self.undoMove(coord,visualB,rackButtons)
        if self.pl1.score >= 50 or self.pl2.score >= 50 or self.sack.sack == []: #checking if the  game is over
            self.endGame()

        Wcoordinates = dd()
        coord = []
        rack_indx = dd()
        #refilling the rack
        if turn % 2 != 0:
            self.pl1.rack.fillRack()

        else:
            self.pl2.rack.fillRack()
        exAllButton["state"] = "normal"
        exOneButton["state"] = "normal"
        skipButton["state"] = "normal"
        hintButton["state"] = "normal"
        self.skip(scrLabel,scrL,turnLabel,rackButtons) #next turn

    def hint(self): #when player hit HINT button
        #finding hint
        if turn % 2 != 0:
            h = Hint(demoBoard,eng_dict,self.pl1.rack.getRack())
            word,w_coord = h.findHint()
        else:
            h = Hint(demoBoard, eng_dict, self.pl2.rack.getRack())
            word, w_coord = h.findHint()
        if word != "":   #found hint
            x, y = w_coord[0]
            hint_window = Toplevel()
            hint_msg = Message(hint_window)
            hint_msg["text"] = "TRY: " + str(word).upper()  + "\n start at: " + str(x+1) +"," + str(y+1)
            hint_msg.grid(column=1 , row=1)
            close_button = Button(hint_window,text="OK")
            close_button.grid(column=2,row=2)
            close_button["command"] = lambda: hint_window.destroy()
        else:      #no hint founded
            hint_window = Toplevel()
            hint_msg = Message(hint_window,
                               text="NO PROPER MOVE FOUND")
            hint_msg.grid(column=1, row=1)
            close_button = Button(hint_window, text="OK")
            close_button.grid(column=2, row=2)
            close_button["command"] = lambda: hint_window.destroy()


    def endGame(self):
        endG = EndGame(self.pl1, self.pl2, self.root)
        endG.endWindow()
