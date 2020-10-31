from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root) # create a base frame on which all controls reside...

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
content.grid(column=0, row=0)   # the main frame, content, is anchored to the top left corner of the root
frame.grid(column=0, row=0, columnspan=3, rowspan=2)    # recall that this frame is a child of the content frame
lbl_name.grid(column=3, row=0, columnspan=2, rowspan=1) # we added the rowspan call here even though it is not needed
txt_name.grid(column=3, row=1, columnspan=2)
chk_one.grid(column=0, row=2)       # The book example had these next five controls in row 3, but it is unclear
chk_two.grid(column=1, row=2)       # if this was intended to provide some sort of additional padding. I did not
chk_three.grid(column=2, row=2)     # notice any substantial difference after changing to 2. Try it out for yourself
btn_okay.grid(column=3, row=2)      # and see if you perceive it differently.
btn_cancel.grid(column=4, row=2)


root.mainloop()

