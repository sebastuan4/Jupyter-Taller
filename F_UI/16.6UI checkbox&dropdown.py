from tkinter import *

class ventana():
    root=Tk()
    #Checkbox
    var=StringVar()
    var2=StringVar()
    chk1=Checkbutton(root,text="Check 1",variable=var,onvalue="Hola",offvalue="Adios")
    chk2=Checkbutton(root,text="Check 2",variable=var2,onvalue="True",offvalue="False")
    chk1.deselect()
    chk2.deselect()
    chk1.pack()
    chk2.pack()
    lbl=Label(root,textvariable=var).pack()
    lbl=Label(root,textvariable=var2).pack()

    #Dropdown
    option=StringVar()
    option.set("Option1")
    drop=OptionMenu(root,option,"Opcion1","Opcion2","Opcion3","Opcion4").pack()
    
    def mostrar():
        ventana.root.mainloop()

ventana.mostrar()


    
