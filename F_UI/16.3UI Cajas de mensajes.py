from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Labelframe

from matplotlib.pyplot import title
class message:
    root=Tk()
   
    msg=["showinfo","showwarning","showerror","askquestion","askokcancel","askyesno"]
    def popUp():
        for val in message.msg:
            getattr(messagebox,val)("title",f"Message {val}")
    frame=Labelframe(root,text="Text",pad=20)
    Button(frame,text="PopUp",command=popUp).pack()
    frame.pack(padx=20,pady=20)

message.root.mainloop()



    
