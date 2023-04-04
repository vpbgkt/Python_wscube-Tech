from tkinter import *
def click():
    window.geometry(f'{length.get()}x{breadth.get()}')

window=Tk()
window.geometry('400x400')
lengthLabel=Label(text='Length').grid(row=1,column=1)
breadthLabel=Label(text='Length').grid(row=2,column=1)

length=Entry()
breadth=Entry()
length.grid(row=1,column=2)
breadth.grid(row=2,column=2)

clicked=Button(text='Change window size',command=click) 
clicked.grid(row=3,column=2)
window.mainloop()