# While fonts are new in this chapter, coloring your widgets and text are not. This example provides just
# a few ways the user might consider customizing their widgets to add an extra bit of zest to the UI. 

from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.title("Fonts and Colors Example")

# Create the widgets to be used....
pad_left = 5
pad_right = 5
pad_top = 5
pad_bottom = 5

# To work with the basic Tk standard fonts....
lblA = ttk.Label(root, text="Using standard font with nn point size", pad=(pad_left, pad_top, pad_right, pad_bottom), font='TkFixedFont')

# To work with custom fonts....
#print(font.families())     # to get a list of the fonts available on your system, uncomment this line...
lblB_font = font.Font(family="Roman", size=12, weight='normal', slant='roman')
lblB = ttk.Label(root, text="Using Roman font with 12 point size", pad=(pad_left, pad_top, pad_right, pad_bottom), font=lblB_font)
lblC_font = font.Font(family='MS Sans Serif', size=10, weight='bold', slant='italic', underline=1, overstrike=1)
lblC = ttk.Label(root, text="Using MS Sans Serif font with 10 point size, bold, italicized, underlined, with strikethrough...", font=lblC_font)
# You can pull custom colors from any HTML chart on the web like https://html-color-codes.info/
lblD = ttk.Label(root, text="Adding color to your control...", foreground="#FAFAFA", background="blue")
lblE = ttk.Label(root, text="Another way to specify font in code...", font=("Helvetica 16 bold roman"), foreground="#00FF00")

# Place the widgets on our form....
lblA.grid(column=0, row=0, sticky=(N, W, E, S))
lblB.grid(column=0, row=1, sticky=(N, W, E, S))
lblC.grid(column=0, row=2, sticky=(N, W, E, S))
lblD.grid(column=0, row=3, sticky=(N, W, E, S))
lblE.grid(column=0, row=4, sticky=(N, W, E, S))
# Start the UI loop...
root.mainloop()

