from tkinter import *
from Board import *

class BoardVisual:


    def __init__(self, root, frame,board):
        self.bframe = frame
        self.root = root
        self.board = board
        self.initialize()
        self.bframe.grid(row=5, column=5)


    def initialize(self):
        for col in range(1, 16):
            label = Label(self.bframe, text=str(col))
            label.grid(row=0, column=col)
        for row in range(1, 16):
            label = Label(self.bframe, text=str(row))
            label.grid(row=row, column=0)



        for row in range(1, 16):
            for col in range(1, 16):
                button = Button(self.bframe, height=3, width=3, bg="bisque", fg="gray1", text=" ")
                button.grid(row=row, column=col)
                self.board[row - 1][col - 1] = button

        self.board[7][7]["bg"] = "salmon"
        self.board[7][7]["text"] = "♥"

        self.board[0][0]["bg"] = "light blue"
        self.board[0][0]["text"] = "W3"
        self.board[14][14]["bg"] = "light blue"
        self.board[14][14]["text"] = "W3"
        self.board[0][14]["bg"] = "light blue"
        self.board[0][14]["text"] = "W3"
        self.board[14][0]["bg"] = "light blue"
        self.board[14][0]["text"] = "W3"

        self.board[3][3]["bg"] = "pale green"
        self.board[3][3]["text"] = "W2"
        self.board[11][3]["bg"] = "pale green"
        self.board[11][3]["text"] = "W2"
        self.board[3][11]["bg"] = "pale green"
        self.board[3][11]["text"] = "W2"
        self.board[11][11]["bg"] = "pale green"
        self.board[11][11]["text"] = "W2"

        self.board[7][3]["bg"] = "pale violet red"
        self.board[7][3]["text"] = "L3"
        self.board[3][7]["bg"] = "pale violet red"
        self.board[3][7]["text"] = "L3"
        self.board[11][7]["bg"] = "pale violet red"
        self.board[11][7]["text"] = "L3"
        self.board[7][11]["bg"] = "pale violet red"
        self.board[7][11]["text"] = "L3"

        self.board[5][5]["bg"] = "plum2"
        self.board[5][5]["text"] = "L2"
        self.board[5][9]["bg"] = "plum2"
        self.board[5][9]["text"] = "L2"
        self.board[9][5]["bg"] = "plum2"
        self.board[9][5]["text"] = "L2"
        self.board[9][9]["bg"] = "plum2"
        self.board[9][9]["text"] = "L2"
