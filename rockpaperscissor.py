import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = f"It's a tie! Both chose {user_choice}."
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! {user_choice} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice} beats {user_choice}."
    
    # Update the result label
    result_label.config(text=result)

# --- UI Setup ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Title Label
tk.Label(root, text="Choose your move:", font=("Arial", 14, "bold"), pady=20).pack()

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Result Display
result_label = tk.Label(root, text="Good luck!", font=("Arial", 12), fg="blue", pady=30)
result_label.pack()

root.mainloop()