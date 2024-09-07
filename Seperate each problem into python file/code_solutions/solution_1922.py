import tkinter as tk
from tkinter import ttk

def button_click(number):
    print(f"Button {number} was clicked.")

def button_clear():
    print("Button 1 was clicked.")
    button_number1.configure(state="normal")
    button_number1.delete(0, tk.END)
    button_number1.configure(state="disabled")

def button_equal():
    print("Button 2 was clicked.")
    button_number