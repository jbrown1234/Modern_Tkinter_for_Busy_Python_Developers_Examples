from tkinter import *
from tkinter import ttk

# Some of the info that begins the chapter is a bit on the redundant or weak side. TopLevel() was
# introduced earlier in the book without much rhyme or reason and (in my case) left the user to
# back out any of its usage. Further, calling up child or ancillary windows tends to leave the user
# wanting to DO SOMETHING with the widgets on the window/frame, and there is no information on managing
# functionality. The close action of the child window found here was found online. Additionally, for
# child windows which need more functionality, it appears that the user should build them into a class
# then instantiate the child window object. We'll leave it up to the reader to investigate further (as
# it seems the book did).

# References...
# https://www.plus2net.com/python/tkinter-Toplevel.php
# https://www.geeksforgeeks.org/python-tkinter-tutorial/#advance


def btn_newwindow_press(*args):
    # stuff
    alt_window = Toplevel(root)
    btn_close = ttk.Button(alt_window, text="Close", command=alt_window.destroy)
    btn_close.grid(column=0, row=0, sticky=(N,W,E,S))

    return


# add some globals here

root = Tk()
root.title("TopLevel Window Maker")
root.geometry("400x300")

# create base widgets...
lbl_dumblabel = ttk.Label(root, text="Dumb Label...")
btn_newwindow = ttk.Button(root, text="A button", command=btn_newwindow_press)

# grid up the base widgets
btn_newwindow.grid(column=3, row=3, sticky=(S,E))
lbl_dumblabel.grid(column=0, row=0, sticky=(N,W))

root.mainloop()