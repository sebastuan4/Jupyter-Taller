from tkinter import *

root=Tk()
#Label---------------------------------------------------------------------------------------------------------

lbl_Calculadora = Label(root, text="Calculadora") 
lbl_Ingresar = Label(root, text="Por favor ingrese 2 numeros")

#TextBox---------------------------------------------------------------------------------------------------------
"""
Width Aumenta el tamaño horizontal
get() obtiene el valor ingresado en la caja de texto
insert() añade texto
delete() borra el texto
"""
txt_Operacion = Entry(root, width=50)

#Botones---------------------------------------------------------------------------------------------------------
"""
padx aumenta el tamaño horizontal
command toma el nombre de funcion para el boton, solo el nombre por eso no usa ()
fg cambia el color del texto Tanto fg como bg funcionan con codigo de colores hexadecimales
bg cambia el color del fondo
"""
#Haciendo el boton funcionar
def calcular():

    stringOperacion = txt_Operacion.get()
    stringSlit=[]
    for letras in stringOperacion:
        match letras:
            case "*":
                stringSlit= stringOperacion.split("*")
                lbl_resultado = Label(root,text=f"Resultado:{int(stringSlit[0])*int(stringSlit[1])}").grid(row=4,column=0)
            case "/":
                stringSlit= stringOperacion.split("/")
                lbl_resultado = Label(root,text=f"Resultado:{int(stringSlit[0])/int(stringSlit[1])}").grid(row=4,column=0)
            case "+":
                stringSlit= stringOperacion.split("+")
                lbl_resultado = Label(root,text=f"Resultado:{int(stringSlit[0])+int(stringSlit[1])}").grid(row=4,column=0)
            case "-":
                stringSlit= stringOperacion.split("-")
                lbl_resultado = Label(root,text=f"Resultado:{int(stringSlit[0])-int(stringSlit[1])}").grid(row=4,column=0)
   

btn_Calcular = Button(root,text="Calcular",padx=20,command=calcular,bg="#323136",fg="white")#Padx aumenta el tamaño horizontal

#Mostando-----------------------------------------------------------------------------------------------------
lbl_Calculadora.grid(row=0,column=0)
lbl_Ingresar.grid(row=1,column=0) #La manera de ubicar es relativa
txt_Operacion.grid(row=2,column=0)
btn_Calcular.grid(row=3,column=0)
root.mainloop()
