from tkinter import *
from tkinter import messagebox as msb

# define a function that handle what to do when the button is clicked
def btn_hello_click():
    msb.showinfo("Hello", "Hello, Python!")

def btn_warning_click():
    msb.showwarning("Warning", "This is a warning message.")

def btn_error_click():
    msb.showerror("Error", "This is an error message.")

window = Tk()   # Create the application window
window.title("GUI Demo 02")   # Add a title to the window
window.geometry('400x300')   # Set the dimensions of the window

# create a button widget, set the 'callback' function to btn_hello_click
btn_hello = Button(window, text="Hello", command=btn_hello_click, width=20)
# padx: distance between the button and the left/right edges of the window
# pady: distance between the button and the top/bottom edges of the window
btn_hello.grid(row=0, column=0, padx=100, pady=20)

btn_warning = Button(window, text="Warning", width=20, command=btn_warning_click)
btn_warning.grid(row=1, column=0, padx=100, pady=20)

btn_error = Button(window, text="Error", width=20, command=btn_error_click)
btn_error.grid(row=2, column=0, padx=100, pady=20)

window.mainloop()