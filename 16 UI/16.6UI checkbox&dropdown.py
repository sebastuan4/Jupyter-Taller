from tkinter import *
from tokenize import String

class ventana:
    root=Tk()
    #Checkbox
    var=StringVar()
    chk1=Checkbutton(root,text="Check 1",variable=var,onvalue="True",offvalue="False")
    chk1.deselect()
    chk1.pack()
    lbl=Label(root,textvariable=var).pack()

    #Dropdown
    option=StringVar()
    option.set("Option1")
    drop=OptionMenu(root,option,"Opcion1","Opcion2","Opcion3","Opcion4").pack()
    
    def mostrar():
        ventana.root.mainloop()

ventana.mostrar()


    
