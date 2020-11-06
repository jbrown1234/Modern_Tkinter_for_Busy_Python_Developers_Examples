# https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_progressbar.htm

from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Making progress...")
# build control functions here...


def button_a_press(*args):
    for j in range(0,101):
        # fist disable the buttons to give the feel that the operation has focus...
        btn_det_start['state'] = 'disabled'
        btn_indet_start['state'] = 'disabled'
        # update the determinate progress bar one percent at a time until full then re-enable the button(s)
        det_prog.set(j)         # update the progress bar
        root.update_idletasks()  # tell the app to update since the widget state has changed; otherwise the app
                                 #    will appear to hang until after it's reached 100% and that doesn't look good
        time.sleep(0.025)        # delay for 25 ms
        # re-enable our buttons...
        btn_det_start['state'] = 'enabled'
        btn_indet_start['state'] = 'enabled'
        #root.update_idletasks()
    return


def button_b_press(*args):
    if indet_state.get() == 0:
        indet_state.set(1)
        prg_indeterminate.start(10) # set the update rate to once every 10 ms
        btn_indet_start['text'] = "Stop"
        btn_det_start['state'] = 'disabled'
    else:
        indet_state.set(0)
        prg_indeterminate.stop()
        btn_indet_start['text'] = "Start"
        btn_det_start['state'] = 'enabled'


det_prog = IntVar()
det_prog.set(0)
indet_state = IntVar()
indet_state.set(0)

# create our controls....
prg_determinate = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate', variable=det_prog)
btn_det_start = ttk.Button(root, text="Start", command=button_a_press)
prg_indeterminate = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='indeterminate')
btn_indet_start = ttk.Button(root, text="Start", command=button_b_press)

# place the controls on the grid...
prg_determinate.grid(column=0, row=0, sticky=(W,E))
btn_det_start.grid(column=1, row=0, sticky=(N,W,E,S))
prg_indeterminate.grid(column=0, row=1, sticky=(W,E))
btn_indet_start.grid(column=1, row=1, sticky=(N,W,E,S))

root.mainloop()