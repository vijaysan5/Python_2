##___ COMBO BOX ___#
import tkinter as tk
from tkinter import ttk

#   Title()
root = tk.Tk()
root.title ("Combo Box eg.")

#   Label()
lable = tk.Label (root, text= "Choose your Distric")
lable.pack(padx=5, pady=5)

#   Entry select >>> Options
dt = ["Mayiladuthurai", "Thiruvaru", "Nagai", "Karaikal", "Thanjavur"]
combo = ttk.Combobox(root, values=dt)
combo.pack(padx=10, pady=10)

#   set main Option
combo.set(" ")

#   function :
def Show_dt():
    print("Distric :", combo.get())

button = ttk.Button (root, text="Submit", command=Show_dt)
button.pack(padx=10, pady=10)

#   Call :
root.mainloop()

