from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

### Event handlers ###

#### GUI setup ####
window = create_window("GUI Demo Checkbox", 400, 300)

lbl_product = Label(window, text="Product:")
lbl_product.grid(row=0, column=0, padx=5, pady=5, sticky=E)

txt_product = Entry(window, width=20)
txt_product.grid(row=0, column=1, padx=5, pady=5, sticky=W)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W)

lbl_accessories = Label(window, text="Accessories:")
lbl_accessories.grid(row=2, column=0, padx=5, pady=5, sticky=E)

cb_case = Checkbutton(window, text="Case ($10.0)")
cb_case.grid(row=2, column=1, padx=5, pady=5, sticky=W)

cb_pen = Checkbutton(window, text="Pen ($25.0)")
cb_pen.grid(row=3, column=1, padx=5, pady=5, sticky=W)

cb_film = Checkbutton(window, text="Protection Film ($5.0)")
cb_film.grid(row=4, column=1, padx=5, pady=5, sticky=W)

lbl_total = Label(window, text="Total:")
lbl_total.grid(row=5, column=0, padx=5, pady=5, sticky=E)

lbl_price = Label(window, text="$0")
lbl_price.grid(row=5, column=1, padx=5, pady=5, sticky=W)


#### Run the window ####
run(window)