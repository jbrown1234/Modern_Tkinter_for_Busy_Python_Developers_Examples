from tkinter import *
from tkinter import ttk
from tkinter import filedialog # note how we must specify this library; it is not implied in the other two import

#filename = filedialog.askdirectory() # dialog to aid in reteruning a selected folder path
#print(filename)

# One really helpful thing you can add to your file open dialog is the ability to filter on
# specific file types. Here we specify that we only want markdown files with the .md extension
# to be made visible when the dialog is presented to us and as we navigate through the file
# system looking for our target.
filename = filedialog.askopenfile(mode='r', filetypes=[('Markdown Files', '*.md')]) #
print(filename)

#filename = filedialog.askopenfiles()
#print(filename)
