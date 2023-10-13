import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)

root = tk.Tk()
root.title("File Selection")

button = tk.Button(root, text="Select File", command=select_file)
button.pack()

root.mainloop()