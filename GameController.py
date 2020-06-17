from Rack import *
turn = 1
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


    def exchangeOne(pl1,pl2,rackButtons):
        def exOne(button,ind,pl1,pl2):
            if turn % 2 != 0:
                new_letter = pl1.rack.exchangeOne(ind)
                button.config(text= str(new_letter).upper())
            else:
                new_letter = pl2.rack.exchangeOne(ind)
                button.config(text=str(new_letter).upper())


        rackButtons[0].config(command=lambda: exOne(rackButtons[0],0,pl1,pl2))
        rackButtons[1].config(command=lambda: exOne(rackButtons[1], 1, pl1, pl2))
        rackButtons[2].config(command=lambda: exOne(rackButtons[2], 2, pl1, pl2))
        rackButtons[3].config(command=lambda: exOne(rackButtons[3], 3, pl1, pl2))
        rackButtons[4].config(command=lambda: exOne(rackButtons[4], 4, pl1, pl2))
        rackButtons[5].config(command=lambda: exOne(rackButtons[5], 5, pl1, pl2))
        rackButtons[6].config(command=lambda: exOne(rackButtons[6], 6, pl1, pl2))







