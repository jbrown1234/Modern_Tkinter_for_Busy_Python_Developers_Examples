from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3, 3, 12, 12)) # add padding values to the edges of the frame...

frame = ttk.Frame(content, borderwidth=5, relief='sunken', width=200, height=100)
lbl_name = ttk.Label(content, text="Name")
txt_name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

chk_one = ttk.Checkbutton(content, text="one", variable=onevar, onvalue=True)
chk_two = ttk.Checkbutton(content, text="two", variable=twovar, onvalue=True)
chk_three = ttk.Checkbutton(content, text="three", variable=threevar, onvalue=True)
btn_okay = ttk.Button(content, text="OK")
btn_cancel = ttk.Button(content, text="Cancel")

# Now let's do some control organization...
content.grid(column=0, row=0, sticky=(N, S, E, W))   # stretch the frame to fit the space it's defined to fill
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))    # same as above
lbl_name.grid(column=3, row=0, columnspan=2, rowspan=1, sticky=(N, W), padx=5) # anchor to the top and left edges of the cell, provide padding to the left and right
txt_name.grid(column=3, row=1, columnspan=2, sticky=(N, W, E), padx=5, pady=5)  # anchor to the top, left, and right, provide padding in the x and y directions
chk_one.grid(column=0, row=2)       # The book example had these next five controls in row 3, but it is unclear
chk_two.grid(column=1, row=2)       # if this was intended to provide some sort of additional padding. I did not
chk_three.grid(column=2, row=2)     # notice any substantial difference after changing to 2. Try it out for yourself
btn_okay.grid(column=3, row=2)      # and see if you perceive it differently.
btn_cancel.grid(column=4, row=2)

root.columnconfigure(0, weight=1)   # define column 0 to grow by a weight/factor of 1
root.rowconfigure(0, weight=1)      # define row 0 to grown by a weight of 1
content.columnconfigure(0, weight=3)    # repeat of the same but effect the columns of the frame that acts
content.columnconfigure(1, weight=3)    #    as the parent for all the widgets we've defined
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()

