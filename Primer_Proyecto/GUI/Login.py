from tkinter import *

from matplotlib.pyplot import tick_params
from Color import *
import sys
sys.path.append(r'C:\Users\sebas\Desktop\Jupyter\Primer_Proyecto')
from Negocio.Login import login as N
class login():
    loginFrm = Tk()
    #Variable tkinter 
    usr=StringVar()
    passw=StringVar()
    #Funciones 
    def login():
        key=N.trylog(login.usr.get(),login.passw.get())
        if key==True:
            pass
        if key==False:
            Label(login.loginFrm,text="Usuario o contraseña incorrectos").pack()
    #Visuales
    loginFrm.title("Login")
    #loginFrm.iconbitmap(r"C:\Users\sebas\Desktop\Jupyter\Primer_Proyecto\GUI\img\login.ico")
    loginFrm.geometry("1340x720+2+5")
    loginFrm.configure(bg=Color.DGRAY)
    #Objetos
    frame=LabelFrame(loginFrm,bg=Color.LGRAY,padx=100,pady=70,borderwidth=0)
    usuarioLbl=Label(frame,text="Usuario",background=Color.LGRAY,foreground=Color.White)
    usuarioTxt=Entry(frame,bg=Color.LGRAY2,borderwidth=0,textvariable=usr)
    passTxt=Entry(frame,bg=Color.LGRAY2,borderwidth=0,textvariable=passw)
    passLbl=Label(frame,text="Contraseña",background=Color.LGRAY,foreground=Color.White)
    loginBtn=Button(frame,text="Login",bg=Color.DBLUE,borderwidth=0,fg=Color.White,cursor="hand2",padx=5,pady=5,command=login)
    #Placing
    usuarioLbl.pack(pady=1)
    usuarioTxt.pack()
    passLbl.pack(pady=1)
    passTxt.pack()
    loginBtn.pack(pady=40)
    frame.pack(pady=150,padx=100)
    def placing():
        login.loginFrm.mainloop()
login.placing()