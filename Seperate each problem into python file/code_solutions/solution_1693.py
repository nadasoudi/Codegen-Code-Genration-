import tkinter as tk

def change_bg_color(event):
    print("Background color changed")
    color_var.set(color_var.get() + 1)
    color_var.trace("w", change_bg_color)

color_var = tk.IntVar()
color_var.set(0)
color_label = tk.Label(text="Background color:", font=("Arial", 12))
color_label.pack()
color_