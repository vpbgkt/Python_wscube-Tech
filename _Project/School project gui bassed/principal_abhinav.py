from tkinter import *
import sqlite3
from tkinter import messagebox
win = Tk()    #creat obj win to call the class.(win=windows)
"""
conn = sqlite3.connect("StudentDatabase.db")
cur = conn.cursor()
cur.execute("CREATE TABLE student_info(name TEXT, fname TEXT, mname TEXT, cnum INT , address TEXT, dob TEXT)")
conn.commit() #use to insert/transfer data into table
conn.close()"""

def button():
    name = e1.get()
    fname = e2.get()
    mname = e3.get()
    cnum = e4.get()
    add = t1.get(1.0,END)
    #l6.config(t1=data)
    dob = e5.get()

    conn = sqlite3.connect("StudentDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student_info VALUES('"+name+"','"+fname+"','"+mname+"','"+cnum+"','"+add+"','"+dob+"')")
    messagebox.showinfo("Information", "STUDENT DATA SAVED SUCCESSFULLY!")
    conn.commit()
    conn.close()

def fee():
    jk = Tk()
    #CREATION OF DATABASE TABLE FOR STUDENT FEES
    """conn = sqlite3.connect("Student_Fee.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE student_fee(rollnum INT, name TEXT, fee INT) ")
    conn.commit()
    conn.close()"""

    jk.geometry("1370x730")
    jk.title("SchoolDBMS")
    jk.config(bg="#AED6F1")
    l_title = Label(jk, text="VAB ACADEMY", font=("Bauhaus 93", 50, "bold"), bg="#2E86C1", fg="WHITE", bd=8,relief="groove")
    l_title.pack(side=TOP, fill=X)

    l_rollnum = Label(jk, text="Roll Number", font="time 19 bold", bg="#AED6F1", fg="black")
    l_rollnum.place(x=10, y=130)
    e11 = Entry(jk, font=("Time New Roman", 18), bg="#EBF5FB", bd=3, relief="groove")
    e11.place(x=220, y=134, height=30)

    l_name = Label(jk, text="Name", font="time 19 bold", bg="#AED6F1", fg="black")
    l_name.place(x=10, y=180)
    e12 = Entry(jk, font=("Time New Roman", 18), bg="#EBF5FB", bd=3, relief="groove")
    e12.place(x=220, y=184, height=30)

    l_fee = Label(jk, text="Fee", font="time 19 bold", bg="#AED6F1", fg="black")
    l_fee.place(x=10, y=230)
    e13 = Entry(jk, font=("Time New Roman", 18), bg="#EBF5FB", bd=3, relief="groove")
    e13.place(x=220, y=232, height=30)

    def fee2():
        rollnum = e11.get()
        name = e12.get()
        fee = e13.get()
        conn = sqlite3.connect("Student_Fee.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO student_fee VALUES('" + rollnum + "','" + name + "','" + fee + "')")
        messagebox.showinfo("Information", "STUDENT FEE DEPOSITED SUCCESSFULLY!")
        conn.commit()
        conn.close()
        #jk.mainloop()

        """conn = sqlite3.connect("Student_Fee.db")
        cur = conn.cursor()
        # t=(rollnum,name,fee)
        data = "INSERT INTO student_info VALUES('" + rollnum + "','" + name + "','" + fee + "')"
        data = ""INSERT INTO student_info VALUES(?,?,?)""
        cur.execute(data)
        messagebox.showinfo("Information", "STUDENT FEE DEPOSITED SUCCESSFULLY!")
        conn.commit()
        conn.close()
        jk.mainloop()"""
    b_submitFee = Button(jk, text="Submit", font="time 12 bold", bg="#1ABC9C", fg="white", width=20, command=fee2)
    b_submitFee.place(x=500, y=600)
    b_exit2 = Button(jk, text="Exit", font="time 12 bold", bg="#C0392B", fg="white", width=20, command=jk.quit)
    b_exit2.place(x=702, y=600)
    jk.mainloop()

