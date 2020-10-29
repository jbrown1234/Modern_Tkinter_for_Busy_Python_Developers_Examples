# https://www.tcl.tk/man/tcl8.6/TkCmd/checkbutton.htm

# Yes, I know the widget is really called a check BUTTON, but I'm moving over from the
# world of Visual Studio and the same tools is referred to as a check BOX. I'll work on
# applying the correct terminology over time and adapt to the Tkinter naming.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Intro to CheckButtons")


def chk_a_action(*args):
    if chk_a_val.get() == 1:
        lbl_a_text.set("This is message A")
    else:
        lbl_a_text.set(" ")
        chk_all_val.set(0)
    return

def chk_b_action(*args):
    if chk_b_val.get() == 1:
        lbl_b_text.set("This is message B")
    else:
        lbl_b_text.set(" ")
        chk_all_val.set(0)
    return


def chk_c_action(*args):
    if chk_c_val.get() == 1:
        lbl_c_text.set("This is message C")
    else:
        lbl_c_text.set(" ")
        chk_all_val.set(0)
    return


def chk_all_action(*args):
    if chk_all_val.get() == 1:
        chk_a_val.set(1)
        chk_b_val.set(1)
        chk_c_val.set(1)
        #chk_a.invoke()
    else:
        chk_a_val.set(0)
        chk_b_val.set(0)
        chk_c_val.set(0)
        #chk_a.invoke()
    return


chk_a_val = IntVar()
chk_a_val.set(1)
lbl_a_text = StringVar()
lbl_a_text.set("This is message A")
a_flag = 1

chk_b_val = IntVar()
chk_b_val.set(1)
lbl_b_text = StringVar()
lbl_b_text.set("This is message B")

chk_c_val = IntVar()
chk_c_val.set(1)
lbl_c_text = StringVar()
lbl_c_text.set("This is message C")

chk_all_val = IntVar()
chk_all_val.set(0)

main_frame = ttk.Frame(root, padding="3 3 12 12", height=350, width=350)
main_frame.pack()
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))    # anchors to the root at the default position
root.columnconfigure(0, weight=1)   # helps with frame/app resizing on the fly
root.rowconfigure(0, weight=1)      # helps with frame/app resizing on the fly

chk_a = ttk.Checkbutton(main_frame, text="Display Message A", command=chk_a_action, variable=chk_a_val)\
    .grid(column=1, row=1, sticky=(N, E, S, W))
lbl_a = ttk.Label(main_frame, text="This is message A", textvariable=lbl_a_text).grid(column=2, row=1)

chk_b = ttk.Checkbutton(main_frame, text="Display Message B", command=chk_b_action, variable=chk_b_val)\
    .grid(column=1, row=2, sticky=(N, E, S, W))
lbl_b = ttk.Label(main_frame, text="This is message B", textvariable=lbl_b_text).grid(column=2, row=2)

chk_c = ttk.Checkbutton(main_frame, text="Display Message C", command=chk_c_action, variable=chk_c_val)\
    .grid(column=1, row=3, sticky=(N, E, S, W))
lbl_c = ttk.Label(main_frame, text="This is message C", textvariable=lbl_c_text).grid(column=2, row=3)

chk_all = ttk.Checkbutton(main_frame, text="Display All", command=chk_all_action, variable=chk_all_val)\
    .grid(column=1, row=4, sticky=(N, E, S, W))

root.mainloop()
