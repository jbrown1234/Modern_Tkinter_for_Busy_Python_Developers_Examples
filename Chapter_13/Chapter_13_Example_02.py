# Example from the book showing how to create a canvas and draw lines on it.

# Reference: https://www.tcl.tk/man/tcl8.6/TkCmd/canvas.htm

from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0
color = "black"


def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    lastx, lasty = event.x, event.y


def setColor(newcolor):
    global color
    color = newcolor


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

# Add three rectangles on the canvas that can be clicked on by the user
# to change the color of the line being drawn. Note how all rectangles
# share the same tag. The ID's are created separate, allowing us to bind
# the click event for each to a different color for the draw line.
id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))

id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))

id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

id = canvas.create_rectangle((10, 85, 30, 105), fill="green")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("green"))

root.mainloop()