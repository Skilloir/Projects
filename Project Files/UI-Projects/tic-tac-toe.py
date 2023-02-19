import tkinter as tk

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("200x200")

        self.board = [[tk.Button(self, width=5, height=2, command=lambda row=i, col=j: self.play(row, col)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.board[i][j].grid(row=i, column=j)
                self.board[i][j].config(bg='white', fg='lightgreen')


        self.player = "X"

    def play(self, row, col):
        self.board[row][col].config(text=self.player)
        self.board[row][col]['state'] = 'disable'
        self.board[row][col].config(text=self.player, justify='center')
        self.check_win()
        self.player = "O" if self.player == "X" else "X"

    def check_win(self):
        pass

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
