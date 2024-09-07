import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Python Code")
    root.configure(background="white")
    label = tk.Label(root, text="Enter the tab size", bg="white", fg="black")
    label.pack()
    label.configure(font=("Courier", 20))
    label.configure(width=20