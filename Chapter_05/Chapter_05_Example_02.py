# A modification from the origina example which was meant to be run
# through IDLE a line at a time, this revision places a frame on the
# UI at run time and applies settings. 
from tkinter import *
from tkinter import ttk
root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
def control_changed(*args):
    if click_counter == 0:
        print(0)
    elif click_counter == 1:
        print(1)
    return

click_counter = IntVar()
click_counter.set(0)

l = ttk.Label(root, text="Starting")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text="Moved mouse inside"))
l.bind('<Leave>', lambda e: l.configure(text="Moved mouse outside"))
l.bind('<l>', lambda e: l.configure(text="Clicked left mouse button"))
l.bind('<Double-l>', lambda e: l.configure(text="Double clicked button"))

# run the application
root.mainloop()