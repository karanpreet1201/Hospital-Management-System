from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root=Tk()
root.attributes("-fullscreen",True)
root.title("LOGIN SCREEN")

def create_clicked():
    con=sqlite3.connect("hospital.sqlite")
    c=con.cursor()
    name=n.get()
    passw=P.get()
    c.execute("select * from createuser where username=? and password=?",(name,passw))
    data=c.fetchall()
    if (len(data)==0):
        messagebox.showerror("Alert!","Username/Password Does not Exist")
        clear_clicked()
    else:
        messagebox.showinfo("Great!","Sucessfully Logged In")
        root.destroy()
        con.close()
        os.system("MENUSCREEN.py")

    
def clear_clicked():
    n.set("")
    P.set("")
    e1.focus()


def button_clicked():
    os.system("CREATESCREEN.py")


n=StringVar()
P=StringVar()

i1=PhotoImage(file="PHOTO2.png")

l1=Label(root,i=i1)

f1=Frame(root,highlightthickness=5,highlightbackground="red",bg="oldlace")
photo=PhotoImage(file="PHOTO3.png")
l=Label(f1)
l.configure(image=photo)
l.place(x=538,y=0)


p=PhotoImage(file="PHOTO4.png")
l=Label(f1)
l.configure(image=p)
l.place(x=0,y=0)


e1=Entry(f1,width="40",textvariable=n,font=("Bahnschrift SemiBold",16,"bold"))
e2=Entry(f1,width="40",show="*",textvariable=P,font=("Bahnschrift SemiBold",16,"bold"))

l0=Label(f1,text="Welcome To Healing Touch Hospital",font=("Franklin Gothic Demi Cond",25,"bold"))
l3=Label(f1,text="LOGIN HERE",fg="darkblue",font=("Engravers MT",30,"bold"))
l4=Label(f1,text="USERNAME",font=("Britannic Bold",20,"bold"))
l5=Label(f1,text="PASSWORD",font=("Britannic Bold",20,"bold"))
l6=Label(f1,text=" Sign up and discover a great \n amount of new oppurtunities ! ",fg="black",bg="lightblue",font=("Monotype Corsiva",20,"italic","bold"),borderwidth=0)
l7=Label(root,text="NEW HERE? ",fg="black",bg="lightblue",font=("Berlin Sans FB",30,"italic","bold"),borderwidth=0)


f1.place(x=220,y=110,width=1100,height=650)

b1=Button(f1,text="Login",bg="black",fg="white",font=("Engravers MT",15,"bold"),borderwidth=0,command=create_clicked)
b2=Button(f1,text="Clear",bg="black",fg="white",font=("Engravers MT",15,"bold"),borderwidth=0,command=clear_clicked)
b3=Button(f1,text="Exit",bg="black",fg="white",font=("Engravers MT",15,"bold"),borderwidth=0,command=root.destroy)
b4=Button(f1,text="Sign Up",bg="lightblue",fg="black",font=("Engravers MT",15,"bold"),borderwidth=0,command=button_clicked)

l1.pack()
l3.place(x=137,y=30)
l0.place(x=20,y=150)
l4.place(x=50,y=250)
l5.place(x=50,y=400)
l6.place(x=580,y=200)
l7.place(x=850,y=200)

e1.place(x=50,y=330)
e2.place(x=50,y=470)

b1.place(x=15,y=570)
b2.place(x=220,y=570)
b3.place(x=430,y=570)
b4.place(x=680,y=350)

e1.focus()

root.mainloop()
