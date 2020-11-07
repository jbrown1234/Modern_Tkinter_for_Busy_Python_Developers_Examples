# Adding this example just to exhibit what the outcome is per using the book example structure. In reality
# while we should expect one UI with the menubar to appear, we get two UIs and only one include our menubar.
# This is not right. The outcome appears to be due to using the Toplevel widget which creates a window/UI
# on top of any other (pre)existing window/UI which has not first been suppressed. See the link
# https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/ for more details.
#
# Perhaps the author had a reason for sharing this with us so early in the learning process, however, it caused
# this programmer some headache and grief. Only examples in later chapters will help reveal if there is a method
# to the madness. However, mistake or not, this did lead to some searching, exploring and learning to share. 

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Menus per the book...")

win = Toplevel(root)
menubar = Menu(root)
appmenu = Menu(menubar, name='apple')
menubar.add_cascade(menu=appmenu)
appmenu.add_command(label='About my application')
appmenu.add_separator()
win['menu'] = menubar

root.mainloop()