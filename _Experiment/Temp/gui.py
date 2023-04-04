from tkinter import *

def python():
    data=e1.get()
    data_1=t1.get(1.0,END)
    l6.config(text=data)

win=Tk()
win.title("School Potfolio")
win.config(bg="#FA8072")
l=Label(win,text="Wscube Tech School",font=("Rockwell Extra Bold",50, "bold"),bg="#FA8072",fg="red")
l.place(x=350,y=30,height=60)

l1=Label(win,text="Name:",font=("Calibri (Body)",20),bg="#FA8072",fg="black")
l1.place(x=10,y=130)
e1=Entry(win,font=("Time New Roman",16))
e1.place(x=97,y=137,height=28)

l2=Label(win,text="Father's name:",font=("Calibri (Body)",20),bg="#FA8072",fg="black")
l2.place(x=10,y=180)
e2=Entry(win,font=("Time New Roman",16))
e2.place(x=197,y=187,height=28)

l3=Label(win,text="Mother's name:",font=("Calibri (Body)",20),bg="#FA8072",fg="black")
l3.place(x=10,y=230)
e3=Entry(win,font=("Time New Roman",16))
e3.place(x=200,y=235,height=28)

l4=Label(win,text="Phone No.:",font=("Calibri (Body)",20),bg="#FA8072",fg="black")
l4.place(x=10,y=280)
e4=Entry(win,font=("Time New Roman",16))
e4.place(x=150,y=285,height=28)

l5=Label(win,text="Address:",font=("Calibri (Body)",20),bg="#FA8072",fg="black")
l5.place(x=10,y=330)
t1=Text(win,font=("Time New Roman",16))
t1.place(x=123,y=334,height=250,width=500)


b=Button(win,text="Submit",font=("Calibri (Body)",20),bg="#FA8072",fg="black",command=python)
b.place(x=600,y=600)
win.mainloop()