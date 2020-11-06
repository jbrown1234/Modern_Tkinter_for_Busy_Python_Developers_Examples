# https://www.tcl.tk/man/tcl8.6/TkCmd/listbox.htm

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Listbox with Scrollbar")

# Initialize our countries "databases":
#   - the list of the country codes (a subset anyway)
#   - a parallel list of country names, in the same order as the country codes
#   - a hash table mapping country code to population
countrycodes = ('ar',
                'au',
                'be',
                'br',
                'ca',
                'cn',
                'dk',
                'fi',
                'fr',
                'gn',
                'in',
                'it',
                'jp',
                'mx',
                'nl',
                'no',
                'es',
                'se',
                'ch')
countrynames = ('Argentina',
                'Australia',
                'Belgium',
                'Brazil',
                'Canada',
                'China',
                'Denmark',
                'Finland',
                'France',
                'Greenland',
                'India',
                'Italy',
                'Japan',
                'Mexico',
                'Netherlands',
                'Norway',
                'Spain',
                'Sweden', 'Switzerland')
cnames = StringVar(value=countrynames)

populations = {'ar': 41000000,
               'au': 21179211,
               'be': 10584534,
               'br': 185971537,
               'ca': 33148682,
               'cn': 1323128240,
               'dk': 5457415,
               'fi': 5302000,
               'fr': 64102140,
               'gn': 11147000,
               'in': 1131043000,
               'it': 59206382,
               'jp': 127718000,
               'mx': 106535000,
               'nl': 16402414,
               'no': 4738085,
               'es': 45116894,
               'se': 9174082,
               'ch':7508700
               }

# Names of the gifts we can send...
gifts = {'card': "Greeting card",
         'flowers': "Flowers",
         'nastygram': "Nastygram"
         }

# state variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

# Called when the selection in the list box changes; figure out which country is currently selected, and then look
# up its country code, and from that, its population. Update the status message with the new population. As well,
# clear the message about the gift being sent, so it doesn't stick around after we start doing other things.
def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of {0} ({1}) is {2}".format(name, code, popn))
    sentmsg.set('')

# Called when the user double-clicks and item in the list box, presses the "Send gift" button, or presses the Return
# key. In the case the selected item is scrolled out of view, make sure it is visible.

# Figure out which country is selected, which gift is selected with the radio buttons, "send the gift", and provide
# feedback that it was sent.


def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # Gift sending left as an exercise to the reader
        sentmsg.set("Sent {0} to leader of {1}.".format(gifts[gift.get()], name))


# Create and grid the outer content frame....
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,S,E,W))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create the different widgets; note the variables that many of them are bound to as well as the button callback.
# Note that we're using the StringVar() 'cnames' constructed from 'countrynames'.
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Send to country's leader:")
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
send = ttk.Button(c, text="Send Gift", command=sendGift, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Let's introduce a scrollbar to help navigate through our list of options...
scb_lbox = ttk.Scrollbar(c, orient=VERTICAL, command=lbox.yview)
lbox['yscrollcommand'] = scb_lbox.set

# Grid all the widgets....
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=2, row=0, padx=10, pady=5)        # let's move some widgets to the right to accommodate
g1.grid(column=2, row=1, sticky=W, padx=20)       #    the scrollbar...
g2.grid(column=2, row=2, sticky=W, padx=20)       #    ...
g3.grid(column=2, row=3, sticky=W, padx=20)       #    ...
send.grid(column=3, row=4, sticky=E)              #    ...
sentlbl.grid(column=2, row=5, columnspan=2, sticky=N, padx=5, pady=5) # ...
status.grid(column=0, row=6, columnspan=3, sticky=(E,W))    # updated the rowspan to be inclusive of the
                                                            #    column the scrollbar now occupies
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)
scb_lbox.grid(column=1, row=0, rowspan=6, sticky=(N,S))

# Set event bindings for the selection in the list box changes, when the user double-clicks the list and when they
# hit the Return key
lbox.bind('<<ListboxSelect>>', showPopulation)
lbox.bind('<Double-l>', sendGift)
root.bind('<Return>', sendGift)

# Colorize alternating lines of the list box....
for i in range(0, len(countrynames), 2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the default gift to send, and clearing the messages.
# Select the first country in the list; becaus the <<ListboxSeledt>> event is only generated when the user makes a
# change, we explicitly call ShowPopulation
gift.set('card')
sentmsg.set('')
lbox.selection_set(0)
showPopulation()

root.mainloop()
