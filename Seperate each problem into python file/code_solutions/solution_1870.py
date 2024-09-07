import tkinter as tk

def change_border(event):
    print("Border changed")
    
    # Create a Tkinter window
    window = tk.Tk()
    
    # Create a Tkinter canvas
    canvas = tk.Canvas(window, width=200, height=200)
    canvas.pack()
    
    # Create a Tkinter Label
    label = tk.Label(window, text="Hello World")
    label.pack()