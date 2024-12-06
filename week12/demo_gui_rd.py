from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

#### Event handlers ####
def txt_price_focus_out(event):
    calculate_bill()

def calculate_bill():
    price = float(txt_price.get())
    delivery_type = delivery_var.get()
    if delivery_type == 1:
        bill = price
    elif delivery_type == 2:
        bill = price + 2.0
    else:
        bill = price + 3.0

    lbl_bill.config(text=f"${bill:.2f}")

#### GUI setup ####
window = create_window("GUI Demo 05", 400, 300)

lbl_product = Label(window, text="Product:")
lbl_product.grid(row=0, column=0, padx=10, pady=10, sticky=W)

txt_product = Entry(window, width=20)
txt_product.grid(row=0, column=1, padx=10, pady=10, sticky=W)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=1, column=0, padx=10, pady=10, sticky=W)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, padx=10, pady=10, sticky=W)
txt_price.bind("<FocusOut>", txt_price_focus_out)

lbl_delivery = Label(window, text="Delivery:")
lbl_delivery.grid(row=2, column=0, padx=10, pady=10, sticky=W)

delivery_var = IntVar()
delivery_var.set(1)
rd_normal = Radiobutton(window, text="Normal (Free)", value=1, 
                        variable=delivery_var, command=calculate_bill)
rd_normal.grid(row=2, column=1, padx=10, pady=10, sticky=W)

rd_express = Radiobutton(window, text="Express ($2.0)", value=2, 
                         variable=delivery_var, command=calculate_bill)
rd_express.grid(row=3, column=1, padx=10, pady=10, sticky=W)

rd_immediate = Radiobutton(window, text="Immediate ($3.0)", value=3, 
                           variable=delivery_var, command=calculate_bill)
rd_immediate.grid(row=4, column=1, padx=10, pady=10, sticky=W)

lbl_total = Label(window, text="Total:")
lbl_total.grid(row=5, column=0, padx=10, pady=10, sticky=W)

lbl_bill = Label(window, text="$0")
lbl_bill.grid(row=5, column=1, padx=10, pady=10, sticky=W)


#### Run the application ####
run(window)