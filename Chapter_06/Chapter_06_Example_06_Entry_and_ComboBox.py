# https://www.tcl.tk/man/tcl8.6/TkCmd/entry.htm
# https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_combobox.htm

from tkinter import *
from tkinter import ttk


def cbo_changed(*args):
    lbl_sel.set(cbo_variable.get())
    if "apple" in cbo_variable.get():
        txt_var.set(lbl_sel.get())
    else:
        txt_input.delete(0, 'end')
        txt_input.insert(0, "boring...")
    return

root = Tk()
root.title("Intro to Entry and Combo Boxes")
root['width'] = 400
root['height'] = 300

cbo_variable = StringVar()
lbl_sel = StringVar()
txt_var = StringVar()
#cbo_variable.set()

cbo_fruits = ttk.Combobox(root, textvariable=cbo_variable)
cbo_fruits.bind('<<ComboboxSelected>>', cbo_changed)
cbo_fruits['values'] = ('apple', 'banana', 'pineapple', 'rutabega', 'avacado')
cbo_fruits.grid(column=1, row=1)

lbl_selected = ttk.Label(root, textvariable=lbl_sel)
lbl_selected.grid(column=1, row=2)

txt_input = ttk.Entry(root, textvariable=txt_var)
txt_input.grid(column=2, row=3)
root.mainloop()
