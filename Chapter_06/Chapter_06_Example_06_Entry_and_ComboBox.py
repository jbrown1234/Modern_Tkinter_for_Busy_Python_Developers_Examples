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

cbo_fruits = ttk.Combobox(root, textvariable=cbo_variable) # .grid(column=1, row=1) # PROBLEM.... see not below
cbo_fruits.bind('<<ComboboxSelected>>', cbo_changed)
cbo_fruits['values'] = ['apple', 'banana', 'pineapple', 'rutabega', 'avacado', 'horse apple']   # the book showed how
                                                                                                # values were added with
                                                                                                # a tuple, but we can
                                                                                                # also use a list
cbo_fruits.grid(column=1, row=1)    # NOTE - if I put the grid assignment in the same line with the combo box definition
                                    # I get an error in assigning values to the combo box in a follow-up statement;
                                    # seems to throw the scope for a loop.
cbo_fruits.current()

lbl_selected = ttk.Label(root, textvariable=lbl_sel)
lbl_selected.grid(column=1, row=2)

txt_input = ttk.Entry(root, textvariable=txt_var)
txt_input.grid(column=2, row=3)
root.mainloop()

# For an interesting example on changing combo box values on-the-fly, see https://www.howtobuildsoftware.com/index.php/how-do/i20/python-3x-combobox-tkinter-how-do-you-populate-a-combobox-based-on-the-selection-of-another-combobox
