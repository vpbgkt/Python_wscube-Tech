from cProfile import label
from tkinter import *
from turtle import bgcolor, color
form_win = Tk()
form_win.geometry("500x600")
form_win.config(bg="#FF5773")
form_win.title("Student form")
sch_name=Label(text="Vishal ki School",font=("Overpass",20,"bold"))

frame=Frame(form_win,borderwidth=6,relief=SUNKEN)
frame.pack(side='left')

name=Label(form_win,text='student name')
# name.pack()

b1=Button(frame,text=("Submit"),fg="blue")
b1.pack(anchor='sw')

sch_name.pack()
form_win.minsize(400,500)


form_win.mainloop()