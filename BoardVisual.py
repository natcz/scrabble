from tkinter import *


class BoardVisual:

    def __init__(self, root, frame):
        self.bframe = frame
        self.root = root
        self.initialize()

    def initialize(self):
        for col in range(1, 16):
            label = Label(self.bframe, text=str(col))
            label.grid(row=0, column=col)
        for row in range(1, 16):
            label = Label(self.bframe, text=str(row))
            label.grid(row=row, column=0)

        board = [['' for columns in range(15)] for rows in range(15)]

        for row in range(1, 16):
            for col in range(1, 16):
                button = Button(self.bframe, height=3, width=3, bg="bisque", fg="gray1", text=" ")
                button.grid(row=row, column=col)
                board[row - 1][col - 1] = button

        board[7][7]["bg"] = "salmon"
        board[7][7]["text"] = "♥"

        board[0][0]["bg"] = "light blue"
        board[0][0]["text"] = "W3"
        board[14][14]["bg"] = "light blue"
        board[14][14]["text"] = "W3"
        board[0][14]["bg"] = "light blue"
        board[0][14]["text"] = "W3"
        board[14][0]["bg"] = "light blue"
        board[14][0]["text"] = "W3"

        board[3][3]["bg"] = "pale green"
        board[3][3]["text"] = "W2"
        board[11][3]["bg"] = "pale green"
        board[11][3]["text"] = "W2"
        board[3][11]["bg"] = "pale green"
        board[3][11]["text"] = "W2"
        board[11][11]["bg"] = "pale green"
        board[11][11]["text"] = "W2"

        board[7][3]["bg"] = "pale violet red"
        board[7][3]["text"] = "L3"
        board[3][7]["bg"] = "pale violet red"
        board[3][7]["text"] = "L3"
        board[11][7]["bg"] = "pale violet red"
        board[11][7]["text"] = "L3"
        board[7][11]["bg"] = "pale violet red"
        board[7][11]["text"] = "L3"

        board[5][5]["bg"] = "plum2"
        board[5][5]["text"] = "L2"
        board[5][9]["bg"] = "plum2"
        board[5][9]["text"] = "L2"
        board[9][5]["bg"] = "plum2"
        board[9][5]["text"] = "L2"
        board[9][9]["bg"] = "plum2"
        board[9][9]["text"] = "L2"
