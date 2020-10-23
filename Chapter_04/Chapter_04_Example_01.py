from tkinter import *
from tkinter import ttk

# we define the function(s) early on in our application, prior to widget + action
# definition to allow for the function(s) to be used by multiple callers
def calculate(*args):
   try:
       value = float(feet.get())
       meters.set((0.0304 * value * 10000.0 +0.5)/10000.0)
   except ValueError:
       pass


root = Tk()
root.title("Feet to Meters")

# Call up a Frame tool from the ttk library and define attributes
mainframe = ttk.Frame(root, padding="3 3 12 12") # tied to root because it is the top-level UI
                                                # padding is interesting and provides room between
                                                # the grid-placed widgets and the frame they
                                                # reside within (R T L B)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # anchors to the root at the default position
root.columnconfigure(0, weight=1)   # helps with frame/app resizing on the fly
root.rowconfigure(0, weight=1)      # helps with frame/app resizing on the fly

# define our two main global variables that are to hold active values
feet = StringVar()
meters = StringVar()

# define a text entry widget to capture user input and to reside within the frame
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# define the label that will display the calculated meters value; note how textvariable is used
# to bind the label the to meters global variable
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# define the button that the user clicks after entering the feet into the text entry input widget
# also note how no parameters are passed into the calculate function bound to command; here is the
# reliance on globals
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# define a label widget to display the units; notice that it's defined to reside in the same
# row as the text entry widget and the column that would place =it to the right of the same
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)

# define a label to dress up the logic on the frame
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)

# define a label to sit to the right of the calculated meters label; note how it's located
# in proximity to the meters label
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# loop to include padding around the widgets that are placed
# on the frame
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# define which widget will be the active control - where the cursor or action will occur - when
# the UI is started and frame/form is displayed
feet_entry.focus()

# this tells the program that whenever the Return or Enter key is pressed the
# calculate function is to be executed - the same action as when the operator
# clicks the Calculate button
root.bind('<Return>', calculate)

# run the application
root.mainloop()