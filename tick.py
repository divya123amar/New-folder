import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 24), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)

        self.window.mainloop()

    def on_button_click(self, row, col):
        index = 3 * row + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_winner(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tie", "The game is a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_button(self, row, col):
        index = 3 * row + col
        button_text = self.board[index]
        buttons = self.window.grid_slaves()
        for button in buttons:
            if button.grid_info()["row"] == row and button.grid_info()["column"] == col:
                button.config(text=button_text, state=tk.DISABLED)

    def check_winner(self, row, col):
        # Check the row
        if all(self.board[row * 3 + i] == self.current_player for i in range(3)):
            return True
        # Check the column
        if all(self.board[i * 3 + col] == self.current_player for i in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.board[i * 3 + i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i * 3 + (2 - i)] == self.current_player for i in range(3)):
            return True
        return False

    def reset_board(self):
        self.current_player = "X"
        self.board = [""] * 9
        buttons = self.window.grid_slaves()
        for button in buttons:
            button.config(text="", state=tk.NORMAL)

if __name__ == "__main__":
    game = TicTacToe()
