from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
import sqlite3
from datetime import datetime
from datetime import date
from tkinter.ttk import Treeview
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


root=Tk()
root.attributes("-fullscreen",True)

specvar1=StringVar()
specvar2=StringVar()
namevar=StringVar()
feevar=StringVar()
nvar=StringVar()
pnmvar=StringVar()
genvar=StringVar()
dtvar1=StringVar()
cnmvar=StringVar()
evar=StringVar()
avar=StringVar()
smpvar=StringVar()
drvar=StringVar()
dtvar2=StringVar()
tmvar=StringVar()
pnmvar1=StringVar()
pnmvar2=StringVar()
specvar3=StringVar()
specvar4=StringVar()
namevar1=StringVar()
namevar2=StringVar()
docid=StringVar()
docid1=StringVar()
pid=StringVar()
pid1=StringVar()
pid2=StringVar()


def clear_clicked():
    p=pnmvar.set("")
    g=genvar.set("")
    d=dtvar1.set("")
    c=cnmvar.set("")
    e=evar.set("")
    a=avar.set("")
    s=smpvar.set("")
    dr=drvar.set("")
    sp=specvar2.set("")
    dt=dtvar2.set("")
    t=tmvar.set("")

def deletepages():
    for i in mainframe.winfo_children():
        i.destroy()

def home():
    deletepages()
    f12=Frame(root,bd=5,bg="darkgray",relief=RAISED)
    f12.place(x=190,y=50,height=60,width=1346)
    
    f13=Frame(mainframe,bd=5,relief=RAISED)
    f13.place(x=30,y=30,height=700,width=1280)
    
    l21=Label(f12,fg="black",bg="darkgray",text="Admin Dashboard",font=("Berlin Sans FB Demi",22,"bold"))
    l21.pack(side="left")

    l22=Label(mainframe,fg="black",text="Today's appointment",font=("Berlin Sans FB Demi",22,"bold"))
    l22.place(x=40,y=15)

##    f14=Frame(f13,bd=5,relief=RAISED)
##    f14.place(x=30,y=30,height=400,width=900)

##    import tkinter as tk
##    import sqlite3
##
##    conn = sqlite3.connect("hospital.sqlite")
##    cursor = conn.cursor()
##    cursor.execute("SELECT * FROM appointments")
##    rows = cursor.fetchall()
##    
##    for i, column_title in enumerate(["NAME   ", "   GENDER   ", "DOB","CONTACT NUMBER","EMAIL","ADDRESS","SYMPTOMS","DOCTOR","SPECIALIZATION","DATE","TIME"]):
##        tk.Label(f14, text=column_title, relief="solid").grid(row=0, column=i)
##
##    for j, row in enumerate(rows):
##        for i, item in enumerate(row):
##            tk.Label(f14, text=item).grid(row=j + 1, column=i)

    # Create an instance of Style widget
    style = ttk.Style()
    style.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5","C6","C7","c8","c9","c10","c11"), show='headings', height=31)
    tree.column("# 1",width="110")
    tree.heading("# 1", text="PATIENT ID")

    tree.column("# 2",width="110")
    tree.heading("# 2", text="NAME")
    tree.column("# 3",width="110")
    tree.heading("# 3", text="GENDER")
    tree.column("# 4",width="110")
    tree.heading("# 4", text="DOB")
    tree.column("# 5",width="125")
    tree.heading("# 5", text="CONTACT NUMBER")
    tree.column("# 6",width="110")
    tree.heading("# 6", text="EMAIL")
    tree.column("# 7",width="110")
    tree.heading("# 7", text="ADDRESS")
