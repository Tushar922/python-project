# I used tkinter module you can also use pygame
import tkinter as tk

# creating class
class TicTacToe:
    # a Constructer in python
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.buttons = []
        # we used here a for loop
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 40), width=3, height=1,
                command=lambda r=i, c=j: self.button_click(r, c))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.current_player = "X"

        # programs main loop
        self.window.mainloop()

        # function for setting buttons logic
    def button_click(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = self.current_player
            self.check_winner()
            self.switch_player()

        # for checking winner 
    def check_winner(self):
        for i in range(3):
            if all(self.buttons[i][j]["text"] == self.current_player for j in range(3)):
                self.declare_winner()
            if all(self.buttons[j][i]["text"] == self.current_player for j in range(3)):
                self.declare_winner()
        if all(self.buttons[i][i]["text"] == self.current_player for i in range(3)):
            self.declare_winner()
        if all(self.buttons[i][2-i]["text"] == self.current_player for i in range(3)):
            self.declare_winner()

        # this function will declare who is winner
    def declare_winner(self):
        winner_label = tk.Label(self.window, text=f"{self.current_player} wins!", font=("Arial", 20))
        winner_label.grid(row=3, columnspan=3)

        # for switching player
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
# __name__ is the name of the python module into a special variable
# __main__ is the name of the environment where top-level code is run.
#  checks whether the current script is being run as the main program 
if __name__ == "__main__":
    game = TicTacToe()
# have a great day