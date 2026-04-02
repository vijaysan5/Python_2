"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
def submit():
    opening = f"""
    #username : {username.get()}
    #password : {password.get()}"
"""
    print(opening)
    #messagebox.showinfo("Information Box", "Ready to Start")
root = tk.Tk()
root.title("Bank Application")
root.geometry("300x400")
username= tk.StringVar()
password = tk.StringVar()
image = Image.open("GUI Tkinter Program/900_image PNG People logo.png").resize((80,80))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.place(x=100, y=5)
tk.Label (root, text="Username").place(x=110, y=100)
tk.Entry (root, textvariable=username).place(x=80, y=120)
tk.Label (root, text="Password").place(x=110, y=150)
tk.Entry (root, textvariable=password).place(x=80, y=170)
tk.Button (root, text="Submit", command=submit).place(x=120, y=320)
root = tk.Tk()
root.title("Bank Application")
root.geometry("300x400")
name= tk.StringVar()
dob= tk.StringVar()
tk.Label (root, text= "Name").place(x=0, y=10)
tk.Entry (root, textvariable=name).place(x=80, y=10)
tk.Label (root, text= "Date of Birth").place(x=0, y=30)
tk.Entry (root, textvariable=dob).place(x=80, y=30)
tk.Button (root, text="Next", command=submit).place(x=120, y=320)
root.mainloop()
"""

import tkinter as tk
from tkinter import messagebox
UseId = "@san"
psId = "505"

accounts = {
    "as_01" : {"name" : "Dhivya", "Balance" : 5000},
    "as_02" : {"name" : "Anusri", "Balance" : 1000}
}

def login():
    user = username_id.get()
    pswd = password_id.get()
    
    if UseId == user and psId == pswd :
        messagebox.showinfo("Login Info", "Login Successfully...!")
        login_win.destroy()
        open_Ac_win()
    else:
        a = messagebox.askyesnocancel("Login Error", "login id is wrong.  create new login id?")
        if a :
            create_newlog()
def create_newlog():
    global UseId, psId
    UseId = username_id.get()
    pswd = password_id.get()
    messagebox.showinfo("Login Info", "New Login Id is created..!")

def open_Ac_win():
    global ac_entry
    ac_win =tk.Tk()
    ac_win.title("Account Window")
    ac_win.geometry("200x200")

    tk.Label (ac_win, text="Enter Your Account Number").pack()
    ac_entry = tk.Entry(ac_win)
    ac_entry.pack()
    tk.Button(ac_win, text="Next", command=check_account).pack()
    ac_win.mainloop()
def check_account():
    acc_no = ac_entry.get()
    if acc_no in accounts:
        messagebox.showinfo("Account Number Search...", "Account number is found...")
        open_bank(acc_no)
    else:
        res = messagebox.askyesnocancel("Account Number Search...", "Account number is not found. plz visit nearby branch.")
        if res:
            create_account()
def create_account():
    new_ac = tk.Tk()
    new_ac.title("Create New Account")
    new_ac.geometry("200x200")

    tk.Label(new_ac, text="Name").pack()
    name = tk.Entry(new_ac)
    name.pack()
    tk.Label(new_ac, text="Enter New Account Number").pack()
    acc_no = tk.Entry(new_ac)
    acc_no.pack()

    def save_newac():
        accounts[acc_no.get()] = {
            "name" : name.get(),
            "Balance" : 500
        }
        messagebox.showinfo("Account Created!", "Your new Bank Account is Created Successfully...")
    tk.Button (new_ac, text="Next", command=save_newac).pack()
    new_ac.mainloop()
def open_bank(acc_no):
    global amount_entry
    bank_win = tk.Tk()
    bank_win.title("Bank Checking")
    bank_win.geometry("200x200")
    tk.Label (bank_win, text="Enter Ammount").pack()
    amount_entry = tk.Entry (bank_win)
    amount_entry.pack()

    def balance_c():
        bal = accounts[acc_no]["Balance"]
        messagebox.showinfo("Account Balance",  f"Your Account Balance : {bal}")

    def Depsit():
        amt = int(amount_entry.get())
        accounts[acc_no]["Balance"] += amt
        messagebox.showinfo("Amount Deposit", f"Amount is Deposited...!")

    def withdr():
        amt = int(amount_entry.get())
        accounts[acc_no]["Balance"] -= amt
        messagebox.showinfo("Amountt Withdrawal", f"Amount is debited...!")

    tk.Button (bank_win, text="Check Balance", command=balance_c).pack()
    tk.Button (bank_win, text="Deposit", command=Depsit).pack()
    tk.Button (bank_win, text="Withdraw", command=withdr).pack()

login_win = tk.Tk()
login_win.title("Bank Application Entry")
login_win.geometry("200x200")

tk.Label(login_win, text="Username").pack()
username_id = tk.Entry(login_win)
username_id.pack()

tk.Label(login_win, text="Password").pack()
password_id = tk.Entry(login_win)
password_id.pack()

tk.Button (login_win, text="Submit", command=login).pack()
login_win.mainloop()