##    tree.column("# 8",width="100")
##    tree.heading("# 8", text="SYMPTOMS")
    tree.column("# 8",width="110")
    tree.heading("# 8", text="DOCTOR")
    tree.column("# 9",width="110")
    tree.heading("# 9", text="SPECIALIZATION")
    tree.column("# 10",width="110")
    tree.heading("# 10", text="DATE")
    tree.column("# 11",width="100")
    tree.heading("# 11", text="TIME")

    con=sqlite3.connect("hospital.sqlite")
    c=con.cursor()
    s=c.execute("SELECT * FROM appointments")
    table_data=c.fetchall()

    for i, data in enumerate(table_data):
        tree.insert("", "end", text=(i), values=data)

    vsb=ttk.Scrollbar(f13,orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    
    tree.place(x=18,y=30)

def doctor():
    
    f7=Frame(root,bd=5,bg="darkgray")
    
    f7.place(x=190,y=50,height=60,width=1346)

    l7=Label(f7,fg="black",bg="darkgray",text="Doctor Dashboard",font=("Berlin Sans FB Demi",22,"bold"))

    l7.place(x=0,y=0)
    
    def specialization():


        


##        def getrow(event):
##            rowid=tree.identify(event.y)
##            item=tree.item(trv.focus())
##            e1.set(item['values'][0])
            
    
            
            

        def clear():
            specvar2.set("")
        
        def insertclicked():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            s=specvar2.get()
            now = datetime.now()
            ct = now.strftime("%H:%M:%S")
            
            c.execute("insert into specialization(spec,date) values (?,?)",(s,ct))
        
            con.commit()
            if(s==""):
                messagebox.showerror
            messagebox.showinfo("Great!","1Record Added")
            
            clear()
            specvar3.set("")
            con.close()
            
##            tree.insert("", "end", text=(table_data[-1]), values=data)

        deletepages()
        
        f5=Frame(mainframe,bd=5,relief=RIDGE)
        f6=Frame(mainframe,bd=5,relief=RIDGE)
    
        f5.place(x=40,y=40,height=500,width=600)
        f6.place(x=700,y=40,height=700,width=600)
         # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(f6, column=("c1", "c2"), show='headings', height=26)
        
        tree.column("# 1",width="210")
        tree.heading("# 1", text="Specialization")
        tree.column("# 2",width="210")
        tree.heading("# 2", text="Current Date")
        
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        s=c.execute("SELECT * FROM specialization")
        table_data=c.fetchall()

        for i, data in enumerate(table_data):
            tree.insert("", "end", text=(i), values=data)

        
        
        vsb=ttk.Scrollbar(f6,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)
    
        tree.place(x=75,y=110)

            

        def selectItem(event):
            item = tree.selection()[0]
##            print("you clicked on", tree.item(item, "text"))
##            print("column values:", tree.item(item, "values"))
            specvar2.set(tree.item(item, "values")[0])

        

##        def search_treeview(tree, search_string):
##            for item in tree.get_children():
##                item_text = tree.item(item, "text")
##            if item_text == search_string:
##                tree.see(item)
##                tree.selection_set(item)
##                return True
##            return False
##        
        def update_clicked():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            ic=specvar2.get()
            now = datetime.now()
            ct = now.strftime("%H:%M:%S")
            ne=specvar3.get()
            
            c.execute("update specialization set spec=?,date=? where spec=?",(ne,ct,ic))
            con.commit()
            messagebox.showinfo("THANK YOU","1 RECOED UPDATED...")
            specvar2.set("")
            specvar3.set("")
            e1.focus()

        def getspec():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            c.execute("select spec from specialization")
            data=c.fetchall()
            l=[]
            for row in data:
                l.append(row[0])
            e1['values']=l
            con.close()

        def delete():
           # Get selected item to Delete
##            selected_item = tree.selection()[0]
##            tree.delete(selected_item)
##            
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            ic=specvar2.get()
            ans=messagebox.askyesno("ALERT","ARE YOU SURE")
            if ans==True:
                c.execute("delete from specialization where spec=?",(ic,))
                con.commit()
                messagebox.showinfo("THANK YOU","1 RECORD DELETED...")
                selected_item = tree.selection()[0]
                tree.delete(selected_item)
                clear_clicked()
                t=[0]
                e1['values']=t
                

                
                getspec()
##            else:
##                for i, data in enumerate(table_data):
##                    tree.insert("", "end", text=(i), values=data)
                
            specvar2.set("")
            e1.focus()

                
            
            con.close()

        def show():
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            s=c.execute("SELECT * FROM specialization")
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)
            specvar4.set("")

        def search_items():
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
##            print(str(specvar4.get()))
            s=c.execute("SELECT * FROM specialization where spec=?",(str(specvar4.get()),))
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)


        

        
        
        l4=Label(mainframe,fg="black",text="Doctor Specialization",font=("Berlin Sans FB Demi",22,"bold"))
        l5=Label(mainframe,fg="black",text="All Specializations",font=("Berlin Sans FB Demi",22,"bold"))
        l6=Label(f5,fg="black",text="Enter Doctor Specialization",font=("Berlin Sans FB Demi",22,"bold"))
        l9=Label(f6,fg="black",text="Search",font=("Berlin Sans FB Demi",22,"bold"))
        l20=Label(f5,fg="black",text="Enter Updated Specialization",font=("Berlin Sans FB Demi",22,"bold"))

    
        l4.place(x=55,y=21)
        l5.place(x=720,y=24)
        l6.place(x=20,y=30)
        l9.place(x=15,y=40)
        l20.place(x=20,y=143)


        e1=Entry(f5,width=42,font=(22),textvar=specvar2,borderwidth=5,relief=GROOVE)
        tree.bind("<ButtonRelease-1>", selectItem)
        e3=Entry(f5,width=42,font=(22),textvar=specvar3,borderwidth=5,relief=GROOVE)

        e2=Entry(f6,width=23,font=(22),textvar=specvar4,borderwidth=5,relief=GROOVE)

        e1.place(x=20,y=80)
        e2.place(x=130,y=45)
        e3.place(x=20,y=200)
        
##        search_item = search_treeview(tree,e2)
##        if search_item:
##            tree.selection_set(search_item)
##            tree.see(search_item)


        b6=Button(f5,width=13,text="Add",bg="blue",fg="white",font=("Berlin Sans FB Demi",22,"bold"),command=insertclicked)
        b7=Button(f5,width=13,text="Update",bg="green",fg="white",font=("Berlin Sans FB Demi",22,"bold"),command=update_clicked)
        b8=Button(f5,width=13,text="Clear",bg="orange",fg="white",font=("Berlin Sans FB Demi",22,"bold"),command=clear)
        b9=Button(f5,width=13,text="Delete",bg="gray",fg="white",font=("Berlin Sans FB Demi",22,"bold"),command=delete)
        b10=Button(f6,width=10,text="Search",bg="purple",fg="white",font=("Berlin Sans FB Demi",10,"bold"),command=search_items)
        b11=Button(f6,width=10,text="Show All",bg="magenta",fg="white",font=("Berlin Sans FB Demi",10,"bold"),command=show)

        b6.place(x=10,y=320)
        b7.place(x=325,y=320)
        b8.place(x=10,y=400)
        b9.place(x=325,y=400)
        b10.place(x=400,y=47)
        b11.place(x=485,y=47)
        e1.focus()

    def mgdoctor():
        deletepages()

        
        def getspec():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            c.execute("select spec from specialization")
            data=c.fetchall()
            if len(data)>0:
                l=[]
            for row in data:
                l.append(row[0])
            e3["values"]=l
            con.close()
        def showdetails(event):
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
##            ic=txtspecvar1.get()
            c.execute("select * from specialization where spec=?",(ic,))
            data=c.fetchall()
            for row in data:
                specvar1.set(row[0])
