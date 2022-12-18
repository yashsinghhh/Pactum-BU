from tkinter import *

window = Tk()

window.geometry("400x250")

uname = Label(window, text="Name").place(x=30, y=50)
password = Label(window, text="Price").place(x=30, y=90)
desc = Label(window, text='Description').place(x=30, y=140)
sbmitbtn = Button(window, text="Submit").place(x=30, y=220)
e1 = Entry(window, width=20).place(x=250, y=50)
e2 = Entry(window, width=20).place(x=250, y=90)
e3 = Entry(window, width=20).place(x=250, y=150)

window.mainloop()