def principal():
    root = Tk()
    root.geometry("1370x730")
    root.title("SchoolDBMS")
    root.config(bg="#AED6F1")
    l_title = Label(root, text="VAB ACADEMY", font=("Bauhaus 93", 50, "bold"), bg="#2E86C1", fg="WHITE", bd=8,relief="groove")
    l_title.pack(side=TOP, fill=X)

    l_passwd = Label(root, text="Password", font="time 19 bold", bg="#AED6F1", fg="black")
    l_passwd.place(x=10, y=130)
    e21 = Entry(root, font=("Time New Roman", 18), bg="#EBF5FB", bd=3, relief="groove")
    e21.place(x=220, y=134, height=30)
    def print_something():
        if e21 == "123":
            print("Welcome")
            #b_submitFee = Button(root, text="Submit", font="time 12 bold", bg="#1ABC9C", fg="white", width=20,command=print_somthing)
            #b_submitFee.place(x=500, y=600)
            #button123 = Button(root, text="Print Me", command=printSomething)
            # #button123.pack()
        else:
            print("wrong")

    b_submitFee = Button(root, text="Submit", font="time 12 bold", bg="#1ABC9C", fg="white", width=20, command= print_something)
    b_submitFee.place(x=500, y=600)
    b_exit2 = Button(root, text="Exit", font="time 12 bold", bg="#C0392B", fg="white", width=20, command=root.quit)
    b_exit2.place(x=702, y=600)


win.geometry("1370x730")
win.title("SchoolDBMS")
win.config(bg="#AED6F1")
l_title=Label(win,text="VAB ACADEMY",font=("Bauhaus 93",50,"bold"),bg="#2E86C1",fg="WHITE",bd=8,relief="groove")
#l.place(x=500,y=40,height=60,width=400)
l_title.pack(side=TOP,fill=X)

l_name=Label(win,text="Name",font="time 19 bold",bg="#AED6F1",fg="black")
l_name.place(x=10,y=130)
e1=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
e1.place(x=220,y=134,height=30)

l_fname=Label(win,text="Father's Name",font="time 19 bold",bg="#AED6F1",fg="black")
l_fname.place(x=10,y=180)
e2=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
e2.place(x=220,y=184,height=30)

l_mname=Label(win,text="Mother's Name",font="time 19 bold",bg="#AED6F1",fg="black")
l_mname.place(x=10,y=230)
e3=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
e3.place(x=220,y=232,height=30)

l_cnum=Label(win,text="Contact Number",font="time 19 bold",bg="#AED6F1",fg="black")
l_cnum.place(x=10,y=280)
e4=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
e4.place(x=220,y=281,height=30)

l_add=Label(win,text="Address",font="time 19 bold",bg="#AED6F1",fg="black")
l_add.place(x=10,y=330)
t1=Text(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
t1.place(x=220,y=331,height=140,width=500)

l_dob=Label(win,text="Date of Birth",font="time 19 bold",bg="#AED6F1",fg="black")
l_dob.place(x=10,y=490)
e5=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
e5.place(x=220,y=492,height=30)

b_submit=Button(win,text="Submit",font="time 12 bold",bg="#1ABC9C",fg="white",width=20,command=button)
b_submit.place(x=500,y=600)
b_exit=Button(win,text="Exit",font="time 12 bold",bg="#C0392B",fg="white",width=20,command=win.quit)
b_exit.place(x=702,y=600)
b_fee=Button(win,text="FEE DEPOSITE",font="time 12 bold",bg="#C0392B",fg="white",width=15,command=fee)
b_fee.place(x=1000,y=100)
b_prin=Button(win,text="PRINCIPAL ACCESS",font="time 12 bold",bg="#C0392B",fg="white",width=17,command=principal)
b_prin.place(x=1170,y=100)


win.mainloop() #use to hold GUI screen


