from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run
def calculate(op):
    a = int(txt_a.get())
    b = int(txt_b.get())
    txt_result.delete(0, END)
    if op == "+":
        txt_result.insert(0, a + b)
    elif op == "-":
        txt_result.insert(0, a - b)
    elif op == "*":
        txt_result.insert(0, a * b)
    elif op == "/":
        txt_result.insert(0, a / b)

def btn_add_click():
    calculate("+")

def btn_sub_click():
    calculate("-")

def btn_mul_click():
    calculate("*")

def btn_div_click():
    calculate("/")

window = create_window("GUI Demo 05", 400, 300)

lbl_a = Label(window, text="Enter a:")
lbl_a.grid(row=0, column=0, padx=10, pady=10)

txt_a = Entry(window, width=20)
txt_a.grid(row=0, column=1, padx=10, pady=10, columnspan=4)

lbl_b = Label(window, text="Enter b:")
lbl_b.grid(row=1, column=0, padx=10, pady=10)

txt_b = Entry(window, width=20)
txt_b.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

btn_add = Button(window, text="+", command=btn_add_click)
btn_add.grid(row=2, column=1, padx=2, pady=10)

btn_sub = Button(window, text="-", command=btn_sub_click)
btn_sub.grid(row=2, column=2, padx=2, pady=10)

btn_mul = Button(window, text="*", command=btn_mul_click)
btn_mul.grid(row=2, column=3, padx=2, pady=10)

btn_div = Button(window, text="/", command=btn_div_click)
btn_div.grid(row=2, column=4, padx=2, pady=10)

lbl_result = Label(window, text="Result:")
lbl_result.grid(row=3, column=0, padx=10, pady=10)

txt_result = Entry(window, width=20)
txt_result.grid(row=3, column=1, padx=10, pady=10, columnspan=4)

run(window)