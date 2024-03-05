import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

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
    
    user_image = Image.open(f"{choice}.png")
    computer_image = Image.open(f"{computer_choice}.png")

    user_image = user_image.resize((150, 150), Image.ANTIALIAS)
    computer_image = computer_image.resize((150, 150), Image.ANTIALIAS)

    user_image = ImageTk.PhotoImage(user_image)
    computer_image = ImageTk.PhotoImage(computer_image)

    user_label.config(image=user_image)
    computer_label.config(image=computer_image)

    user_label.image = user_image
    computer_label.image = computer_image

    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {computer_choice}\n\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Load default images
default_user_image = Image.open("default.png")
default_computer_image = Image.open("default.png")

default_user_image = default_user_image.resize((150, 150), Image.ANTIALIAS)
default_computer_image = default_computer_image.resize((150, 150), Image.ANTIALIAS)

default_user_image = ImageTk.PhotoImage(default_user_image)
default_computer_image = ImageTk.PhotoImage(default_computer_image)

# Create labels for displaying hand gestures
user_label = tk.Label(window, image=default_user_image)
computer_label = tk.Label(window, image=default_computer_image)

user_label.pack(pady=10)
computer_label.pack(pady=10)

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(window, text="Rock", command=lambda: on_choice_button_click("rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: on_choice_button_click("paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: on_choice_button_click("scissors"))

rock_button.pack(pady=1)
