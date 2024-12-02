from tkinter import *
window = Tk()   # Create the application window
window.title("GUI Demo")   # Add a title to the window
window.geometry('400x300')   # Set the dimensions of the window

# create a label widget with the text "Hello"
lbl_hello = Label(window, text="Hello")
# set position of the label on the window
lbl_hello.grid(row=0, column=0)

# create a label widget with the text "Python"
lbl_python = Label(window, text="Python")
lbl_python.grid(row=1, column=1)

window.mainloop()   # Run the application