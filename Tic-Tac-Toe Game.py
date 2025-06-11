import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x350")
        self.root.resizable(False, False)
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.label = tk.Label(self.root, text="Player X's Turn", font=("Arial", 14))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for i in range(9):
            button = tk.Button(self.frame, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 12), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def on_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.label.config(text=f"Player {self.current_player} Wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                self.label.config(text="It's a Draw!")
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                for i in (a, b, c):
                    self.buttons[i].config(bg="lightgreen")
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.label.config(text="Player X's Turn")
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")

# Launch the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
