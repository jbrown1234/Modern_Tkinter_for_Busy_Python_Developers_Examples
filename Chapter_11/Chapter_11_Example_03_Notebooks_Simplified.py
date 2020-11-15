from tkinter import *
from tkinter import ttk

root = Tk()

n = ttk.Notebook(root, width=100, height=100)
f1 = ttk.Frame(n, width=100, height=100)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n, width=100, height=100)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')

btn_a = ttk.Button(f1, text="A Button")
btn_b = ttk.Button(f2, text='Another')

n.grid(column=0, row=0)

btn_a.grid(column=0, row=0)
btn_b.grid(column=0, row=0)

root.mainloop()