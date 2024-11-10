import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

def check_easter_egg(event=None):
    content = text_area.get(1.0, tk.END).strip()
    if "bunny" in content.lower():
        messagebox.showinfo("Easter Egg Found!", "🐇 You found the bunny! Hoppy coding! 🐇")

        # ASCII Bunny
        bunny = """
               (\_/)
               (o.o)
               (> <)
        """
        messagebox.showinfo("Bunny!", bunny)

# Set up the main application window
root = tk.Tk()
root.title("Easter Egg Notepad")
root.geometry("600x400")

# Create a text area
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH)

# Add event binding for Easter egg trigger
text_area.bind("<Return>", check_easter_egg)

# Create a menu bar
menu_bar = tk.Menu(root)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Set the menu bar
root.config(menu=menu_bar)

# Run the application
root.mainloop()
