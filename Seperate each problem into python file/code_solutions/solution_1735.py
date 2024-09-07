import tkinter as tk

def add_border(button, color):
    button.config(bg=color)

def main():
    root = tk.Tk()
    root.title("Add Border")
    root.geometry("300x300")
    button = tk.Button(root, text="Add Border", command=add_border)
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    main