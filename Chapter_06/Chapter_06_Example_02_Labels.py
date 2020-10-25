# Reference: https://www.tcl.tk/man/tcl8.6/TkCmd/label.htm

from tkinter import *
from tkinter import ttk
from tkinter import font as tk_font		# for playing with fonts

root = Tk()

# let's start with creating a frame on which to place our labels...
my_window = ttk.Frame(root, padding="3 3 12 12", height=350, width=350)
my_window.grid(column=0, row=0, sticky=(N, W, E, S))    # anchors to the root at the default position
root.columnconfigure(0, weight=1)   # helps with frame/app resizing on the fly
root.rowconfigure(0, weight=1)      # helps with frame/app resizing on the fly

string_variable = StringVar()

label = ttk.Label(my_window, text="Full name")  # define our label and tell to reside on the frame
label.grid(column=1, row=2, sticky=E)           # make sure you place on the grid or the label won't show
label['textvariable'] = string_variable         # and make the label automatically responsive to changes to
                                                #   the variable string_variable
label['foreground'] = "#0101DF"                 # modify the foreground text color without a Style applied
label['background'] = "#00FFBF"                        # same goes for the background color
a_font = tk_font.nametofont("TkTooltipFont")    # the text in this chapter discusses changing fonts, but no
label.configure(font=a_font)                    # good example is provided; this is a hack; doesn't crash the
string_variable.set("hey, look.... new text")   # program; but doesn't appear to change things either

# labels can also act as a small canvas on which to place an image....
some_image = PhotoImage(file="Chapter_06_Example_02_gold-mines.gif")
image_label = ttk.Label(my_window, image=some_image)
image_label.grid(column=1, row=3)

root.mainloop()

