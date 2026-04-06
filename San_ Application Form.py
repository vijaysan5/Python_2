
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Person Data Form")
root.geometry("600x600")

def San_Detailz():
    with open("San_create_Bio",'a') as bio:
        bio.write("\nName          :"+ name_entry.get())
        bio.write("\nDate of Birth :"+ dob_entry.get())
        bio.write("\nQualification :"+ Qualif_entry.get())
        bio.write("\nMobile        :"+ mobile_entry.get())
        bio.write("\nAadhar Number :"+ aadhar_entry.get())
        bio.write("\nMail-ID       :"+ mail_entry.get())
        bio.write("\n  ")
        print(bio)
        messagebox.showinfo("Person Data", "Your Detailz is Updated in your form")
    
tk.Label (root, text="Name").place(x=0, y=0)
name_entry = tk.Entry (root)
name_entry.place(x=100, y=0, width=200)

tk.Label (root, text="Date of Birth").place(x=0, y=30)
dob_entry = tk.Entry (root)
dob_entry.place(x=100, y=30)

tk.Label (root, text="Qualification").place(x=0, y=60)
Qualif_entry = tk.Entry (root)
Qualif_entry.place(x=100, y=60)

tk.Label (root, text="Mobile").place(x=0, y=90)
mobile_entry = tk.Entry(root)
mobile_entry.place(x=100, y=90)

tk.Label (root, text="Aadhar Number").place(x=0, y=120)
aadhar_entry = tk.Entry (root)
aadhar_entry.place(x=100, y=120)

tk.Label (root, text="Mail ID").place(x=0, y=150)
mail_entry = tk.Entry (root)
mail_entry.place(x=100, y=150, width=150)

tk.Label (root, text="Select Gender").place(x=0, y=180)
a = IntVar()
b = Radiobutton(root, text="Male", variable=a, value=1)
b.place(x=100, y=180)
c = Radiobutton(root, text="Female", variable=a, value=2)
c.place(x=170, y=180)

Label (root, text="Select Language").place(x=0, y=210)
x = IntVar()
y = IntVar()
z = IntVar()
a = Checkbutton(root, text="Tamil", variable=x)
a.place(x=100, y=210)
b = Checkbutton(root, text="English", variable=y)
b.place(x=170, y=210)
c = Checkbutton(root, text="Hindi", variable=z)
c.place(x=240, y=210)

tk.Button (root, text="Submit", command=San_Detailz).place(x=260, y=500)

root.mainloop()

"""san = open("San_create_Bio",'x')
print("File is Created")"""