from tkinter import *
pri_win=Tk()
def submission():
    print("submitted")
    namemessage = Message(pri_win, textvariable=name).grid(row=26, column=1)

pri_win.geometry("500x600")
pri_win.config(bg='orange')
# f1=Frame(pri_win,bg="green",borderwidth=7,)
# f1.pack()
pri_win.title("Principal Access")
sch_name=Label(pri_win,text="Principal access",font=("Overpass",20,"bold")).grid(,row=5,column=30,pady=20)

namelable=Label(pri_win,text="Student name").grid(row=6,column=0,pady=5,padx=5)
roll_no_lable=Label(pri_win,text='Enter RollNO').grid(row=7,column=0,pady=5,padx=5)

name=StringVar()
roll_no=StringVar()

name_entry = Entry(pri_win,textvariable=name).grid(row=6,column=1)
roll_no_entry=Entry(pri_win,textvariable=roll_no).grid(row=7,column=1)



b1=Button(text="Get data",command=submission).grid(row=25,column=5)


pri_win.mainloop()