from tkinter import *
from tkinter import messagebox as msb

from gui_util import create_window, run
def btn_copy_click():
    # get text from txt_msg1
    s = txt_msg1.get()
    # copy to lbl_msg2
    txt_msg2.delete(0, END)
    txt_msg2.insert(0, s)

def btn_translate_click():
    txt_msg2.delete(0, END)
    txt_msg2.insert(0, "Bonjour le monde!")
    
window = create_window("GUI Demo 03", 600, 300)

txt_msg1 = Entry(window, text="Hello, World!")
txt_msg1.grid(row=0, column=0, padx=20, pady=20)

btn_copy = Button(window, text="Copy", width=20, command=btn_copy_click)
btn_copy.grid(row=0, column=1, padx=20, pady=20)

txt_msg2 = Entry(window, text="Python")
txt_msg2.grid(row=0, column=2, padx=20, pady=20)

btn_translate = Button(window, text="Translate", width=20, command=btn_translate_click)
btn_translate.grid(row=1, column=1, padx=20, pady=20)

btn_exit = Button(window, text="Exit", width=20, command=window.quit)
btn_exit.grid(row=2, column=1, padx=20, pady=20)

run(window)