##                txtrate.set(str(row[2]))
##                txtqoh.set(str(row[3]))
            con.close()


                    
        def getdoccode():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            c.execute("select id from doctor")
            data=c.fetchall()
            if len(data)==0:
                dc=1001
            else:
                dc=data[-1][0]+1
            docid.set(str(dc))
            con.close()
            
        def clear():
            docid.set("")
            specvar1.set("")
            namevar.set("")
            feevar.set("")
            nvar.set("")
            getdoccode()


        
        def insert():
            
                con=sqlite3.connect("hospital.sqlite")
                c=con.cursor()
                dc=int(docid.get())
                s=specvar1.get()
                nm=namevar.get()
                f=int(feevar.get())
                n=int(nvar.get())
                c.execute("insert into doctor(id,spec,name,fee,contact) values(?,?,?,?,?)",(dc,s,nm,f,n))
                con.commit()
                messagebox.showinfo("Great!","1Record Added")
                
                
                            
                specvar1.set("")
                namevar.set("")
                feevar.set("")
                nvar.set("")
                e3.focus()
                getdoccode()
            
        
        def selectItem(event):
            item = tree.selection()[0]
##            print("you clicked on", tree.item(item, "text"))
##            print("column values:", tree.item(item, "values"))
            
            docid.set(tree.item(item, "values")[0])
            specvar1.set(tree.item(item, "values")[1])
            namevar.set(tree.item(item, "values")[2])
            feevar.set(tree.item(item, "values")[3])
            nvar.set(tree.item(item, "values")[4])

        
        f9=Frame(mainframe,bd=5,relief=RIDGE)
        f10=Frame(mainframe,bd=5,relief=RIDGE)

        f9.place(x=30,y=30,height=650,width=600)
        f10.place(x=650,y=20,height=700,width=650)
         # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(f10, column=("c1", "c2","c3","c4","c5"), show='headings', height=26)
        tree.column("# 1",width="70")
        tree.heading("# 1", text="ID")

        tree.column("# 2",width="140")
        tree.heading("# 2", text="Specialization")
        tree.column("# 3",width="140")
        tree.heading("# 3", text="Doctor Name")
        tree.column("# 4",width="100")
        tree.heading("# 4", text="Fees")
        tree.column("# 5",width="140")
        tree.heading("# 5", text="Contact no.")

        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        s=c.execute("SELECT * FROM doctor")
        table_data=c.fetchall()

        for i, data in enumerate(table_data):
            tree.insert("", "end", text=(i), values=data)

    


        
        vsb=ttk.Scrollbar(f10,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)
    
        tree.place(x=13,y=110)
        
        
        def delete():
           # Get selected item to Delete
##            selected_item = tree.selection()[0]
##            tree.delete(selected_item)
##            
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            ic=specvar1.get()
            ans=messagebox.askyesno("ALERT","ARE YOU SURE")
            if ans==True:
                c.execute("delete from doctor where spec=?",(ic,))
                con.commit()
                messagebox.showinfo("THANK YOU","1 RECORD DELETED...")
                selected_item = tree.selection()[0]
                tree.delete(selected_item)

                clear_clicked()
                l=[0]
                e3['values']=1
                getspec()
            specvar1.set("")
            namevar.set("")
            feevar.set("")
            nvar.set("")
            e3.focus()
            getdoccode()

##        def show()
        def update_clicked():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            ic=specvar1.get()
            ne=namevar.get()
            f=feevar.get()
            ct=nvar.get()            
            
            
            c.execute("update doctor set name=?,fee=?,contact=? where spec=?",(ne,f,ct,ic))
            con.commit()
            messagebox.showinfo("THANK YOU","1 RECOED UPDATED...")

            specvar1.set("")
            namevar.set("")
            feevar.set("")
            nvar.set("")
            e3.focus()
            getdoccode()


            
