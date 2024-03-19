from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
import sqlite3
from datetime import datetime
from datetime import date
from tkinter.ttk import Treeview
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root=Tk()
root.attributes("-fullscreen",True)

pid=StringVar()
pname=StringVar()
pgen=StringVar()
pdob=StringVar()
pconm=StringVar()
pemail=StringVar()
padd=StringVar()
psymp=StringVar()
docapp=StringVar()
spec=StringVar()
date=StringVar()
time=StringVar()
nxtdate=StringVar()
meds=StringVar()
pid1=StringVar()

def showdetails1():
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        q=pid1.get()
        c.execute("select * from doctor1 where pid=?",(q,))
        data=c.fetchall()
        for row in data:
            pid.set(str(row[0]))
            pname.set(str(row[1]))
            pgen.set(str(row[2]))
            pdob.set(str(row[3]))
            pconm.set(str(row[4]))
            pemail.set(str(row[5]))
            padd.set(str(row[6]))
            psymp.set(str(row[7]))
            docapp.set(str(row[8]))
            spec.set(str(row[9]))
            date.set(str(row[10]))
            time.set(str(row[11]))
            nxtdate.set(str(row[12]))
            meds.set(str(row[13]))

        con.close()

def showdetails():
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        n=pid.get()
        c.execute("select * from appointments where pid=?",(n,))
        data=c.fetchall()
        for row in data:
            pname.set(str(row[1]))
            pgen.set(str(row[2]))
            pdob.set(str(row[3]))
            pconm.set(str(row[4]))
            pemail.set(str(row[5]))
            padd.set(str(row[6]))
            docapp.set(str(row[7]))
            spec.set(str(row[8]))
            date.set(str(row[9]))
            time.set(str(row[10]))
            
        con.close()
        
def clear():
    pid.set("")
    pname.set("")
    pgen.set("")
    pdob.set("")
    pconm.set("")
    pemail.set("")
    padd.set("")
    psymp.set("")
    docapp.set("")
    spec.set("")
    date.set("")
    time.set("")
    nxtdate.set("")
    meds.set("")
    pid1.set("")
def send_email():
        # get the input values from the user
        recipient = pemail.get()
        subject = "GREETINGS OF THE DAY"
        body1 ="YOUR NEXT VISIT IS:"
        body1_1 = nxtdate.get()
        body2 = "\nPATIEENT NAME:"
        body2_1=pname.get()
        body3="\n\nCONTACT NUMBER:"
        body3_1=pconm.get()
        body4="\n\nSYMPTOMS:"
        body4_1=psymp.get()
        body5="\n\nMEDICINES PRESCRIBED:"
        body5_1=meds.get()

        final_body=body1+str(body1_1)+body2+str(body2_1)+body3+str(body3_1)+body4+str(body4_1)+body5+str(body5_1)
        
        # create a message object
        message = MIMEMultipart()
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(final_body, 'plain'))
        
        # create an SMTP object and login
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login('narangshiven88@gmail.com', 'jpaulrbshyxanqrg')
        
        # send the email
        smtp_obj.sendmail('narangshiven88@gmail.com', recipient, message.as_string())
        
        # close the connection
        smtp_obj.quit()        

