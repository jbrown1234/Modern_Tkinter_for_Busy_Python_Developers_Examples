# https://www.tcl.tk/man/tcl8.6/TkCmd/radiobutton.htm

# This example creates two frames where two separate sets of radio buttons are grouped. We show
# how the user might independently coordinate behaviors and interact with the operator.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Intro to RadioButtons")


def frame_a_rdo_click(*args):
    if var1.get() == "Opt 1":
        my_text_var1.set("Option 1")
    elif var1.get() == "Opt 2":
        my_text_var1.set("Option 2")
    elif var1.get() == "Opt 3":
        my_text_var1.set("Option 3")
    return


def frame_b_rdo_click(*args):
    if var2.get() == 1:
        my_text_var2.set("Option 1")
    elif var2.get() == 2:
        my_text_var2.set("Option 2")
    elif var2.get() == 3:
        my_text_var2.set("Option 3")
    return


var1 = StringVar()
var1.set("Default")
var2 = IntVar()
var2.set(1)
my_text_var1 = StringVar()
my_text_var1.set("Default")
my_text_var2 = StringVar()
my_text_var2.set("Other")

frame_a = ttk.Frame(root, padding="3 3 12 12", height=350, width=350)
frame_a.grid(column=1, row=1, sticky=(N, W, E, S))    # anchors to the root at the default position
s = ttk.Style()
s.configure('My.TFrame', background='#81F7BE')
frame_a.configure(style='My.TFrame')
frame_a['relief'] = 'groove'        # how do you want your frame to appear on the screen - play with
                                    # settings like flat (default, raised, sunken, solid, ridge, groove
frame_a['borderwidth'] = 50

frame_b = ttk.Frame(root, padding="3 3 12 12", height=350, width=350)
frame_b.grid(column=2, row=1, sticky=(N, W, E, S))    # anchors to the root at the default position
s2 = ttk.Style()
s2.configure('My.TFrame', background='#81F7BE')
frame_b.configure(style='My.TFrame')
frame_b['relief'] = "sunken"
frame_b['borderwidth'] = 50

rdo_fa1 = ttk.Radiobutton(frame_a, text="Option 1", variable=var1, value="Opt 1", command=frame_a_rdo_click).grid(column=1, row=1)
rdo_fa2 = ttk.Radiobutton(frame_a, text="Option 2", variable=var1, value="Opt 2", command=frame_a_rdo_click).grid(column=1, row=2)
rdo_fa3 = ttk.Radiobutton(frame_a, text="Option 3", variable=var1, value="Opt 3", command=frame_a_rdo_click).grid(column=1, row=3)
lbl_fa = ttk.Label(frame_a, textvariable=my_text_var1).grid(column=1, row=5)

rdo_fb1 = ttk.Radiobutton(frame_b, text="Option 1", variable=var2, value=1, command=frame_b_rdo_click).grid(column=1, row=1)
rdo_fb2 = ttk.Radiobutton(frame_b, text="Option 2", variable=var2, value=2, command=frame_b_rdo_click).grid(column=1, row=2)
rdo_fb3 = ttk.Radiobutton(frame_b, text="Option 3", variable=var2, value=3, command=frame_b_rdo_click).grid(column=1, row=3)
lbl_fb = ttk.Label(frame_b, textvariable=my_text_var2).grid(column=1, row=5)

root.mainloop()