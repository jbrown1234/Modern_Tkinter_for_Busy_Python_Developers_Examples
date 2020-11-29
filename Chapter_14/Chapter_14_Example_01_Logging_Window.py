# We have already breifly covered Text widgets in an earlier chapter and the author is circling
# back to try to do it justice with more in-depth explanation.
#
# Interesting example from the text: "Here's a short example illustrating how to use a text widget
# as an 80x24 logging window for your application. The user doesn't edit the text widget at all;
# instead, your program will write log messages to it. You'd like to keep the content to no more
# than 24 lines (so no scrolling), so as you add new messages to the end, you'll have to remove
# old ones from the top if there are already 24 lines.
#
# Important take-away: THIS IS NOT A COMPLETE EXAMPLE. The author is leaving it up to the reader
# to find a way to include it within their own code. The point is to show off how to refer to
# different text positions within the widget.

from tkinter import *
from tkinter import ttk

root = Tk()
log = Text(root, state='disabled', width=80, height=24, wrap='none')
log.grid(column=0, row=0)

def writeToLog(msg):
    num_lines = log.index('end - 1 line').split('.')[0]
    log['state'] = 'normal'
    if num_lines == 24:
        log.delete(1.0, 2.0)
    if log.index('end-1c') != '1.0':
        log.insert('end', '\n')
    log.insert('end', msg)
    log['state'] = 'disabled'

# run.mainloop()