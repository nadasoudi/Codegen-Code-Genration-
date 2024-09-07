import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Scientific Calculator")
    root.geometry("300x300")
    root.resizable(False, False)
    root.configure(bg="white")
    
    # Create a label widget
    label = ttk.Label(root, text="Scientific Calculator", font=("Arial", 20))
    label.pack(pady=20)