##
        def show():
            namevar1.set("")
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            s=c.execute("SELECT * FROM doctor")
            table_data=c.fetchall()
            

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)
                
        def search_items():
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
##            print(str(specvar4.get()))
            s=c.execute("SELECT * FROM doctor where id=?",(str(docid1.get()),))
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)

            



        l4=Label(mainframe,fg="black",text="Add Doctor",font=("Berlin Sans FB Demi",22,"bold"))
        l5=Label(mainframe,fg="black",text="Doctor Details",font=("Berlin Sans FB Demi",22,"bold"))
        l10=Label(f9,fg="black",text="Specialization",font=("Berlin Sans FB Demi",22,"bold"))
        l11=Label(f9,fg="black",text="Name",font=("Berlin Sans FB Demi",22,"bold"))
        l12=Label(f9,fg="black",text="Consultancy Fees",font=("Berlin Sans FB Demi",22,"bold"))
        l13=Label(f9,fg="black",text="Contact No.",font=("Berlin Sans FB Demi",22,"bold"))
        l14=Label(f10,fg="black",text="Enter Doctor ID",font=("Berlin Sans FB Demi",22,"bold"))
        l15=Label(f9,fg="black",text="Doctor ID",font=("Berlin Sans FB Demi",22,"bold"))
            
        l4.place(x=40,y=15)
        l5.place(x=660,y=8)
        l10.place(x=10,y=130)
        l11.place(x=10,y=220)
        l12.place(x=10,y=300)
        l13.place(x=10,y=390)
        l14.place(x=10,y=30)
        l15.place(x=10,y=56)

        e3=Combobox(f9,width="29",font=(15),textvar=specvar1)
        e3.bind("<<ComboboxClicked>>")
        e4=Entry(f9,width="30",font=(15),textvar=namevar,relief=GROOVE)
        e5=Entry(f9,width="30",font=(15),textvar=feevar,relief=GROOVE)
        e6=Entry(f9,width="30",font=(15),textvar=nvar,relief=GROOVE)
        e8=Entry(f9,width="30",font=("Calibri (Body)",15,"bold"),textvar=docid,relief=GROOVE,state="disabled")
        e7=Entry(f10,width="16",font=(15),textvar=docid1,relief=GROOVE)
        tree.bind("<ButtonRelease-1>", selectItem)

        e3.place(x=240,y=137)
        e4.place(x=244,y=227)
        e5.place(x=244,y=307)
        e6.place(x=244,y=397)
        e7.place(x=230,y=38)
        e8.place(x=244,y=63)

        b11=Button(f9,text="Add",width=16,font=("Berlin Sans FB Demi",20,"bold"),fg="white",bg="blue",command=insert)
        b12=Button(f9,text="Update",width=16,font=("Berlin Sans FB Demi",20,"bold"),fg="white",bg="green",command=update_clicked)
        b13=Button(f9,text="Clear",width=16,font=("Berlin Sans FB Demi",20,"bold"),fg="white",bg="orange",command=clear)
        b14=Button(f9,text="Delete",width=16,font=("Berlin Sans FB Demi",20,"bold"),fg="white",bg="gray",command=delete)
        b15=Button(f10,text="Search",font=("Berlin Sans FB Demi",14,"bold"),fg="white",bg="darkblue",command=search_items)
        b16=Button(f10,text="Show All",font=("Berlin Sans FB Demi",14,"bold"),fg="white",bg="orange",command=show)

        b11.place(x=25,y=470)
        b12.place(x=316,y=470)
        b13.place(x=25,y=570)
        b14.place(x=316,y=570)
        b15.place(x=430,y=35)
        b16.place(x=520,y=35)

        e3.focus()

        getspec()
        getdoccode()

        

    specialization()
        

    b11=Button(f7,width=20,text="Manage Speacialization",font=("Berlin Sans FB Demi",18,"bold"),fg="white",bg="gray",command=specialization)
    b12=Button(f7,width=20,text="Manage Doctor",font=("Berlin Sans FB Demi",18,"bold"),fg="white",bg="blue",command=mgdoctor)

    b11.place(x=270,y=0)
    b12.place(x=580,y=0)
##    getspec()
    
    

