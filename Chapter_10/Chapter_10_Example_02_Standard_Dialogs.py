from tkinter import *
from tkinter import ttk
from tkinter import filedialog # note how we must specify this library; it is not implied in the other two imports

# In general, tkinter offers many standard dialogs to help with a number of different things. We hit the basics here,
# but it would be best to see them in action.

#directoryname = filedialog.askdirectory() # dialog to aid in reteruning a selected folder path
#print(directoryname)

# One really helpful thing you can add to your file open dialog is the ability to filter on
# specific file types. Here we specify that we only want markdown files with the .md extension
# to be made visible when the dialog is presented to us and as we navigate through the file
# system looking for our target.
file = filedialog.askopenfile(mode='r', filetypes=[('Markdown Files', '*.md')]) #
if file is not None:
        content = file.read()
        print(content)

#filename = filedialog.askopenfiles()
#print(filename)

# The example below uses asksaveasfile to first create then open the file for writing. The two links below show 1. the
# general function being used and 2. an actual application of the function.
# https://www.geeksforgeeks.org/python-asksaveasfile-function-in-tkinter/
# https://iot4beginners.com/asksaveasfile-function-in-python-tkinter/
filetypes = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
             ('Markdown Files' '*.md')]

filename = filedialog.asksaveasfile(mode="w", filetypes=filetypes)
filename.write("A simple sentence...")
filename.close()

# We will not cover them in this example, but other options are as follows:
# filedialog.askopenfilename()
# filedialog.askopenfilenames()
# filedialog.asksaveasfilename()
