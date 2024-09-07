import tkinter as tk

def add_padding(widget, padx, pady):
    widget.grid_configure(padx=padx, pady=pady)

root = tk.Tk()

widget = tk.Label(root, text="Hello World")
widget.grid(row=0, column=0)

add_padding(widget, 10, 10)

root.mainloop()

"""

from tkinter import