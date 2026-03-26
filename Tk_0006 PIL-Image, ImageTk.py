# Tkinter >>> PIL >>> Image, ImageTk
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Royalty Flower Pot")
root.geometry("500x400")

f_image = Image.open("900_image__PNG_logo-removebg-preview.png")
f_photo = ImageTk.PhotoImage(f_image.resize((700, 700)))

label = tk.Label (root, image=f_photo)
label.place(x=200, y=10)                       # image to photo convert >>> call_ root.mainloop()


A_image = Image.open("900_image_A_logo-removebg-preview.png")               # extra added
A_photo = ImageTk.PhotoImage(A_image.resize((100, 100)))

label_1 = tk.Label (root, image=A_photo)
label_1.place(x=750, y=130)

from tkinter import messagebox
def submit():
    data = f"""
    name = {name.get()}
    dob = {dob.get()}
    mobile = {mobile.get()}
    degree = {degree.get()}
    {loc.get()}
    """
    print(data)
    messagebox.showinfo("Submited", "Registration Succussful!")
name = tk.StringVar()
dob = tk.StringVar()
mobile = tk.StringVar()
loc = tk.StringVar()

from tkinter import ttk
Degree = ["B.A(Tamil)", "B.A(English)","B.A(History)", "B.Sc(Maths)", "B.Sc.(Computer Science)", "B.Sc(IT)", "BBA", "BCA"]
degree = ttk.Combobox(root, values=Degree)
degree.place(x=500, y=250)
degree.set(" ")

tk.Label (root, text="Name :").place(x=367, y=160)
tk.Entry (root, textvariable= name).place(x= 500, y=160)

tk.Label (root, text= "Date of Birth :").place(x=367, y=190)
tk.Entry (root, textvariable= dob).place(x=500, y=190)

tk.Label (root, text= "Mobile :").place(x=367, y=220)
tk.Entry (root, textvariable= mobile).place(x=500, y=220)

tk.Label (root, text= "Select your Degree :").place(x=367, y=250)

tk.Label (root, text= "Location :").place(x=367, y=280)
Textbox = tk.Text (root, height=5, width=20)
Textbox.place(x=500,  y=280)

tk.Button(root, text="Submit", command=submit).place(x= 580, y= 490)

root.mainloop()