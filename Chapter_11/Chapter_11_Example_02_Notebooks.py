from tkinter import *
from tkinter import ttk
import pyautogui            # note that to get this to recognize you will need to install this package

root = Tk()
root.title("Notebooks with Separators")
root.iconbitmap(r'py.ico')          # added a copy of the Python icon local to the script directory

# Add the first notebook and populate buttons on each of the enclosed frames...
ntb_a = ttk.Notebook(root, width=200, height=50, pad=(5, 5, 5, 5))
frm_a1 = ttk.Frame(ntb_a)
ntb_a.add(frm_a1, text='Tab 1')
frm_a2 = ttk.Frame(ntb_a)
ntb_a.add(frm_a2, text='Tab 2')

btn_a = ttk.Button(frm_a1, text="Button A")
btn_b = ttk.Button(frm_a2, text="Button B")

# Add the second notebook and populate checkboxes on each of the enclosed frames...
ntb_b = ttk.Notebook(root, width=200, height=50, pad=(5, 5, 5, 5))
frm_b1 = ttk.Frame(ntb_b)
ntb_b.add(frm_b1, text="Tab 3")
frm_b2 = ttk.Frame(ntb_b)
ntb_b.add(frm_b2, text="Tab 4")

chk_a = ttk.Checkbutton(frm_b1, text="Check A")
chk_b = ttk.Checkbutton(frm_b2, text="Check B")

sep_a = ttk.Separator(root, orient=VERTICAL)
sep_b = ttk.Separator(root, orient=HORIZONTAL)

ntb_c = ttk.Notebook(root, width=400, height=50, pad=(5, 5, 5, 5))
frm_c1 = ttk.Frame(ntb_c)
ntb_c.add(frm_c1, text="Tab 5")
frm_c2 = ttk.Frame(ntb_c)
ntb_c.add(frm_c2, text="Tab 6")
frm_c3 = ttk.Frame(ntb_c)
ntb_c.add(frm_c3, text="Tab 7")
frm_c4 = ttk.Frame(ntb_c)
ntb_c.add(frm_c4, text="Tab 8")

lbl_a = ttk.Label(frm_c1, text="Label A")
lbl_b = ttk.Label(frm_c2, text="Label B")
lbl_c = ttk.Label(frm_c3, text="Label C")
lbl_d = ttk.Label(frm_c4, text="Label D")

# Grid up our widgets....
ntb_a.grid(column=0, row=0)
btn_a.grid(column=0, row=0)
btn_b.grid(column=0, row=0)

sep_a.grid(column=1, row=0, sticky=(N, W, E, S))

ntb_b.grid(column=2, row=0)
chk_a.grid(column=0, row=0)
chk_b.grid(column=0, row=0)

sep_b.grid(column=0, row=1, columnspan=3)

ntb_c.grid(column=0, row=2, columnspan=3)
lbl_a.grid(column=0, row=0)
lbl_b.grid(column=0, row=0)
lbl_c.grid(column=0, row=0)
lbl_d.grid(column=0, row=0)

# Let's center our GUI on the display....
gui_width = root.winfo_width()  # extract the width and height....
gui_height = root.winfo_height()

# Alternatives to the above...
# getting screen's width in pixels
screen_width = root.winfo_screenwidth()

# getting screen's height in pixels
screen_height = root.winfo_screenheight()

left_position = int((screen_width - gui_width)/2)       # cast to an int to avoid getting a float
top_position = int((screen_height - gui_height)/2)
geometry_string = "+{0}+{1}".format(left_position, top_position)  # build the string that
                                                                                                # will define the size
                                                                                                # and placement...
# Let the GUI grow on its own, but position in the center....
root.geometry(geometry_string)

root.mainloop()