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


def no_help(*args):
    if nohelpmnustate.get() == 1:                       # For disabling a menubar option, the index of the option is
        #menubar.entryconfig(3, state='disabled')       # not zero-based, but starts at 1. The Help menu is option 3
        menubar.entryconfig('Help', state='disabled')   # so we pass this in as the first parameter of the entryconfig()
    else:                                               # method and define its availability per the 'state' option.
        menubar.entryconfig(3, state='normal')          # It does appear that you can do the same using a key value.


def no_about(*args):                                # While menu option items enabling/disabling shares the use of
    if noaboutmnustate.get() == 1:                  # entryconfig(), note how the items are expected to be zero-based
        menu_help.entryconfig(0, state='disabled')  # when referencing. If using key values, the difference in how the
    else:                                           # target is accessed is probably not a big deal.
        #menu_help.entryconfig(0, state='normal')
        menu_help.entryconfig('About', state='normal')


nohelpmnustate = IntVar()
nohelpmnustate.set(0)
noaboutmnustate = IntVar()
noaboutmnustate.set(0)

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
menubar.add_cascade(menu=menu_file, label='File', underline=0)       # While the main menubar menus were shown to be added
menubar.add_cascade(menu=menu_edit, label='Edit', underline=0)       #   to the bar first in the book, other examples show
menubar.add_cascade(menu=menu_help, label='Help', underline=0)       #   adding the menu items being configured for each
                                                                     #   menu first. Experiment on your own and review conventions
                                                                     #   used by more seasoned programmers to determine
                                                                     #   what works best for you.
                                                                     # Something of interest to note: the underline option
                                                                     #   helps to add shortcut key action to the menu item
                                                                     #   selection. However, what I see on Windows is that
                                                                     #   the underline doesn't show up until (or unless)
                                                                     #   the menu bar has focus. Not being able to see
                                                                     #   what the alt+key combo might be somewhat defeats
                                                                     #   the purpose of having it available.
menu_file.add_command(label='New', command=new_file, accelerator="Ctrl+f")  # Check out the add of the accelerator tag
root.bind("<Control-f>", new_file)  # ...and this statement binds the accelerator key combo to the function
menu_file.add_command(label='Open', command=open_file, accelerator="Ctrl+o")
root.bind("<Control-o>", open_file)
menu_file.add_command(label='Close', command=close_file, accelerator="Ctrl+c")
root.bind("<Control-s>", close_file)
menu_file.add_separator()           # add a separator to break things up a bit....
menu_file.add_command(label='Exit', command=exit_file, accelerator="Ctrl+x")
root.bind("<Control-x>", exit_file)

menu_edit.add_command(label='Copy', command=copy_text)
menu_edit.add_command(label='Cut', command=cut_text)
menu_edit.add_command(label='Paste', command=paste_text)
menu_edit.add_separator()
menu_edit.add_checkbutton(label="Bold", command=make_bold)              # Checkbuttons can be used to apply multiple
menu_edit.add_checkbutton(label='Italics', command=make_italics)        # attributes as desired/needed
menu_edit.add_checkbutton(label="Underline", command=make_underline)
menu_edit.add_separator()
menu_edit.add_radiobutton(label='Green', command=change_green)          # Radiobuttons make the user choose between
menu_edit.add_radiobutton(label='Blue', command=change_blue)            # the options in a given group.
menu_edit.add_radiobutton(label='Red', command=change_red)
menu_edit.add_separator()
#menu_edit.add_radiobutton(label='One')                                 # The separator does not implicitly break
#menu_edit.add_radiobutton(label='Two')                                 # these additional radiobutton items from the
                                                                        # ones defined previously for this menu. Will
                                                                        # leave figuring out how to split things up
                                                                        # for a future investigation.
menu_edit.add_checkbutton(label="No Help", command=no_help, variable=nohelpmnustate)    # Added these two menu options
menu_edit.add_checkbutton(label="No About", command=no_about, variable=noaboutmnustate) # to see how they operate. See
                                                                                        # their command functions above
                                                                                        # for additional peculiarities.

menu_help.add_command(label='About', command=show_about)

root.mainloop()
