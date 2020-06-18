from Rack import *
from Board import *
from Letters import *
from CheckBoard import *
turn = 1
Wcoordinates = dict()
coord = []
l = Letters()
eng_dict = l.makeDict()
demoBoard = Board(eng_dict,15)

class GameController:

    def skip(pl1,pl2,scrLabel,scrL,turnLabel,rackButtons):
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



    def exchangeAll(pl1,pl2,rackButtons):
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


    def exchangeOne(pl1,pl2,rackButtons,board):
        def exOne(button,ind,pl1,pl2):
            if turn % 2 != 0:
                new_letter = pl1.rack.exchangeOne(ind)
                button.config(text= str(new_letter).upper())
            else:
                new_letter = pl2.rack.exchangeOne(ind)
                button.config(text=str(new_letter).upper())
        def disableB(buttons):
            for i in range(len(buttons)):
                buttons[i]["command"] = lambda x=i: GameController.makeMove(pl1,pl2,x, board)


        for i in range(len(rackButtons)):
            rackButtons[i].config(command=lambda x=i: [exOne(rackButtons[x], x, pl1, pl2),disableB(rackButtons)])





    def makeMove(pl1,pl2,ind,board):

        def placeLetter(button,row,col,letter):
            global coord
            global Wcoordinates
            button["text"] = str(letter).upper()
            Wcoordinates[(row, col)] = letter
            coord.append((row, col))

        if turn % 2 != 0:
            letter = pl1.rack.getRack()[ind]

        else:
            letter = pl2.rack.getRack()[ind]



        for row in range(15):
            for col in range(15):
                board[row][col]["command"] = lambda c=col, r=row:placeLetter(board[r][c],r,c,letter)


    def endTurn():
        global coord,eng_dict
        global Wcoordinates,demoBoard
        checkB = CheckBoard(demoBoard)
        def makeProperWord():
            global Wcoordinates,coord
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
            if not sameRow  and not sameCol:
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

        proper_word = makeProperWord()
        checkB.checkBoard(eng_dict, proper_word, coord)


        Wcoordinates = dict()
        coord = []



