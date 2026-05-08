import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_chars = lower + upper + digits + symbols
    
    # Set password length (defaulting to 12)
    password_length = 12
    
    # Generate a random password
    password = "".join(random.sample(all_chars, password_length))
    
    # Display the password in the entry box
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# --- UI Setup ---
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("350x200")
root.config(padx=20, pady=20)

# Instruction Label
label = tk.Label(text="Click the button to generate a secure password:", pady=10)
label.pack()

# Entry field to show the password
password_entry = tk.Entry(width=30, justify='center', font=("Arial", 12))
password_entry.pack(pady=10)

# Generate Button
generate_btn = tk.Button(text="GENERATE", command=generate_password, bg="#00a8ff", fg="white", font=("Arial", 10, "bold"), width=15)
generate_btn.pack(pady=10)

root.mainloop()