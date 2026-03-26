#  ___MESSAGE BOX___
#1. Open >>> Application text box : 
import tkinter as tk
from tkinter import messagebox

def submit():
    info = f"""
    Name: {name_var.get()}
    Fother_Name: {fname_var.get()}
    Mother_Name: {mname_var.get()}
    DOB: {birth_var.get()}
    SSLC_Mark:{SSLC_var.get()}
    HSC_Mark: {HSC_var.get()}
    Degree_Name: {degree_var.get()}
    Mobile: {mobile_var.get()}
    """
    print(info)
    messagebox.showinfo("Submited", "Registration Succussful!")

root = tk.Tk()
root.title("Student Registration")
root.geometry("600x600")

name_var = tk.StringVar()
fname_var = tk.StringVar()
mname_var = tk.StringVar()
birth_var = tk.StringVar()
SSLC_var = tk.StringVar()
HSC_var = tk.StringVar()
degree_var = tk.StringVar()
mobile_var = tk.StringVar()

tk.Label (root, text= "Name").pack()
tk.Entry (root, textvariable= name_var).pack()

tk.Label (root, text= "Fother Name").pack()
tk.Entry (root, textvariable= fname_var).pack()

tk.Label (root, text= "Mother Name").pack()
tk.Entry (root, textvariable= mname_var).pack()

tk.Label (root, text= "Date of Birth").pack()
tk.Entry (root, textvariable= birth_var).pack()

tk.Label (root, text= "SSLC Percentage").pack()
tk.Entry (root, textvariable=SSLC_var).pack()

tk.Label (root, text= "HSC Percentage").pack()
tk.Entry (root, textvariable= HSC_var).pack()

tk.Label (root, text= "Degree Name").pack()
tk.Entry (root, textvariable= degree_var).pack()

tk.Label (root, text= "Mobile Number").pack()
tk.Entry (root, textvariable= mobile_var).pack()

tk.Label (root, text= "Message Box").pack()
Text_Box = tk.Text (root, height=4, width=30)
Text_Box.pack()

tk.Button(root, text= "Submit", command=submit).pack(pady=10)

root.mainloop()


#2. Open >>> messagebox >>> Calculating Mark :
import tkinter as tk
from tkinter import messagebox
def Submit():
    cc = f"""
    Name: {name_var.get()}
    sub_1: {tamil.get()}
    sub_2: {english.get()}
    sub_3: {maths.get()}
    sub_4: {evs_c.get()}
    sub_5: {hindi_c.get()}
    """
    print(cc)
    Total = tamil.get() + english.get() + maths.get() + evs_c.get() + hindi_c.get()
    print(Total)
    a = 5
    b = Total / a
    print(b)
    messagebox.showinfo("Submited", "Ready to Show your Result!")  

root = tk.Tk()
root.title("Student's Result...>>>")
root.geometry("600x600")

name_var = tk.StringVar()
tamil = tk.IntVar()
english = tk.IntVar()
maths = tk.IntVar()
evs_c = tk.IntVar()
hindi_c = tk.IntVar()

tk.Label (root, text= "Name").pack()
tk.Entry (root, textvariable= name_var).pack()

tk.Label (root, text= "Tamil").pack()
tk.Entry (root, textvariable= tamil).pack()

tk.Label (root, text= "English").pack()
tk.Entry (root, textvariable= english).pack()

tk.Label (root, text= "Maths").pack()
tk.Entry (root, textvariable= maths).pack()

tk.Label (root, text= "EVS").pack()
tk.Entry (root, textvariable= evs_c).pack()

tk.Label (root, text= "Hindi").pack()
tk.Entry (root, textvariable= hindi_c).pack()

tk.Button(root, text= "Submit", command= Submit).pack(pady=10)

root.mainloop()


##___ LIST BOX ___#
from tkinter import *
select = Tk()
select.title("Choose your Degree")
xy = Listbox(select)
xy.insert(1, "B.A.,")
xy.insert(2, "B.Sc.,")
xy.insert(3, "B.Com.,")
xy.insert(4, "BBA")
xy.insert(5, "BCA")
xy.pack()
mainloop()