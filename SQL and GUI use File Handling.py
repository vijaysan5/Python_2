from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql as sqls

root = tk.Tk()
root.title("Application form")
root.geometry("400x400")

App = sqls.connect(
    host="localhost",
    user="root",
    passwd="password",
)
"""conn = App.cursor()
conn.execute("CREATE DATABASE Data_Application")"""

db = sqls.connect(host="localhost", user="root", passwd="password", database="Data_Application")
code = db.cursor()

def San_Det():
    #code.execute("create table application(Sname varchar(30),Birth varchar(25),Qualif varchar(15),Mobile varchar(15))")
    code.execute(f"insert into application(Sname,Birth,Qualif,Mobile) values ('{name_entry.get()}','{birth_entry.get()}','{qualif_entry.get()}','{mobile_entry.get()}')")
    code.execute("select * from application")
    out = code.fetchall()
    for ab in out:
        print(ab)
        db.commit()
        messagebox.showinfo("Data Info", "Person data is updated...")
tk.Label(root, text="SName").place(x=0, y=0)
name_entry = tk.Entry(root)
name_entry.place(x=100, y=0, width=200)

tk.Label(root, text="Birth").place(x=0, y=30)
birth_entry = tk.Entry (root)
birth_entry.place(x=100, y=30)

tk.Label (root, text="Qualif").place(x=0, y=60)
qualif_entry = tk.Entry (root)
qualif_entry.place(x=100, y=60)

tk.Label (root, text="Mobile").place(x=0, y=90)
mobile_entry = tk.Entry(root)
mobile_entry.place(x=100, y=90)

tk.Button(root,  text="Submit", command=San_Det).place(x=260, y=360)
root.mainloop()