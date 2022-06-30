
from cProfile import label
from tkinter import *
#pip install ttkthemes
class login():
    loginFrm = Tk()
    #Paleta de colores-----------------------------------------------------------------------------------------------
    LGRAY = '#3e4042' # button color effects in the title bar 
    DGRAY = '#25292e' # window background color               
    RGRAY = '#10121f' # title bar color                       
    DBLUE = "#283593" #Color for buttons
    LGRAY2 = "#e0e0e0" #Color for textbox
    White = "#ffffff" #Fg white
    #Visuales
    loginFrm.title("Login")
    loginFrm.iconbitmap(r"C:\Users\sebas\Desktop\Jupyter\Primer Proyecto\GUI\img\login.ico")
    loginFrm.geometry("1340x720+2+5")
    loginFrm.configure(bg=DGRAY)
    frame=LabelFrame(loginFrm,bg=LGRAY,padx=100,pady=70,borderwidth=0)
    usuarioLbl=Label(frame,text="Usuario",background=LGRAY,foreground=White)
    usuarioTxt=Entry(frame,bg=LGRAY2,borderwidth=0)
    passTxt=Entry(frame,bg=LGRAY2,borderwidth=0)
    passLbl=Label(frame,text="Contraseña",background=LGRAY,foreground=White)
    loginBtn=Button(frame,text="Login",bg=DBLUE,borderwidth=0,fg=White,cursor="hand2",padx=5,pady=5)
    #Placing
    usuarioLbl.pack(pady=1)
    usuarioTxt.pack()
    passLbl.pack(pady=1)
    passTxt.pack()
    loginBtn.pack(pady=40)
    frame.pack(pady=150,padx=100)
    loginFrm.mainloop()