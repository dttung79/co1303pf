from tkinter import *

def create_window(title, width, height):
    window = Tk()   # Create the application window
    window.title(title)   # Add a title to the window
    window.geometry(f'{width}x{height}')   # Set the dimensions of the window
    return window

def run(window):
    window.mainloop()   # Run the application