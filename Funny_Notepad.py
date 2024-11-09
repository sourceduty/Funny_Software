import tkinter as tk
from tkinter import messagebox
import random

# Sarcastic comments for saving
save_comments = [
    "Saving this? Bold move.",
    "Are you sure this is worth it?",
    "Masterpiece in the making? Probably.",
    "This better not be another grocery list."
]

# Random pun generator
pun_list = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I would avoid the sushi if I were you. It’s a little fishy.",
    "I’m reading a book on anti-gravity. It’s impossible to put down!"
]

def save_file():
    # Simulate saving a file with a sarcastic comment
    comment = random.choice(save_comments)
    messagebox.showinfo("Save File", f"File saved! {comment}")

def random_pun():
    # Display a random pun in the text box
    pun = random.choice(pun_list)
    text_box.insert(tk.END, f"\n\nPun Break: {pun}")

def ego_boost():
    compliments = [
        "You're the Hemingway of keyboard smashing!",
        "This draft is pure genius. Pulitzer material.",
        "If this isn't art, I don't know what is!"
    ]
    boost = random.choice(compliments)
    messagebox.showinfo("Ego Boost", boost)

def sarcastic_typo(event):
    # React to typos with a sarcastic message
    if event.char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]:
        comment = "Creative punctuation, I see. Nice touch!"
        messagebox.showinfo("Typo Detected", comment)

def erase_drama(event):
    # Dramatic reaction to backspace
    if event.keysym == "BackSpace":
        drama = random.choice([
            "Nooo... why me?!",
            "Another word bites the dust.",
            "Was it really so bad?"
        ])
        status_label.config(text=drama)

# Create main application window
root = tk.Tk()
root.title("Funny Notepad")
root.geometry("600x400")

# Text box
text_box = tk.Text(root, wrap="word", font=("Comic Sans MS", 12))
text_box.pack(expand=1, fill="both", padx=10, pady=10)

# Add key bindings for sarcasm
text_box.bind("<Key>", sarcastic_typo)
text_box.bind("<KeyPress-BackSpace>", erase_drama)

# Status label
status_label = tk.Label(root, text="Welcome to Funny Notepad!", font=("Arial", 10), fg="gray")
status_label.pack(side="bottom", fill="x")

# Button bar
button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x")

save_button = tk.Button(button_frame, text="Save File", command=save_file)
save_button.pack(side="left", padx=5)

pun_button = tk.Button(button_frame, text="Pun Generator", command=random_pun)
pun_button.pack(side="left", padx=5)

boost_button = tk.Button(button_frame, text="Ego Boost", command=ego_boost)
boost_button.pack(side="left", padx=5)

# Run the application
root.mainloop()
