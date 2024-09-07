import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple Calculator")

# Create a frame inside the root window
frame = ttk.Frame(root, padding="10 10 10")
frame.grid()

# Create a label widget inside the frame
label = ttk.Label(frame, text="Enter a number:")
label.grid(column=0, row=0)

# Create a entry widget inside the frame
entry =