from tkinter import *
from tkinter import ttk

root = Tk()
root.title("A Look at Frames...")

# Call up a Frame tool from the ttk library and define attributes
mainframe = ttk.Frame(root, padding="3 3 12 12", height=35, width=35) # tied to root because it is the top-level UI
                                                # padding is interesting and provides room between
                                                # the grid-placed widgets and the frame they
                                                # reside within (R T L B)
                                                
mainframe.configure(height=175, width=300)  # note that we can use the configure method and pass the
                                            # height and width

s = ttk.Style()                             # To change the background color, first create a Style
#s.configure('My.TFrame', background='red')  # to define the attribute(s) you want to apply...
s.configure('My.TFrame', background='#088A68')  # you can also pass in HTML color codes - refer to
                                                # https://html-color-codes.info/ for colors and codes
                                                # of your own choosing
mainframe.configure(style='My.TFrame')      # ...then use configure to enable it

mainframe['padding'] = (5, 10)      # allow for some cushion between internal widgets and the frame edge

mainframe['borderwidth'] = 50       # for frames with visible borders, define the thickness

mainframe['relief'] = 'groove'      # how do you want your frame to appear on the screen - play with
                                    # settings like flat (default, raised, sunken, solid, ridge, groove

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # anchors to the root at the default position
root.columnconfigure(0, weight=1)   # helps with frame/app resizing on the fly
root.rowconfigure(0, weight=1)      # helps with frame/app resizing on the fly

root.mainloop()

# for more info see: https://tcl.tk/man/tcl8.6/TkCmd/frame.htm
