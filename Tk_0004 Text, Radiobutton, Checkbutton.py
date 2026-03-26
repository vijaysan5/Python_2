#   tkinter _ Text :
from tkinter import *
root = Tk()
a = Text(root, height=5, width=30)
a.pack()
a.insert(END, "Hey!\nCome yah!\nGood Morning...\nHave a Great Day...")
mainloop()

#   tkinter _ Radiobutton :
from tkinter import *
root = Tk()
a = IntVar()
b = Radiobutton(root, text="Male", variable=a, value=1)
b.pack(anchor=W)
c = Radiobutton(root, text="Female", variable=a, value=2)
c.pack(anchor=W)
mainloop()

#   tkinter _ Checkbutton :
from tkinter import *
root = Tk()
root.title ("Choose Qualifications")
x = IntVar()
y = IntVar()
z = IntVar()
a = Checkbutton(root, text="SSLC or HSC", variable=x)
a.grid(row=1, sticky=W)
b = Checkbutton(root, text="Diploma", variable=y)
b.grid(row=2, sticky=W)
c = Checkbutton(root, text="Degree", variable=z)
c.grid(row=3, sticky=W)

mainloop()