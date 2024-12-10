from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

### Event handlers ###
def txt_product_enter(event):
    # move the focus to the next widget
    txt_price.focus()

def txt_price_enter(event):
    # move the focus to the next widget
    cb_case.focus()
    calculate_bill()

def calculate_bill():
    price = float(txt_price.get())
    if case_var.get():  # if case is selected
        price += 10.0
    if pen_var.get():  # if pen is selected
        price += 25.0
    if film_var.get():  # if film is selected
        price += 5.0
    
    lbl_price.config(text=f"${price:.2f}")
    
#### GUI setup ####
window = create_window("GUI Demo Checkbox", 400, 300)

lbl_product = Label(window, text="Product:")
lbl_product.grid(row=0, column=0, padx=5, pady=5, sticky=E)

txt_product = Entry(window, width=20)
txt_product.grid(row=0, column=1, padx=5, pady=5, sticky=W)
txt_product.focus()
txt_product.bind("<Return>", txt_product_enter)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W)
txt_price.bind("<Return>", txt_price_enter)

lbl_accessories = Label(window, text="Accessories:")
lbl_accessories.grid(row=2, column=0, padx=5, pady=5, sticky=E)

case_var = BooleanVar()
case_var.set(False)
cb_case = Checkbutton(window, text="Case ($10.0)", variable=case_var, command=calculate_bill)
cb_case.grid(row=2, column=1, padx=5, pady=5, sticky=W)

pen_var = BooleanVar()
pen_var.set(False)
cb_pen = Checkbutton(window, text="Pen ($25.0)", variable=pen_var, command=calculate_bill)
cb_pen.grid(row=3, column=1, padx=5, pady=5, sticky=W)

film_var = BooleanVar()
film_var.set(False)
cb_film = Checkbutton(window, text="Protection Film ($5.0)", variable=film_var, command=calculate_bill)
cb_film.grid(row=4, column=1, padx=5, pady=5, sticky=W)

lbl_total = Label(window, text="Total:")
lbl_total.grid(row=5, column=0, padx=5, pady=5, sticky=E)

lbl_price = Label(window, text="$0")
lbl_price.grid(row=5, column=1, padx=5, pady=5, sticky=W)


#### Run the window ####
run(window)