# import tkinter >>> Label and Entry and Button
import tkinter as tk
from tkinter import messagebox
def submit():
    information = f"""
    Name = {name_.get()}
    User Name = {user.get()}
    Mobile = {mobile.get()}
    """
    print(information)
    messagebox.showinfo("Update Mobile Number", "Mobile Number Update succussfully!")
root = tk.Tk()
root.title("Mobile Number Update")
root.geometry("200x200")
name_ = tk.StringVar()
user = tk.StringVar()
mobile = tk.StringVar()
tk.Label (root, text="Name").pack()
tk.Entry (root, textvariable= name_).pack()
tk.Label (root, text="User Name").pack()
tk.Entry (root, textvariable= user).pack()
tk.Label (root, text="Mobile Number").pack()
tk.Entry (root, textvariable= mobile).pack()
tk.Button(root, text= "Submit", command=submit).pack(pady=10)

root.mainloop()
