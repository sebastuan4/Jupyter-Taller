from tkinter import *
from tkinter.ttk import Labelframe

class rbtn:
    root=Tk()
    #r=IntVar()
    #r.set(1)
    frame=Labelframe(root,text="Text",pad=20)
    Modes = [("Opcion 1","Opcion 1"),("Opcion 2","Opcion 2"),("Opcion 3","Opcion 3"),("Opcion 4","Opcion 4")]
    options = StringVar()
    options.set("Opcion 1")

    def mostrando():
        for textOpt, valor in rbtn.Modes:
            Radiobutton(rbtn.frame,text=textOpt,variable=rbtn.options,value=valor).pack()
        Label(rbtn.frame,textvariable=rbtn.options).pack()
        rbtn.frame.pack(padx=20,pady=20)
        rbtn.root.mainloop()
      
rbtn.mostrando()


    
