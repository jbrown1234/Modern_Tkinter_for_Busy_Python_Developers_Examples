# https://www.tcl.tk/man/tcl8.6/TkCmd/menu.htm

from tkinter import *
from tkinter import ttk

root = Tk()
#root.option_add('tearOff', FALSE)      # The book calls for using this in code in common practice
                                        #   but doesn't provide any concrete example where it is used
root.title("Exercise in Using Menus")
root.geometry('350x200')


def new_file(*args):
    print('new file')


def open_file(*args):
    print('open file')


def close_file(*args):
    print('close file')


def exit_file(*args):
    exit(0)


def copy_text(*args):
    print('Copy')


def cut_text(*args):
    print('Cut')


def paste_text(*args):
    print('Paste')


def show_about(*args):
    print('About...')


def make_bold(*args):
    print('Bold')


def make_italics(*args):
    print('Italics')


def make_underline(*args):
    print('Underline')


def change_green(*args):
    print('Green')


def change_blue(*args):
    print('Blue')


def change_red(*args):
    print('Red')


# Create a menubar by first creating a menu widget then unsing the window's menu configuration option
# to attach the menu widget to the window....
menubar = Menu(root) # insert a menubar on the main window

root.config(menu=menubar)    # this was found in an online example and...
#root['menu'] = menubar      #   ...has the same effect as this line

# Create a menu widget for each menu that will go into the menu bar...
menu_file = Menu(menubar, tearoff=0)        # Note the 'tearoff' option called out here; an alternative to
                                            # the recommendation by the book
menu_edit = Menu(menubar, tearoff=0)
menu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu_file, label='File')       # While the main menubar menus were shown to be added
menubar.add_cascade(menu=menu_edit, label='Edit')       #   to the bar first in the book, other examples show
menubar.add_cascade(menu=menu_help, label='Help')       #   adding the menu items being configured for each
                                                        #   menu first. Experiment on your own and review conventions
                                                        #   used by more seasoned programmers to determine
                                                        #   what works best for you.
menu_file.add_command(label='New', command=new_file, accelerator="Ctrl+f")
root.bind("<Control-f>", new_file)
menu_file.add_command(label='Open', command=open_file, accelerator="Ctrl+o")
root.bind("<Control-o>", open_file)
menu_file.add_command(label='Close', command=close_file, accelerator="Ctrl+c")
root.bind("<Control-s>", close_file)
menu_file.add_separator()
menu_file.add_command(label='Exit', command=exit_file, accelerator="Ctrl+x")
root.bind("<Control-x>", exit_file)

menu_edit.add_command(label='Copy', command=copy_text)
menu_edit.add_command(label='Cut', command=cut_text)
menu_edit.add_command(label='Paste', command=paste_text)
menu_edit.add_separator()
menu_edit.add_checkbutton(label="Bold", command=make_bold)
menu_edit.add_checkbutton(label='Italics', command=make_italics)
menu_edit.add_checkbutton(label="Underline", command=make_underline)
menu_edit.add_separator()
menu_edit.add_radiobutton(label='Green', command=change_green)
menu_edit.add_radiobutton(label='Blue', command=change_blue)
menu_edit.add_radiobutton(label='Red', command=change_red)

menu_help.add_command(label='About', command=show_about)

root.mainloop()
