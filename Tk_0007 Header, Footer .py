#___HEADER and FOOTER

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Header and Footer")
root.geometry("900x700")
root.configure(bg="#000000")

frame = tk.Frame(root, bg="#C9DEE7", bd=3,  relief="ridge")
frame.place(x=380, y=10, width=500, height=670)

tk.Label (frame, text= "<<< Leave me ALONE >>>", font=("Algerian", 20), bg="#C9DEE7", fg="#000000").place(x=90, y=20)
tk.Label (frame, text= """SANJAY
          Creation'z""", font=("Forte", 20), bg="#C9DEE7", fg="#04128d").place(x=300, y=600)

frame.mainloop()