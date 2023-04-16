from tkinter import *

win = Tk()
win.geometry("1370x730")
win.title("CarRental")
win.config(bg="#424949")

img = PhotoImage(name="rr", file="fishes.gif")
lbl_img1=Label(win,image=img)
lbl_img1.pack()



win.mainloop()