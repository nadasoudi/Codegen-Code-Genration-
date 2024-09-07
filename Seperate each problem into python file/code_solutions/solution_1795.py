import tkinter as tk

def change_border_color(event):
    color = event.widget.cget("bg")
    event.widget.config(bg=color)

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

frame.bind("<Button-1>", change_border_color)

frame.bind("<Configure>", change_border_color)

frame.bind("<FocusIn>",