def appointment():
        
        
    def showdetails(event):
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        n=str(drvar.get())
        c.execute("select * from doctor where name=?",(n,))
        data=c.fetchall()
        for row in data:
            today = date.today()
            now = datetime.now()
            date1 = now.strftime('%d/%m/%Y')
            ct = now.strftime("%H:%M")
            specvar2.set(str(row[1]))
            dtvar2.set(date1)
            tmvar.set(ct)
        con.close()
    def getdoctor():
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        s=c.execute("select name from doctor")
        data=c.fetchall()
        if len(data)>0:
                l=[]
        for row in data:
            l.append(row[0])
        e8["values"]=l
        con.close()
        getpcode()
    def getpcode():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            c.execute("select pid from appointments")
            data=c.fetchall()
            if len(data)==0:
                pc=2001
            else:
                pc=data[-1][0]+1
            pid1.set(str(pc))
            con.close()

        
    def getgen():
        l=["Male","Female","Others"]
        e2["values"]=l

    def send_email():
        # get the input values from the user
        recipient = evar.get()
        subject = "GREETINGS OF THE DAY"
        body1=pid1.get()
        body2="YOUR PATIENT ID :"
        body3_1="\nNAME OF PATIENT:"
        body3=pnmvar.get()
        body4_1="\nCONATACT NUMBER:"
        body4=cnmvar.get()
        body5_1="\nDOCTOR APPOINTED:"
        body5=drvar.get()
        final_body=body2+str(body1)+body3_1+body3+body4_1+body4+body5_1+body5
        
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
            
        
            pc=pid1.get()
            p=pnmvar.get()
            g=genvar.get()
            d=dtvar1.get()
            c=int(cnmvar.get())
            e=evar.get()
            a=avar.get()
    ##        s=smpvar.get()
            dr=drvar.get()

            sp=specvar2.get()
            dt=dtvar2.get()
            t=tmvar.get()
            con=sqlite3.connect("hospital.sqlite")
            cu=con.cursor()

            cu.execute("insert into appointments(pid,pname,gen ,dob ,conm ,email ,address,dr,spec,date ,time ) values(?,?,?,?,?,?,?,?,?,?,?)",(pc,p,g,d,c,e,a,dr,sp,dt,t))
    ##        cu.execute("insert into appointment2(pid,pname,conm ,symp,spec,dr,date ,time ) values(?,?,?,?,?,?,?,?)",(pc,p,c,s,dr,dt,t))

            con.commit()
            messagebox.showinfo("Great","appointment Fixed")
                   
    ##        except:
    ##            messagebox.showerror("Error","Something Went Wrong")
            send_email()
            
            

            
            
            pid1.set("")
            pnmvar.set("")
            genvar.set("")
            dtvar1.set("")
            cnmvar.set("")
            evar.set("")
            avar.set("")
            drvar.set("")
            dtvar2.set("")
            tmvar.set("")
            specvar2.set("")
            getpcode()
         

    def clear_clicked():
            
            pnmvar.set("")
            genvar.set("")
            dtvar1.set("")
            cnmvar.set("")
            evar.set("")
            avar.set("")
            drvar.set("")

            specvar2.set("")
            dtvar2.set("")
            tmvar.set("")
            pid1.set("")
            getpcode()

            

        
        
        
            






    deletepages()
    
    f8=Frame(mainframe,bd=5,relief=RIDGE)
    f9=Frame(mainframe,bd=5,relief=RIDGE)
    f10=Frame(root,bd=5,bg="darkgrey",relief=RAISED)
    f11=Frame(mainframe,bd=5,relief=RIDGE)
    
    f8.place(x=15,y=15,height=450,width=640)
    f9.place(x=700,y=15,height=450,width=630)
    f10.place(x=190,y=50,height=60,width=1346)
    f11.place(x=10,y=500,height=240,width=1316)
    # Create an instance of Style widget
    style = ttk.Style()
    style.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(f11, column=("c1", "c2","c3","c4","c5","C6","C7","c8","c9","c10","c11"), show='headings', height=5)
    tree.column("# 1",width="110")
    tree.heading("# 1", text="Patient ID")

    tree.column("# 2",width="110")
    tree.heading("# 2", text="Patient Name")
    tree.column("# 3",width="110")
    tree.heading("# 3", text="Gender")
    tree.column("# 4",width="110")
    tree.heading("# 4", text="D.O.B")
    tree.column("# 5",width="110")
    tree.heading("# 5", text="Contact")
    tree.column("# 6",width="110")
    tree.heading("# 6", text="Email")
    tree.column("# 7",width="110")
    tree.heading("# 7", text="Address")
    tree.column("# 8",width="110")
    tree.heading("# 8", text="Doctor")
    tree.column("# 9",width="110")
    tree.heading("# 9", text="Specialization")
    tree.column("# 10",width="110")
    tree.heading("# 10", text="Apt Date")
    tree.column("# 11",width="110")
    tree.heading("# 11", text="Apt Time")

    con=sqlite3.connect("hospital.sqlite")
    c=con.cursor()
    s=c.execute("SELECT * FROM appointments")
    table_data=c.fetchall()

    for i, data in enumerate(table_data):
        tree.insert("", "end", text=(i), values=data)



    vsb=ttk.Scrollbar(f11,orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    
    tree.place(x=45,y=90)
    
    def update_clicked():
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        pc=pid1.get()
        a=pnmvar.get()
        b=genvar.get()
        d=dtvar1.get()
        e=int(cnmvar.get())
        f=evar.get()
        g=avar.get()
        i=drvar.get()
        j=dtvar2.get()
        k=tmvar.get()
        l=specvar2.get()
        

        c.execute("update appointments set pname=?,gen=?,dob=?,conm=?,email=?,address=?,dr=?,spec=?,date=?,time=? where pid=?",(a,b,d,e,f,g,i,j,k,l,pc))
        con.commit()
        messagebox.showinfo("THANK YOU","1 RECOED UPDATED...")
        clear_clicked()
        e1.focus()
        getpcode()

    def pname():
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            c.execute("select pname from appointments")
            data=c.fetchall()
            l=[]
            for row in data:
                l.append(row[0])
            e1['values']=l
            con.close()

    def delete():
           # Get selected item to Delete
##            selected_item = tree.selection()[0]
##            tree.delete(selected_item)
##            
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            pc=pid1.get()
            ans=messagebox.askyesno("ALERT","ARE YOU SURE")
            if ans==True:
                c.execute("delete from appointments where pid=?",(pc,))
                c.execute("delete from doctor1 where pid=?",(pc,))

                con.commit()
                messagebox.showinfo("THANK YOU","1 RECORD DELETED...")
                selected_item = tree.selection()[0]
                tree.delete(selected_item)
                con=sqlite3.connect("hospital.sqlite")
                c=con.cursor()
                ic=pnmvar.get()
        
                
                c.execute("delete from appointment2 where pid=?",(pc,))
                con.commit()

            

##                clear_clicked()
##                l=[0]
##                e1['values']=1
##                pname()
            
            clear_clicked()
            pid1.set("")
            getpcode()
            

            e1.focus()
            
            
##      


    def selectItem(event):
            item = tree.selection()[0]
##            print("you clicked on", tree.item(item, "text"))
##            print("column values:", tree.item(item, "values"))
            pid1.set(tree.item(item, "values")[0])

            pnmvar.set(tree.item(item, "values")[1])
            genvar.set(tree.item(item, "values")[2])
            dtvar1.set(tree.item(item, "values")[3])
            cnmvar.set(tree.item(item, "values")[4])
            evar.set(tree.item(item, "values")[5])
            avar.set(tree.item(item, "values")[6])
            
            drvar.set(tree.item(item, "values")[7])
            specvar2.set(tree.item(item, "values")[8])
            dtvar2.set(tree.item(item, "values")[9])
            tmvar.set(tree.item(item, "values")[10])
    def clear2():
        pid2.set("")
    def search_items():
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
##            print(str(specvar4.get()))
            s=c.execute("SELECT * FROM appointments where pid=?",(str(pid2.get()),))
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)
    def show():
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
            s=c.execute("SELECT * FROM appointments")
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)

