import tkinter as tk

def click_button(event):
    print(event.x, event.y)

root = tk.Tk()

button = tk.Button(root, text="Click Me", command=click_button)
button.pack()

root.mainloop()

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_