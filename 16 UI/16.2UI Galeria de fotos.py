from tkinter import *
from PIL import ImageTk,Image
class image_galery:
    root=Tk()
    index_Image=0
    #Ajustes visuales---------------------------------------------------------------------------------------------------------
    root.title("Galeria de fotos")
    root.resizable(1,1)
    root.iconbitmap(r'C:\Users\sebas\Desktop\Jupyter\16 UI\img\python.ico')
    #root.geometry("840x840")

    #Agregando una imagen con polimorfismo
    img_dirs=[r"C:\Users\sebas\Desktop\Jupyter\16 UI\img\python.png",r"C:\Users\sebas\Desktop\Jupyter\16 UI\img\python2.png",r"C:\Users\sebas\Desktop\Jupyter\16 UI\img\python3.jpeg"]
    def mostrar_imagen():  
        global img_resized
        my_img = Image.open(image_galery.img_dirs[image_galery.index_Image])
        img_resized=ImageTk.PhotoImage(my_img.resize((250,250)))
        image_tool=Label(image=img_resized)
        image_tool.grid(row=1,column=1,columnspan=3)
        status_bar = Label(text=f"Imagen {(image_galery.index_Image)+1} de {len(image_galery.img_dirs)}")
        status_bar.grid(row=3,column=3,columnspan=3,sticky=W+E)
        
    #Funciones para los botones
    def button_next():
        if(image_galery.index_Image!=3):
            image_galery.index_Image+=1
            image_galery.mostrar_imagen()
    def button_back():
        if(image_galery.index_Image!=0):
            image_galery.index_Image-=1
            image_galery.mostrar_imagen()

    #Definiendo los botones
    button_backk = Button(text="<<<",command=button_back)
    button_nextt = Button(text=">>>", command=button_next)

    #Definiendo barra de progreso
    
    #Mostrando
    def mostrarGUI():
        image_galery.mostrar_imagen()
        image_galery.button_backk.grid(row=2,column=1)
        image_galery.button_nextt.grid(row=2,column=3)
        image_galery.root.mainloop()

image_galery.mostrarGUI()

    
