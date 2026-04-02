
import tkinter as tk
from tkinter import messagebox
import qrcode as qrc
from PIL import Image, ImageTk

def Create_qr():
    code = code_entry.get()
    if not code:
        messagebox.showerror("Error, Please try again later...")
    
    Qr_c = qrc.QRCode(version=1, box_size=20, border=2)
    Qr_c.add_data(code)
    Qr_c.make(fit=True)

    San_img = Qr_c.make_image(fill_colour="black", background_colour="white")
    San_img = San_img.resize((200,200))

    image_s = ImageTk.PhotoImage(San_img)
    qr_label.config(image=image_s)
    qr_label.image = image_s

root = tk.Tk()
root.title("Create QR Code")
root.geometry("400x400")

tk.Label(root, text="Enter >>> TEXT (or) URL").place(x=3, y=3)
code_entry = tk.Entry(root)
code_entry.place(x=150, y=5)

qr_label = tk.Label(root)
qr_label.place(x=100, y=60)
tk.Button (root, text="Create QR Code", command=Create_qr).place(x=150, y=300)
root.mainloop()