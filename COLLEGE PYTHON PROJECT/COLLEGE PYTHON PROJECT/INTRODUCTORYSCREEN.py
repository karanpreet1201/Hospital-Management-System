from tkinter import *
import time
import os

root=Tk()
photo=PhotoImage(file="photo1.png")
l=Label(root)
l.configure(image=photo)
l.place(x=0,y=0)
root.attributes("-fullscreen",True)
root.title("WELCOME SCREEN")

def doctor():
    os.system("DOCTORLOGINSCREEN.py")
def rec():
    os.system("LOGINSCREEN.py")
    
l0=Label(root,text=" WELCOME TO ",bg="white",fg="darkred",font=("Felix Titling",75,"bold","underline","italic"),borderwidth=0)
l1=Label(root,text=" HEALING TOUCH ",bg="white",fg="darkred",font=("Felix Titling",75,"italic","bold","underline"),borderwidth=0)
l2=Label(root,text=" HOSPITAL ",bg="white",fg="darkred",font=("Felix Titling",75,"italic","bold","underline"),borderwidth=0)
l3=Label(root,text="     WHO ARE YOU ?     ",bg="white",fg="darkred",font=("Felix Titling",40,"italic","bold","underline"),borderwidth=0)


b4=Button(root,text="    EXIT    ",bg="white",fg="black",font=("Engravers MT",15,"bold"),borderwidth=0,command=root.destroy)
b4.place(x=473,y=768)
b5=Button(root,text="RECEPTIONIST",bg="white",fg="black",font=("Engravers MT",15,"bold"),borderwidth=0,command=rec)
b6=Button(root,text="     DOCTOR     ",bg="white",fg="black",font=("Engravers MT",15,"bold"),borderwidth=0,command=doctor)
b5.place(x=260,y=680)
b6.place(x=610,y=680)




l0.place(x=150,y=50)
l1.place(x=80,y=220)
l2.place(x=260,y=380)
l3.place(x=250,y=550)

##def waitfn():
##    time.sleep(1)
##    root.destroy()
##    os.system("LOGINSCREEN.py")
##root.after(2000,waitfn)

root.mainloop()
