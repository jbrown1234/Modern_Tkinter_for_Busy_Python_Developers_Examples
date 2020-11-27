# Similar to the example for Frames in Chapter 2, here we offer an alternate way to
# add an image to a widget. We use the "made for Python" image library identified as
# PIL (aka, Python Imaging Library) that is an extension of the pillow library. The
# book is careful to note that pillow may not be installed on your PC but can be
# added by issuing the following at a command line: pip install Pillow.

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Images with Python on the PIL")

# Load up an image which we can display....
myimg = ImageTk.PhotoImage(Image.open('happy_dog.png'))

# Apply the image to a label widget....
lbl_image_holder = ttk.Label(root, image=myimg)

# Place the label in the UI
lbl_image_holder.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()