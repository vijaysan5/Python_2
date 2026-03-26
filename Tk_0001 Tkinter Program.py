# Tkinter Widget
"""
Label - The Label widget is used to provide a single-line caption for other widgets. It can also contain images.

Button - The Button widget is used to display the buttons in your application.

Entry - The Entry widget is used to display a single-line text field for accepting values from a user.

Text - The Text widget is used to display text in multiple lines.

Radiobutton - The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.

Checkbutton - The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.

Combobox – walk you through the steps of creating a combobox widget.

Message - The Message widget is used to display multiline text fields for accepting values from a user.

Frame - The Frame widget is used as a container widget to organize other widgets.

Menu - The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.

Menubutton - The Menubutton widget is used to display menus in your application. 

Canvas - The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.
"""


from tkinter import *
select = Tk()
def submit():
    data = f"""
    name = {name.get()}
    dob = {dob.get()}
    mobile = {mobile.get()}
    """
select.title("College Application Form")
name = StringVar()
dob = StringVar()
mobile = StringVar()
a1 = Label (select, text="Name") 
a1.pack(anchor=W)
a2 = Entry (select, textvariable= name)
a2.pack(anchor=W)
b1 = Label (select, text= "Date of Birth")
b1.pack(anchor=W)
b2 = Entry (select, textvariable= dob)
b2.pack(anchor=W)
c1 = Label (select, text= "Mobile")
c1.pack(anchor=W)
c2 = Entry (select, textvariable= mobile)
c2.pack(anchor=W)
a = IntVar()
b = Radiobutton(select, text="Male", variable=a, value=1)
b.pack(anchor=W)
c = Radiobutton(select, text="Female", variable=a, value=2)
c.pack(anchor=W) 
lable = Label (select, text= "Choose your Degree")
lable.pack(padx=5, pady=5)
from tkinter import ttk
Degree = ["B.A(Tamil)", "B.A(English)","B.A(History)", "B.Sc(Maths)", "B.Sc.(Computer Science)", "B.Sc(IT)", "BBA", "BCA"]
combo = ttk.Combobox(select, values=Degree)
combo.pack(padx=10, pady=10)
combo.set(" ")
def Show_degree():
    print("Name   :", name.get())
    print("DOB    :", dob.get())
    print("Mobile :", mobile.get())
    print("Degree :", combo.get())
button = Button (select, text="Submit", command=Show_degree)
button.pack(padx=10, pady=10)

select.mainloop()


