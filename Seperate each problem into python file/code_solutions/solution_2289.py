import os
import tkinter as tk
from tkinter import filedialog

def rename_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    os.chdir(path)
    os.rename('images', 'images_new')
    root.destroy()

rename_folder()

"""

import os
import tkinter as tk
from tkinter import filedialog