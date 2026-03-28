import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Royalty Flower Pot")
root.geometry("1000x700")
root.configure(bg="#f0f8ff")  # light blue background


b_image = Image.open("900 image_Royalty_Flowers.jpg").resize((1000, 700))
b_photo = ImageTk.PhotoImage(b_image)

bg_label = tk.Label(root, image=b_photo)
bg_label.image = b_photo
bg_label.place(x=0, y=0)


logo = Image.open("900_image__PNG_logo-removebg-preview.png").convert("RGBA")

logo = logo.resize((120, 120))  # decreased size

# Blend logo with background color (important)
bg_color = (240, 248, 255, 255)  # same as window color (#f0f8ff)
bg_logo = Image.new("RGBA", logo.size, bg_color)
bg_logo.paste(logo, (0, 0), logo)

logo_photo = ImageTk.PhotoImage(bg_logo)

logo_label = tk.Label(root, image=logo_photo, bg="#f0f8ff")
logo_label.image = logo_photo
logo_label.place(x=30, y=20)


frame = tk.Frame(root, bg="#ffffff", bd=3, relief="ridge")
frame.place(x=400, y=80, width=420, height=400)


name = tk.StringVar()
dob = tk.StringVar()
mobile = tk.StringVar()


def submit():
    data = f"""
Name: {name.get()}
DOB: {dob.get()}
Mobile: {mobile.get()}
Degree: {degree.get()}
Location: {location_box.get('1.0', tk.END).strip()}
"""
    print(data)
    messagebox.showinfo("Submitted", "Registration Successful!")


tk.Label(frame, text="Registration Form", font=("Arial", 16, "bold"),
         bg="#ffffff", fg="#7c05eb").place(x=100, y=10)


tk.Label(frame, text="Name", bg="#ffffff").place(x=30, y=60)
tk.Entry(frame, textvariable=name, width=30).place(x=150, y=60)

tk.Label(frame, text="Date of Birth", bg="#ffffff").place(x=30, y=100)
tk.Entry(frame, textvariable=dob, width=30).place(x=150, y=100)

tk.Label(frame, text="Mobile", bg="#ffffff").place(x=30, y=140)
tk.Entry(frame, textvariable=mobile, width=30).place(x=150, y=140)

tk.Label(frame, text="Degree", bg="#ffffff").place(x=30, y=180)

Degree = [
    "B.A(Tamil)", "B.A(English)", "B.A(History)",
    "B.Sc(Maths)", "B.Sc(Computer Science)",
    "B.Sc(IT)", "BBA", "BCA"
]

degree = ttk.Combobox(frame, values=Degree, width=27)
degree.place(x=150, y=180)
degree.set("Select Degree")

tk.Label(frame, text="Location", bg="#ffffff").place(x=30, y=220)

location_box = tk.Text(frame, width=23, height=4)
location_box.place(x=150, y=220)


tk.Button(frame, text="Submit", command=submit,
          bg="#0577c4", fg="white", width=15).place(x=130, y=310)


root.mainloop()