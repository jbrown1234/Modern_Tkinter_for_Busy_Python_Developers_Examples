# https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_spinbox.htm

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Spinboxes...")


def spn_change(*args):
    lbl_a_var.set("The value in the spinbox is {0}".format(spn_a_var.get()))


def spn_b_change(*args):
    lbl_b_var.set("{0} I will jump {1} times".format(spn_b_var.get(), spn_a_var.get()))


spn_a_var = StringVar()
lbl_a_var = StringVar()
spn_b_var = StringVar()
lbl_b_var = StringVar()

# create the widgets to add...
spn_a = Spinbox(root, from_=0, to=100, textvariable=spn_a_var, width=10, command=spn_change)
lbl_a = ttk.Label(root, text="", width=30, textvariable=lbl_a_var)
spn_b = Spinbox(root, textvariable=spn_b_var, width=10, command=spn_b_change)
spn_b['values'] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
lbl_b = ttk.Label(root, text="", width=30, textvariable=lbl_b_var)

# place our widgets on the grid...
spn_a.grid(column=0, row=0, sticky=(W,E))
lbl_a.grid(column=1, row=0, sticky=(W,E))
spn_b.grid(column=0, row=1, sticky=(W,E))
lbl_b.grid(column=1, row=1, sticky=(W,E))


root.mainloop()
