# Reference: https://www.tcl.tk/man/tcl8.6/TkCmd/button.htm

from tkinter import *
from tkinter import ttk
import winsound             # note - intended to work with Windows systems; no promises on Linux or Mac

root = Tk()


def button_a_press(*args):
    # issue a system beep
    #print('\a')                # should be universally acceptable, but some sound systems disable
    #winsound.Beep(440, 500)    # blocked on some Windows system configurations
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    if button_b.instate(['disabled']):  # we can also check the state of the control...
        button_b.state(['!disabled'])
    return


def button_b_press(*args):
    button_a.invoke()     # we can access button A's event/action/callback by invoking it
    return


def button_c_press(*args):
    button_a.invoke()
    button_b.state(['disabled'])    # note that states can be: disabled, active, focus, press, or selected; in
                                    # this case you should note how the B button becomes disabled and unusable
    return


# note that we don't necessarily have to start with a frame, we can "pack" a widget into the
# root object and it will be displayed as well...
button_a = ttk.Button(text="A button", command=button_a_press)
button_a.pack(side=LEFT)

# buttons need a styled defined to change their background and foreground colors
s = ttk.Style()
s.configure('My.TButton', background='#151515', foreground='#FF0000')
button_a.configure(style='My.TButton')

button_b = ttk.Button(text='B button', command=button_b_press)
button_b.pack(side=RIGHT)

button_c = ttk.Button(text='C button', command=button_c_press)
button_c.pack(side=RIGHT)

root.mainloop()