##    def insert_message(phone, message):
##        con=sqlite3.connect("hospital.sqlite")
##        c=con.cursor()
##
####        cu.execute("insert into appointments(pid,pname,gen ,dob ,conm ,email ,address ,symp ,dr,spec,date ,time ) values(?,?,?,?,?,?,?,?,?,?,?,?)",(pc,p,g,d,c,e,a,s,dr,sp,dt,t))
##
##        con.execute("INSERT INTO messages (phone, message) VALUES (?, ?)", (phone, message))
##        con.commit()
        






    
    l8=Label(mainframe,fg="black",text="Patients Details",font=("Berlin Sans FB Demi",22,"bold"))
    l9=Label(f8,fg="black",text="Patient Name",font=("Berlin Sans FB Demi",19,"bold"))
    l20=Label(f8,fg="black",text="Patient ID",font=("Berlin Sans FB Demi",19,"bold"))

    l10=Label(f8,fg="black",text="Gender",font=("Berlin Sans FB Demi",19,"bold"))
    l11=Label(f8,fg="black",text="D.O.B",font=("Berlin Sans FB Demi",19,"bold"))
    l12=Label(f8,fg="black",text="Contact No.",font=("Berlin Sans FB Demi",19,"bold"))
    l13=Label(f8,fg="black",text="Email",font=("Berlin Sans FB Demi",19,"bold"))
    l14=Label(f8,fg="black",text="Address",font=("Berlin Sans FB Demi",19,"bold"))

    l15=Label(f10,fg="black",bg="darkgray",text="Appointment",font=("Berlin Sans FB Demi",25,"bold"))

    l8.place(x=40,y=10)
    l9.place(x=20,y=85)
    l10.place(x=20,y=130)
    l11.place(x=20,y=176)
    l12.place(x=20,y=225)
    l13.place(x=20,y=275)
    l14.place(x=20,y=350)
    l20.place(x=20,y=40)

    l15.pack(side="left")

    e1=Entry(f8,width=32,font=(22),textvar=pnmvar,borderwidth=2,relief=GROOVE)
    e1.place(x=240,y=88)
    e2=Combobox(f8,width=28,font=(22),textvar=genvar)
    e2.bind("<<ComboboxClicked>>")
    e2.place(x=240,y=134)
    e3=Entry(f8,width=32,font=(22),textvar=dtvar1,borderwidth=2,relief=GROOVE)
    e3.place(x=240,y=180)
    e4=Entry(f8,width=32,font=(22),textvar=cnmvar,borderwidth=2,relief=GROOVE)
    e4.place(x=240,y=230)
    e5=Entry(f8,width=32,font=(22),textvar=evar,borderwidth=2,relief=GROOVE)
    e5.place(x=240,y=280)
    e6=Entry(f8,width=32,font=(22),textvar=avar,borderwidth=2,relief=GROOVE)
    e6.place(x=240,y=330,height=100)
    e16=Entry(f8,width=32,font=("Calibri (Body)",15,"bold"),textvar=pid1,borderwidth=2,relief=GROOVE,state="disabled")
    e16.place(x=240,y=45)

    tree.bind("<ButtonRelease-1>",selectItem)

    e16.focus()

    l16=Label(mainframe,fg="black",text="Appoint Doctor",font=("Berlin Sans FB Demi",22,"bold"))
##    l17=Label(f9,fg="black",text="Symptoms",font=("Berlin Sans FB Demi",19,"bold"))
    l18=Label(f9,fg="black",text="Select to Appoint Doctor",font=("Berlin Sans FB Demi",19,"bold"))
    l21=Label(f9,fg="black",text="Select to Appoint Specialization",font=("Berlin Sans FB Demi",19,"bold"))
    l19=Label(f9,fg="black",text="Enter Date(DD/MM/YYYY)",font=("Berlin Sans FB Demi",19,"bold"))
    l20=Label(f9,fg="black",text="Enter Time(HH:MM:SS)",font=("Berlin Sans FB Demi",19,"bold"))

    l16.place(x=730,y=10)
##    l17.place(x=12,y=50)
    l18.place(x=12,y=62)
    l19.place(x=12,y=193)
    l20.place(x=12,y=270)
    l21.place(x=12,y=120)

