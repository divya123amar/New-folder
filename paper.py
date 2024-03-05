import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "You lose!"

def on_choice_button_click(choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {computer_choice}\n\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(window, text="Rock", command=lambda: on_choice_button_click("rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: on_choice_button_click("paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: on_choice_button_click("scissors"))

# Pack the buttons into the window
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Start the main event loop
window.mainloop()
