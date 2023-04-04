from tkinter import *
import sqlite3
from tkinter import messagebox
win = Tk()    #creat obj win to call the class.(win=windows)

"""conn = sqlite3.connect("StudentDatabase.db")
cur = conn.cursor()
xconn.commit() #use to insert/transfer data into table
conn.close()"""

def button():
    name = e1.get()
    fname = e2.get()
    mname = e3.get()
    cnum = e4.get()
    address = t1.get()
    dob = e5.get()
    conn = sqlite3.connect("StudentDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student_info VALUES(NULL,'"+name+"','"+fname+"','"+mname+"','"+cnum+"','"+address+"','"+dob+"')")
    #cur.execute("""INSERT INTO student_info VALUES('+ name +','" + fname + "','" + mname + "','" + cnum + "','" + dob + "')")
    # cur.execute("""INSERT INTO  student_info VALUES(NULL,'nameisv','fnameisu','mnameisof','4564','address','dob')""")



    messagebox.showinfo("Information", "STUDENT DATA SAVED SUCCESSFULLY!")
    conn.commit()
    conn.close()

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
# This is line for address...........................
l_add=Label(win,text="Address",font="time 19 bold",bg="#AED6F1",fg="black")
l_add.place(x=10,y=330)
t1=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
t1.place(x=220,y=331,height=140,width=500)

l_dob=Label(win,text="Date of Birth",font="time 19 bold",bg="#AED6F1",fg="black")
l_dob.place(x=10,y=490)
e5=Entry(win,font=("Time New Roman",18),bg="#EBF5FB",bd=3,relief="groove")
e5.place(x=220,y=492,height=30)

b_submit=Button(win,text="Submit",font="time 12 bold",bg="#1ABC9C",fg="white",width=20,command=button)
b_submit.place(x=500,y=600)
b_exit=Button(win,text="Exit",font="time 12 bold",bg="#C0392B",fg="white",width=20,command=win.quit)
b_exit.place(x=702,y=600)
win.mainloop()
