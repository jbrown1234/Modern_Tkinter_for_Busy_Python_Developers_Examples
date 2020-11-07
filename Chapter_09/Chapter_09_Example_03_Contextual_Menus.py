# This example shows how to include pop-up menus to your application. Note that 'aqua' refers to use
# on a Mac system where the binding of the mouse click needs to be a little more hardware specific. In
# the case of Windows and Linux, things are a bit more common.
from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Contextual Menus')
root.geometry('300x300')

menu = Menu(root)
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)
if(root.tk.call('tk', 'windowingsystem') == 'aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))           # Bind to a middle mouse button click...
    root.bind('<Control-1', lambda e: menu.post(e.x_root, e.y_root))    # ...or the Ctrl plus left mouse button click
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))           # Bind to a right mouse button click.

label = ttk.Label(root, text="Click on the window area to reveal the menu")
label.grid(column=0, row=0, sticky=(W,E))

root.mainloop()