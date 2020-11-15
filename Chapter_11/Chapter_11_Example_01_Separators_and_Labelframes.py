from tkinter import *
from tkinter import ttk
import pyautogui            # note that to get this to recognize you will need to install this package


def frame_a_rdo_click(*args):
    if rdoga.get() == 1:
        my_text_var1.set("Option 1")
    elif rdoga.get() == 2:
        my_text_var1.set("Option2")
    elif rdoga.get() == 3:
        my_text_var1.set("Option 3")
    return

def chk_a_action(*args):
    if chk_a_val.get() == 1:
        lbl_a_text.set("This is message A")
    else:
        lbl_a_text.set(" ")
    return

def chk_b_action(*args):
    if chk_b_val.get() == 1:
        lbl_b_text.set("This is message B")
    else:
        lbl_b_text.set(" ")
    return


def chk_c_action(*args):
    if chk_c_val.get() == 1:
        lbl_c_text.set("This is message C")
    else:
        lbl_c_text.set(" ")
    return

root = Tk()
root.title("Separators and Labelframes")

# Let's center our GUI on the display....
screen_width, screen_height = pyautogui.size()  # extract the width and height....

gui_width = 600                                     # define the GUI width
gui_height = 200                                    # define the GUI height
left_position = int((screen_width - gui_width)/2)       # cast to an int to avoid getting a float
top_position = int((screen_height - gui_height)/2)
geometry_string = "{0}x{1}+{2}+{3}".format(gui_width, gui_height, left_position, top_position)  # build the string that
                                                                                                # will define the size
                                                                                                # and placement...
root.geometry(geometry_string)
root.iconbitmap(r'py.ico')          # added a copy of the Python icon local to the script directory

rdoga = IntVar()
rdoga.set(1)
my_text_var1 = StringVar()
chk_a_val = IntVar()
chk_b_val = IntVar()
chk_c_val = IntVar()
lbl_a_text = StringVar()
lbl_b_text = StringVar()
lbl_c_text = StringVar()

# create a vertical separator and drop label frames (a.k.a., group boxes) on either side
sep_a = ttk.Separator(root, orient=VERTICAL)
grp_a = ttk.Labelframe(root, text='Group A', pad=(5, 5, 5, 5), height=400)
grp_b = ttk.Labelframe(root, text='Group B', pad=(5, 5, 5, 5))
sep_b = ttk.Separator(root, orient=HORIZONTAL)

# add some radio buttons to the Group A label frame - if nothing is within the label frame, it won't show
rdo_ga1 = ttk.Radiobutton(grp_a, text='First', variable=rdoga, value=1, command=frame_a_rdo_click, width=15, pad=(5,0,0,0))
rdo_ga2 = ttk.Radiobutton(grp_a, text='Second', variable=rdoga, value=2, command=frame_a_rdo_click, width=15, pad=(5,0,0,0))
rdo_ga3 = ttk.Radiobutton(grp_a, text='Third', variable=rdoga, value=3, command=frame_a_rdo_click, width=15, pad=(5,0,0,0))

# add some check buttons to the Group B label frame - if nothing is within the label frame, it won't show
chk_a = ttk.Checkbutton(grp_b, text="Display Message A", command=chk_a_action, variable=chk_a_val)
chk_b = ttk.Checkbutton(grp_b, text="Display Message B", command=chk_b_action, variable=chk_b_val)
chk_c = ttk.Checkbutton(grp_b, text="Display Message C", command=chk_c_action, variable=chk_c_val)
lbl_a = ttk.Label(grp_b, text="stuff", textvariable=lbl_a_text, width=15)
lbl_b = ttk.Label(grp_b, text="stuff", textvariable=lbl_b_text, width=15)
lbl_c = ttk.Label(grp_b, text="stuff", textvariable=lbl_c_text, width=15)

btn_a = ttk.Button(root, text="Ok")
lbl_alt = ttk.Label(root, text="General label...")

# grid up our controls on the main GUI....
grp_a.grid(column=0, row=0, sticky=(N, W))
rdo_ga1.grid(column=0, row=0, sticky=W)
rdo_ga2.grid(column=0, row=1, sticky=W)
rdo_ga3.grid(column=0, row=2, sticky=W)

# place the separator between the two label frames
sep_a.grid(column=1, row=0, sticky=(N, W, E, S))

grp_b.grid(column=2, row=0, sticky=(N, E))
chk_a.grid(column=0, row=0, sticky=(N, E, S, W))
chk_b.grid(column=0, row=1, sticky=(N, E, S, W))
chk_c.grid(column=0, row=2, sticky=(N, E, S, W))
lbl_a.grid(column=1, row=0, sticky=(N, E, S, W))
lbl_b.grid(column=1, row=1, sticky=(N, E, S, W))
lbl_c.grid(column=1, row=2, sticky=(N, E, S, W))

sep_b.grid(column=0, row=1, columnspan=4)   # For some reason, this is not showing up....

lbl_alt.grid(column=0, row=2, columnspan=3)
btn_a.grid(column=3, row=2, sticky=(N, W, E, S))

root.mainloop()
