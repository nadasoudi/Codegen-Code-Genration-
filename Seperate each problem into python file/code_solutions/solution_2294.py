import tkinter as tk

def get_selected_row(event):
    try:
        global selected_tuple
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        e1.delete(0, tk.END)
        e1.insert(tk.END, selected_tuple[1])
        e2.delete(0, tk.END)
        e2.insert(tk.