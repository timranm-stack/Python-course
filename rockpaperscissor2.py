import random
import tkinter as tk
from tkinter import messagebox

# Core Game Logic Function
def play_round(user_choice):
    global user_score, computer_score
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    # Update choices on the interface
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    
    # Determine the winner using conditional statements
    if user_choice == computer_choice:
        result = "It's a Tie!"
        result_label.config(text=result, fg="gray")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win this round!"
        user_score += 1
        result_label.config(text=result, fg="green")
    else:
        result = "Computer Wins this round!"
        computer_score += 1
        result_label.config(text=result, fg="red")
        
    # Update score display
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

# Function to reset the game state
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    comp_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Make your move!", fg="black")
    score_label.config(text="Score -> You: 0 | Computer: 0")

# Initialize Tkinter Window
root = tk.Tk()
root.title("Rock Paper Scissors GUI")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# Initialize global scores
user_score = 0
computer_score = 0

# Header Title Label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=15)

# Selection Frame for Action Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Game Action Buttons using a loop for layout organization
actions = [("Rock", "#e74c3c"), ("Paper", "#3498db"), ("Scissors", "#2ecc71")]
for action, color in actions:
    btn = tk.Button(
        button_frame, 
        text=action, 
        font=("Arial", 12, "bold"), 
        width=10, 
        bg=color, 
        fg="white",
        command=lambda c=action: play_round(c)
    )
    btn.pack(side=tk.LEFT, padx=10)

# Display Labels for Results
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12), bg="#f0f0f0")
comp_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=15)

score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 10), command=reset_game, bg="#95a5a6", fg="white")
reset_btn.pack(pady=15)

# Execute main Tkinter loop
root.mainloop()