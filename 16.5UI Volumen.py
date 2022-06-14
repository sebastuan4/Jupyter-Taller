
from tkinter import *

class ventana:
    root=Tk()
    def open():
        top=Toplevel()
        volume=IntVar()
        lbl=Label(top,text="Nueva ventana").pack()
        vertical=Scale(top,from_=100,to=0,variable=volume)
        vertical.pack()
        lbl_volume=Label(top,textvariable=volume).pack()
        btn_cerrar= Button(top,text="Cerrar",command=top.destroy).pack()
        
    btn = Button(root,text="Volumen",command=open).pack(padx=50,pady=50)
    def mostrar():
        ventana.root.mainloop()

ventana.mostrar()


    
