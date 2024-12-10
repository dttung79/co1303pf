from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

products = []
prices = []
quantities = []

### Event handlers ###

#### GUI setup ####
window = create_window("GUI Demo Listbox", 650, 300)

lbl_all_products = Label(window, text="All Products:")
lbl_all_products.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=2)

lst_products = Listbox(window, width=30, height=10)
lst_products.grid(row=1, column=0, padx=5, pady=5, sticky=W, columnspan=2, rowspan=4)

lbl_details = Label(window, text="Product Details:")
lbl_details.grid(row=0, column=2, padx=5, pady=5, sticky=W, columnspan=4)

lbl_name = Label(window, text="Name:")
lbl_name.grid(row=1, column=2, padx=5, pady=5, sticky=E)

txt_name = Entry(window, width=30)
txt_name.grid(row=1, column=3, padx=5, pady=5, sticky=W, columnspan=3)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=2, column=2, padx=5, pady=5, sticky=E)

txt_price = Entry(window, width=30)
txt_price.grid(row=2, column=3, padx=5, pady=5, sticky=W, columnspan=3)

lbl_quantity = Label(window, text="Quantity:")
lbl_quantity.grid(row=3, column=2, padx=5, pady=5, sticky=E)

txt_quantity = Entry(window, width=30)
txt_quantity.grid(row=3, column=3, padx=5, pady=5, sticky=W, columnspan=3)

btn_add = Button(window, text="Add", width=5)
btn_add.grid(row=4, column=3, padx=5, pady=5, sticky=W)

btn_edit = Button(window, text="Edit", width=5)
btn_edit.grid(row=4, column=4, padx=5, pady=5, sticky=W)

btn_delete = Button(window, text="Del", width=5)
btn_delete.grid(row=4, column=5, padx=5, pady=5, sticky=W)

btn_load = Button(window, text="Load", width=5)
btn_load.grid(row=5, column=0, padx=5, pady=5, sticky=W)

btn_save = Button(window, text="Save", width=5)
btn_save.grid(row=5, column=1, padx=5, pady=5, sticky=E)


#### run the main event loop ####
run(window)