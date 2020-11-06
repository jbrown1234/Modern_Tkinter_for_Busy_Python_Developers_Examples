# https://www.tcl.tk/man/tcl8.6/TkCmd/scrollbar.htm

from tkinter import *
from tkinter import ttk

root = Tk()

l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,S,E,W))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set         # reference the scrollbar action to the list box scroll command
ttk.Label(root, text="Status message here", anchor=(W)).grid(column=0, row=1, sticky=(W,E))
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))  # Note the introduction to the sizegrip control and how it
                                                        # gets placed in the bottom right corner of the UI

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

for i in range (0, 100):
    l.insert('end', "Line {0} of 100".format(i))

root.mainloop()