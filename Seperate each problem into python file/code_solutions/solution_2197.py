import tkinter as tk
import PIL.Image as Image

def resize_image(image, width=None, height=None):
    if width is None:
        width = image.size[0]
    if height is None:
        height = image.size[1]
    new_image = image.resize((width, height))
    return new_image

def main():
    root = tk.Tk()
    root.title("Resize Image")
    root