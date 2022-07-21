from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntryListbox
root=Tk()
lista=["valor 1","val 2","volar","ve","carlos"]
AutocompleteEntryListbox(root,completevalues=lista).pack()
root.mainloop()