##    e7=Entry(f9,width=25,font=(22),textvar=smpvar,borderwidth=2,relief=GROOVE)
##    e7.place(x=170,y=55,height=100)
    e8=Combobox(f9,width=20,font=(22),textvar=drvar)
    e8.bind("<<ComboboxSelected>>",showdetails)
    e8.place(x=320,y=67)
    e10=Entry(f9,width=23,font=(22),textvar=dtvar2,borderwidth=2,relief=GROOVE,state="disabled")
    e10.place(x=340,y=200)
    e11=Entry(f9,width=23,font=(22),textvar=tmvar,borderwidth=2,relief=GROOVE,state="disabled")
    e11.place(x=320,y=275)
    e12=Entry(f9,width=21,font=(22),textvar=specvar2,borderwidth=2,relief=GROOVE)
    e12.place(x=370,y=127)

    b1=Button(f9,bg="blue",text="Add",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=add)
    b2=Button(f9,bg="green",text="Update",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=update_clicked)
    b3=Button(f9,bg="red",text="Delete",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=delete)
    b4=Button(f9,bg="darkgray",text="Clear",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=clear_clicked)
    

    b1.place(x=20,y=361)
    b2.place(x=160,y=361)
    b3.place(x=330,y=361)
    b4.place(x=500,y=361)

    l21=Label(mainframe,fg="black",text="Patients Details",font=("Berlin Sans FB Demi",22,"bold"))
    l21.place(x=40,y=500)
    l22=Label(f11,fg="black",text="Enter Patient ID",font=("Berlin Sans FB Demi",19,"bold"))
    l22.place(x=20,y=40)

    e13=Entry(f11,width=29,font=(22),textvar=pid2,borderwidth=2,relief=GROOVE)
    e13.place(x=270,y=46)

    b6=Button(f11,bg="darkblue",fg="white",text="Search",bd=5,font=("Berlin Sans FB Demi",15,"bold"),relief=RAISED,command=search_items)
    b7=Button(f11,bg="gray",fg="white",text="Clear",bd=5,font=("Berlin Sans FB Demi",15,"bold"),relief=RAISED,command=clear2)
    b8=Button(f11,bg="orange",fg="white",text="Show All",bd=5,font=("Berlin Sans FB Demi",15,"bold"),relief=RAISED,command=show)

    b6.place(x=630,y=30)
    b7.place(x=790,y=30)
    b8.place(x=950,y=30)

    getgen()
    getdoctor()
    getpcode()
    
    

def patient():
    def clear_clicked():
        namevar2.set("")
        

    deletepages()
    f8=Frame(mainframe,bd=5,relief=RIDGE)
    f9=Frame(mainframe,bd=5,relief=RIDGE)
    f10=Frame(root,bd=5,bg="darkgray",relief=RAISED)
    f11=Frame(mainframe,bd=5,relief=RIDGE)
    
    f8.place(x=10,y=15,height=135,width=1320)
    f9.place(x=10,y=170,height=130,width=1320)
    f10.place(x=190,y=50,height=60,width=1346)
    f11.place(x=10,y=310,height=430,width=1320)
    # Create an instance of Style widget
    style = ttk.Style()
    style.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(f11, column=("c1", "c2","c3","c4","c5","C6","C7","c8","c9","c10","c11","c12","c13","c14"), show='headings', height=18)
    tree.column("# 1",width="70")
    tree.heading("# 1", text="Patient ID")

    tree.column("# 2",width="90")
    tree.heading("# 2", text="Name")
    tree.column("# 3",width="70")
    tree.heading("# 3", text="Gender")
    tree.column("# 4",width="70")
    tree.heading("# 4", text="D.O.B")
    tree.column("# 5",width="100")
    tree.heading("# 5", text="Contact No.")
    tree.column("# 6",width="100")
    tree.heading("# 6", text="Email")
    tree.column("# 7",width="100")
    tree.heading("# 7", text="Address")
    tree.column("# 8",width="100")
    tree.heading("# 8", text="Symptoms")
    tree.column("# 9",width="100")
    tree.heading("# 9", text="Doctor App.")
    tree.column("# 10",width="100")
    tree.heading("# 10", text="Specialization")
    tree.column("# 11",width="100")
    tree.heading("# 11", text="Apt. Date")
    tree.column("# 12",width="75")
    tree.heading("# 12", text="APT. Time")
    tree.column("# 13",width="75")
    tree.heading("# 13", text="Next APT.")
    tree.column("# 14",width="118")
    tree.heading("# 14", text="Medicines")


    con=sqlite3.connect("hospital.sqlite")
    c=con.cursor()
    s=c.execute("SELECT * FROM doctor1")
    table_data=c.fetchall()

    for i, data in enumerate(table_data):
        tree.insert("", "end", text=(i), values=data)

    
    

    vsb=ttk.Scrollbar(f11,orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    
    tree.place(x=10,y=10)

##    def show_today():
##        today = datetime.now()
##
##            # Connect to the database
##        con=sqlite3.connect("hospital.sqlite")
##        c=con.cursor()
##        s=c.execute("SELECT * FROM doctor1")
##        table_data=c.fetchall()
##
##
##        
##            # Fetch today's appointments from the database
##        query = "SELECT pname,conm,symp,spec,dr,date,time FROM appointments WHERE date = today"
##        c.execute(query, (today,))
##        appointments = c.fetchall()
##        for appointment in appointments:
##            tree.insert("", "end", text=appointment[0], values=(appointment[1], appointment[2], appointment[3]))





##    def getpcode():
##            con=sqlite3.connect("hospital.sqlite")
##            c=con.cursor()
##            c.execute("select pid from appointment2")
##            data=c.fetchall()
##            if len(data)==0:
##                pc=2001
##            else:
##                dc=data[-1][0]+1
##            pid.set(str(pc))
##            con.close()


    def show_all():

        tree.delete(*tree.get_children())
        con=sqlite3.connect("hospital.sqlite")
        c=con.cursor()
        s=c.execute("SELECT * FROM doctor1")
        table_data=c.fetchall()

        for i, data in enumerate(table_data):
            tree.insert("", "end", text=(i), values=data)
    def search_items():
            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
##            print(str(specvar4.get()))
            s=c.execute("SELECT * FROM doctor1 where pid=?",(str(pid.get()),))
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)
    def search_items1():
            today = date.today()
            now = datetime.now()
            date1 = now.strftime('%d/%m/%Y')

            