def add():

        
        
        
        a=pid.get()
        b=pname.get()
        c=pgen.get()
        d=pdob.get()
        e=int(pconm.get())
        f=pemail.get()
        g=padd.get()
        h=psymp.get()
        i=docapp.get()
        j=spec.get()
        k=date.get()
        l=time.get()
        m=nxtdate.get()
        n=meds.get()
        
        con=sqlite3.connect("hospital.sqlite")
        cu=con.cursor()

        cu.execute("insert into doctor1(pid,pname,pgen,pdob,pconm,pemail,padd,psymp,docapp,spec,date,time,nxtdate,meds) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i,j,k,l,m,n))

        con.commit()
        messagebox.showinfo("Great","Thank You")
        send_email()
        clear()
        
def delete():
           # Get selected item to Delete
           
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            pc=pid1.get()
            ans=messagebox.askyesno("ALERT","ARE YOU SURE")
            if ans==True:
                c.execute("delete from doctor1 where pid=?",(pc,))
                c.execute("delete from appointments where pid=?",(pc,))

                con.commit()
                messagebox.showinfo("THANK YOU","1 RECORD DELETED...")            
            clear()

def update():
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
                        
        a=pid1.get()
        b=pname.get()
        p=pgen.get()
        d=pdob.get()
        e=int(pconm.get())
        f=pemail.get()
        g=padd.get()
        h=psymp.get()
        i=docapp.get()
        j=spec.get()
        k=date.get()
        l=time.get()
        m=nxtdate.get()
        n=meds.get()
                    
        c.execute("update doctor1 set pname=?,pgen=?,pdob=?,pconm=?,pemail=?,padd=?,psymp=?,docapp=?,spec=?,date=?,time=?,nxtdate=?,meds=? where pid=?",(b,p,d,e,f,g,h,i,j,k,l,m,n,a))
        c.execute("update appointments set pname=?,gen=?,dob=?,conm=?,email=?,address=?,dr=?,spec=?,date=?,time=? where pid=?",(b,p,d,e,f,g,i,j,k,l,a))
        con.commit()
        messagebox.showinfo("THANK YOU","1 RECOED UPDATED...")
        clear()
            
mainframe=Frame(root)
f1=Frame(root,bd=5,bg="teal",relief=RAISED)
f2=Frame(root,bd=5,bg="beige",relief=RAISED)
f3=Frame(root,bd=5,bg="darkgray",relief=RAISED)
f4=Frame(root,bd=5,relief=RAISED,background="darkgrey")

l1=Label(f1,bg="teal",fg="beige",text="Hospital Management System",font=("Berlin Sans FB Demi",26,"bold"))
l2=Label(f2,bg="beige",text="Menu",font=("Berlin Sans FB Demi",25,"bold"))
l3=Label(f3,fg="black",bg="darkgray",text="Admin Dashboard",font=("Berlin Sans FB Demi",22,"bold"))
l4=Label(f4,fg="black",bg="darkgray",text="''",font=("Berlin Sans FB Demi",18,"bold"))
l5=Label(f4,fg="black",bg="darkgray",text="Medicines Cure",font=("Berlin Sans FB Demi",18,"bold"))
l6=Label(f4,fg="black",bg="darkgray",text="diseases,",font=("Berlin Sans FB Demi",18,"bold"))
l7=Label(f4,fg="black",bg="darkgray",text="but only",font=("Berlin Sans FB Demi",18,"bold"))
l8=Label(f4,fg="black",bg="darkgray",text="doctors can",font=("Berlin Sans FB Demi",18,"bold"))
l9=Label(f4,fg="black",bg="darkgray",text="cure patients",font=("Berlin Sans FB Demi",18,"bold"))
l10=Label(f4,fg="black",bg="darkgray",text="''",font=("Berlin Sans FB Demi",18,"bold"))
l11=Label(f4,fg="black",bg="darkgray",text="WELCOME",font=("Berlin Sans FB Demi",19,"bold"))

mainframe.place(x=190,y=110,height=740,width=1345)

f1.pack(side="top",fill=X)
f2.place(x=0,y=50,height=60,width=190)
f3.place(x=190,y=50,height=60,width=1346)
f4.place(x=0,y=110,height=753,width=190)

l1.pack(side="left")
l2.pack()
l3.pack(side="left")
l4.place(x=80,y=155)
l5.place(x=5,y=188)
l6.place(x=36,y=233)
l7.place(x=34,y=275)
l8.place(x=17,y=319)
l9.place(x=10,y=364)
l10.place(x=78,y=412)
l11.place(x=24,y=60)

i5=PhotoImage(file="EXIT.png")
b5=Button(f4,bg="lightgrey",bd=2,image=i5,relief=RAISED,command=root.destroy)
b5.place(x=0,y=595,height=150.6,width=181)

f8=Frame(mainframe,bd=5,relief=RIDGE)
f10=Frame(root,bd=5,bg="darkgrey",relief=RAISED)
    
f8.place(x=15,y=15,height=720,width=1308)
f10.place(x=190,y=50,height=60,width=1346)

l8=Label(mainframe,fg="black",text="Patients Details",font=("Berlin Sans FB Demi",22,"bold"))
l9=Label(f8,fg="black",text="Patient Name",font=("Berlin Sans FB Demi",19,"bold"))
l20=Label(f8,fg="black",text="Patient ID",font=("Berlin Sans FB Demi",19,"bold"))

l10=Label(f8,fg="black",text="Gender",font=("Berlin Sans FB Demi",19,"bold"))
l11=Label(f8,fg="black",text="D.O.B",font=("Berlin Sans FB Demi",19,"bold"))
l12=Label(f8,fg="black",text="Contact No.",font=("Berlin Sans FB Demi",19,"bold"))
l13=Label(f8,fg="black",text="Email",font=("Berlin Sans FB Demi",19,"bold"))
l14=Label(f8,fg="black",text="Address",font=("Berlin Sans FB Demi",19,"bold"))

l15=Label(f10,fg="black",bg="darkgray",text="DOCTOR",font=("Berlin Sans FB Demi",25,"bold"))

l8.place(x=40,y=10)
l9.place(x=20,y=105)
l10.place(x=20,y=150)
l11.place(x=20,y=196)
l12.place(x=20,y=245)
l13.place(x=20,y=295)
l14.place(x=600,y=60)
l20.place(x=20,y=60)

l15.pack(side="left")

e1=Entry(f8,width=26,font=(22),textvar=pid)
e1.place(x=207,y=65)
e2=Entry(f8,width=33,font=(22),textvar=pname,borderwidth=2,relief=GROOVE)
e2.place(x=207,y=108)
e3=Entry(f8,width=33,font=(22),textvar=pgen,borderwidth=2,relief=GROOVE)
e3.place(x=207,y=154)
e4=Entry(f8,width=33,font=(22),textvar=pdob,borderwidth=2,relief=GROOVE)
e4.place(x=207,y=200)
e5=Entry(f8,width=33,font=(22),textvar=pconm,borderwidth=2,relief=GROOVE)
e5.place(x=207,y=250)
e6=Entry(f8,width=39,font=(22),textvar=pemail,borderwidth=2,relief=GROOVE)
e6.place(x=141,y=300)
e7=Entry(f8,width=48,font=(22),textvar=padd,borderwidth=2,relief=GROOVE)
e7.place(x=730,y=65)

l17=Label(f8,fg="black",text="Symptoms",font=("Berlin Sans FB Demi",19,"bold"))
l18=Label(f8,fg="black",text="Doctor Appointed",font=("Berlin Sans FB Demi",19,"bold"))
l21=Label(f8,fg="black",text="Doctor Specialization",font=("Berlin Sans FB Demi",19,"bold"))
l19=Label(f8,fg="black",text="Date(DD/MM/YYYY)",font=("Berlin Sans FB Demi",19,"bold"))
l20=Label(f8,fg="black",text="Time(HH:MM:SS)",font=("Berlin Sans FB Demi",19,"bold"))
l26=Label(f8,fg="black",text="Next Visit Date(DD/MM/YYYY)",font=("Berlin Sans FB Demi",19,"bold"))
l27=Label(f8,fg="black",text="Medicines Prescribed",font=("Berlin Sans FB Demi",19,"bold"))
l28=Label(f8,fg="black",text="Select Patient ID To Update Or Delete",font=("Berlin Sans FB Demi",19,"bold"))

l17.place(x=600,y=105)
l18.place(x=600,y=150)
l21.place(x=600,y=196)
l19.place(x=600,y=245)
l20.place(x=600,y=295)
l26.place(x=20,y=400)
l27.place(x=20,y=470)
l28.place(x=20,y=530)

e8=Entry(f8,width=48,font=(22),textvar=psymp,borderwidth=2,relief=GROOVE)
e8.place(x=730,y=108)
e9=Entry(f8,width=36,font=(22),textvar=docapp,borderwidth=2,relief=GROOVE,state="disabled")
e9.place(x=850,y=154)
e10=Entry(f8,width=36,font=(22),textvar=spec,borderwidth=2,relief=GROOVE,state="disabled")
e10.place(x=850,y=200)
e11=Entry(f8,width=25,font=(22),textvar=date,borderwidth=2,relief=GROOVE,state="disabled")
e11.place(x=850,y=250)
e12=Entry(f8,width=25,font=(22),textvar=time,borderwidth=2,relief=GROOVE,state="disabled")
e12.place(x=850,y=300)
e13=Entry(f8,width=25,font=(22),textvar=nxtdate,borderwidth=2,relief=GROOVE)
e13.place(x=400,y=406)
e14=Entry(f8,width=84,font=(22),textvar=meds,borderwidth=2,relief=GROOVE)
e14.place(x=330,y=476)
e15=Entry(f8,width=20,font=(22),textvar=pid1)

e15.place(x=533,y=535)

b1=Button(f8,bg="lightgrey",text="Add",bd=5,font=("Berlin Sans FB Demi",21,"bold"),relief=RAISED,command=add)
b2=Button(f8,bg="green",text="Update",bd=5,font=("Berlin Sans FB Demi",21,"bold"),relief=RAISED,command=update)
b3=Button(f8,bg="red",text="Delete",bd=5,font=("Berlin Sans FB Demi",21,"bold"),relief=RAISED,command=delete)
b4=Button(f8,bg="darkgray",text="Clear",bd=5,font=("Berlin Sans FB Demi",21,"bold"),relief=RAISED,command=clear)
b5=Button(f8,bg="lightgrey",text="OK",bd=5,font=("Berlin Sans FB Demi",13,"bold"),relief=RAISED,command=showdetails)
b6=Button(f8,bg="lightgrey",text="Fill Data",bd=5,font=("Berlin Sans FB Demi",14,"bold"),relief=RAISED,command=showdetails1) 

b1.place(x=50,y=600)
b2.place(x=395,y=600)
b3.place(x=780,y=600)
b4.place(x=1150,y=600)
b5.place(x=520,y=57)
b6.place(x=800,y=525)


root.mainloop()
