# Example from the book showing how to create a canvas and draw lines on it. This third update to the
# main example takes tags a step further. We expand the opreator's viewing/creating area by adding in
# scrollbars.

# Reference: https://www.tcl.tk/man/tcl8.6/TkCmd/canvas.htm

from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0
color = "black"


def xy(event):
    global lastx, lasty
    # Change such that the coordinates are updated according to where on the sized
    # and/or scrolled canvas the event occurred.
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)


def addLine(event):
    global lastx, lasty
    # During the drawing of the line, we'll make it more pronounced by increasing
    # its width. The line being created will get its own identifying tag so that it
    # can be referenced by doneStroke() and restore the original width once the line
    # has been placed.
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y) # note the slight variation on how
                                                            # we are capturing the clicked
                                                            # coordinates
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y


def doneStroke(event):
    # When done drawing the line, set the width back to the default
    canvas.itemconfigure('currentline', width=1)


def setColor(newcolor):
    global color
    color = newcolor
    # Updates to this function
    canvas.dtag('all', 'palletteSelected')
    canvas.itemconfigure('pallette', outline='white') # note that the default outline is white...
    canvas.addtag('palletteSelected', 'withtag', 'pallette{0}'.format(color))
    canvas.itemconfigure('palletteSelected', outline='#999999') # ...but the outline changes color when selected


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add horizontal and vertical scrollbars to our UI
h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)

canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S, E))
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
h.grid(column=0, row=1, sticky=(W, E))      # place the scrollbars
v.grid(column=1, row=0, sticky=(N, S))

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)   # bind the event action to the function just defined

# Add three rectangles on the canvas that can be clicked on by the user
# to change the color of the line being drawn. Note how all rectangles
# share the same tag. The ID's are created separate, allowing us to bind
# the click event for each to a different color for the draw line. In this
# case, notice how each rectangle is defined with a series of tags, one
# common - 'pallette' - with the rest being unique. The common tag can be
# used to configure all the items with one command call while the individual
# tags promote focus on a specific item (as used in the setColor() function.
id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('pallette', 'pallettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))

id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('pallette', 'palletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))

id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('pallette', 'palletteblack', 'palletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

id = canvas.create_rectangle((10, 85, 30, 105), fill="green", tags=('pallette', 'pallettegreen'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("green"))

setColor('black')
canvas.itemconfigure('pallette', width=5)

root.mainloop()
