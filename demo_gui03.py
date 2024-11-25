from tkinter import *
from tkinter import messagebox as msb

from gui_util import create_window, run
def btn_copy_click():
    # get text from lbl_msg1
    s = lbl_msg1.cget("text")
    # copy to lbl_msg2
    lbl_msg2.config(text=s)

def btn_translate_click():
    lbl_msg2.config(text="Bonjour le monde!")
    
window = create_window("GUI Demo 03", 600, 300)

lbl_msg1 = Label(window, text="Hello, World!")
lbl_msg1.grid(row=0, column=0, padx=20, pady=20)

btn_copy = Button(window, text="Copy", width=20, command=btn_copy_click)
btn_copy.grid(row=0, column=1, padx=20, pady=20)

lbl_msg2 = Label(window, text="Python")
lbl_msg2.grid(row=0, column=2, padx=20, pady=20)

btn_translate = Button(window, text="Translate", width=20, command=btn_translate_click)
btn_translate.grid(row=1, column=1, padx=20, pady=20)

btn_exit = Button(window, text="Exit", width=20, command=window.quit)
btn_exit.grid(row=2, column=1, padx=20, pady=20)

run(window)