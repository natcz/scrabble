from Rack import *
turn = 1
word = ""
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
        global word
        def placeLetter(button,letter):
            button["text"] = str(letter).upper()

        if turn % 2 != 0:
            letter = pl1.rack.getRack()[ind]
            word += letter
        else:
            letter = pl2.rack.getRack()[ind]
            word += letter

        for row in range(15):
            for col in range(15):
                board[row][col]["command"] = lambda c=col, r=row:placeLetter(board[r][c],letter)


    def endTurn():
        global word
        print(word)
        word = ""
        print(word)


