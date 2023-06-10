from tkinter import *
root = Tk()
def access():
    if e21.get()== '123':
        print(l_passwd)
        print("Access Given")
    else:
        print(e21)
        print('denied')
root.geometry("1370x730")
root.title("SchoolDBMS")
root.config(bg="#AED6F1")
l_title = Label(root, text="VAB ACADEMY", font=("Bauhaus 93", 50, "bold"), bg="#2E86C1", fg="WHITE", bd=8,
                relief="groove")
l_title.pack(side=TOP, fill=X)

l_passwd = Label(root, text="Password", font="time 19 bold", bg="#AED6F1", fg="black")
l_passwd.place(x=10, y=130)

e21 = Entry(root, font=("Time New Roman", 18), bg="#EBF5FB", bd=3, relief="groove")
e21.place(x=220, y=134, height=30)

b_getaccess = Button(root, text="Get access", font="time 12 bold", bg="#1ABC9C", fg="white", width=20,
                     command=access)

b_getaccess.place(x=500, y=600)
root.mainloop()
