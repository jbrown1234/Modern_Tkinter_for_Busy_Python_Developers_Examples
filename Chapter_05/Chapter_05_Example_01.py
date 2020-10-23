# This example is best used by executing one line at a time with the IDLE interface
from tkinter import *
from tkinter import ttk

root = Tk()

# create a button passing two options....
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid()
# check the current value of the text option
button['text']
#change the value of the test option:
button['text'] = "goodbye"
# another way to do the same thing...
button.configure(text="adios")
# check the current value of the text option:
print(button['text'])
# get all the information about the text option...
button.configure('text')
# get information on all options for this widget:
button.configure()
# {'command': ('command', 'command', 'Command', '', 'buttonpressed'),
#  'default': ('default', 'default', 'Default', <string object: 'normal'>, <string object: 'normal'>),
#  'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'),
#  'text': ('text', 'text', 'Text', '', 'adios'),
#  'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
#  'underline': ('underline', 'underline', 'Underline', -1, -1),
#  'width': ('width', 'width', 'Width', '', ''),
#  'image': ('image', 'image', 'Image', '', ''),
#  'compound': ('compound', 'compound', 'Compound', <string object: 'none'>, <string object: 'none'>),
#  'padding': ('padding', 'padding', 'Pad', '', ''),
#  'state': ('state', 'state', 'State', <string object: 'normal'>, <string object: 'normal'>),
#  'cursor': ('cursor', 'cursor', 'Cursor', '', ''),
#  'style': ('style', 'style', 'Style', '', ''),
#  'class': ('class', '', '', '', '')}