##            print(today)

            tree.delete(*tree.get_children())
            con=sqlite3.connect("hospital.sqlite")
            c=con.cursor()
##            print(str(specvar4.get()))
            s=c.execute("SELECT * FROM doctor1 where date=?",(date1,))
            table_data=c.fetchall()

            for i, data in enumerate(table_data):
                tree.insert("", "end", text=(i), values=data)

##    def date():
##            con=sqlite3.connect("hospital.sqlite")
##            c=con.cursor()
##            c.execute("select date from appointment2")
##            data=c.fetchall()
##            l=[]
##            for row in data:
##                l.append(row[0])
##            e1['values']=l
##            con.close()
##
##    def delete_today():
##           # Get selected item to Delete
####            selected_item = tree.selection()[0]
####            tree.delete(selected_item)
##            today = date.today()
####            
##            con=sqlite3.connect("hospital.sqlite")
##            c=con.cursor()
##            
##            ans=messagebox.askyesno("ALERT","ARE YOU SURE")
##            if ans==True:
##                c.execute("delete from appointment2 where date=?",(today,))
##                con.commit()
##                messagebox.showinfo("THANK YOU","1 RECORD DELETED...")
##                selected_item = tree.selection()[0]
##                tree.delete(selected_item)
##                con=sqlite3.connect("hospital.sqlite")
##                c=con.cursor()
##                ic=namevar2.get()
##        
##                
##                c.execute("delete from appointments where date=?",(today,))
##                con.commit()
##
##            
##
##                clear_clicked()
##                l=[0]
##                e1['values']=l
##                date()
####                namevar2.set("")

        


        


        



    
    l1=Label(f10,fg="black",bg="darkgray",text="Patients | Appointment History",font=("Berlin Sans FB Demi",25,"bold"))
    l1.pack(side="left")

    l8=Label(mainframe,fg="black",text="Search appointment",font=("Berlin Sans FB Demi",22,"bold"))
    l8.place(x=20,y=10)

    l9=Label(f8,fg="black",text="Patient ID     :",font=("Berlin Sans FB Demi",19,"bold"))
    l9.place(x=20,y=50)

    e1=Entry(f8,width=28,font=(22),textvar=pid,borderwidth=2,relief=GROOVE)
    e1.place(x=210,y=55)

    b6=Button(f8,bg="darkblue",fg="white",text="Search",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=search_items)
    b7=Button(f8,bg="gray",fg="white",text="Clear",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=clear_clicked)

    b6.place(x=600,y=40)
    b7.place(x=770,y=40)

    l12=Label(mainframe,fg="black",text="appointment Menu",font=("Berlin Sans FB Demi",22,"bold"))
    l12.place(x=20,y=155)


    b14=Button(f9,bg="darkblue",fg="white",text="Show Today's appointment",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=search_items1)
    b15=Button(f9,bg="gray",fg="white",text="Show All appointment",bd=5,font=("Berlin Sans FB Demi",18,"bold"),relief=RAISED,command=show_all)


    b14.place(x=20,y=30)
    b15.place(x=410,y=30)
    
    e1.focus()

    
mainframe=Frame(root)
f1=Frame(root,bd=5,bg="teal",relief=RAISED)
f2=Frame(root,bd=5,bg="beige",relief=RAISED)
f3=Frame(root,bd=5,bg="darkgray",relief=RAISED)
f4=Frame(root,bd=5,relief=RAISED,background="black")

l1=Label(f1,bg="teal",fg="beige",text="Hospital Management System",font=("Berlin Sans FB Demi",26,"bold"))
l2=Label(f2,bg="beige",text="Menu",font=("Berlin Sans FB Demi",25,"bold"))
l3=Label(f3,fg="black",bg="darkgray",text="Admin Dashboard",font=("Berlin Sans FB Demi",22,"bold"))

i1=PhotoImage(file="HOME.png")
i2=PhotoImage(file="DOCTOR.png")
i3=PhotoImage(file="PATIENT.png")
i4=PhotoImage(file="appointment.png")
i5=PhotoImage(file="EXIT.png")

b1=Button(f4,bg="lightgrey",bd=5,image=i1,relief=RAISED,command=home)
b2=Button(f4,bg="lightgrey",bd=5,image=i2,relief=RAISED,command=doctor)
b3=Button(f4,bg="lightgrey",bd=5,image=i3,relief=RAISED,command=patient)
b4=Button(f4,bg="lightgrey",bd=5,image=i4,relief=RAISED,command=appointment)
b5=Button(f4,bg="lightgrey",bd=5,image=i5,relief=RAISED,command=root.destroy)

mainframe.place(x=190,y=110,height=740,width=1345)
f1.pack(side="top",fill=X)
f2.place(x=0,y=50,height=60,width=190)
f3.place(x=190,y=50,height=60,width=1346)
f4.place(x=0,y=110,height=753,width=190)

l1.pack(side="left")
l2.pack()
l3.pack(side="left")

b1.place(x=0,y=0,height=150.6,width=185)
b2.place(x=0,y=150.6,height=150.6,width=185)
b3.place(x=0,y=301.2,height=150.6,width=185)
b4.place(x=0,y=451.8,height=150.6,width=185)
b5.place(x=0,y=602.4,height=150.6,width=185)

home()

root.mainloop()
