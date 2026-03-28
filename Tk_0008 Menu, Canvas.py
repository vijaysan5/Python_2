#   Creating Menu :
from tkinter import *
root = Tk()
san_menu = Menu(root)
root.config(menu=san_menu)

San_file = Menu(san_menu)
san_menu.add_cascade(label =  "File", menu = San_file)
San_file.add_command(label = "New Folder")
San_file.add_command(label = "New Window")
San_file.add_command(label = "Open File")
San_file.add_command(label = "Open Window")
San_file.add_separator()
San_file.add_command(label = "Exit", command = root.quit)

San_Edit = Menu(san_menu)
san_menu.add_cascade(label= "Edit", menu= San_Edit)
San_Edit.add_command(label = "Copy")
San_Edit.add_command(label = "Cut")
San_Edit.add_command(label = "Rename")

San_Help = Menu(san_menu)
san_menu.add_cascade(label= "Help", menu= San_Help)
San_Help.add_command(label= "Helpline")
San_Help.add_command(label= "Security")
San_Help.add_command(label= "About")
mainloop()



#   Creating Canvas :
"Create a Single line use canvas"
from tkinter import Tk
root= Tk()
san = Canvas(width=500, height=400, bg="skyblue")
san.pack()
san.create_line(100, 200, 400, 200)
root.mainloop()

"Create shape use canvas"
import tkinter as tk
root = tk.Tk()
san_v = Canvas(width=900, height=500, bg="lightpink", bd=3)
san_v.pack()
san_v.create_rectangle(500, 200, 250, 50, outline="black", fill="darkgreen")
san_v.create_arc(900, 100, 300, 300)
san_v.create_oval(10, 50, 200, 300, outline="black", fill= "darkblue")
san_v.create_text(380, 230, text="Yazhrose", font=("Forte", 25), fill="red")

root.mainloop()