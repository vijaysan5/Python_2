# Train runing:

import tkinter as tk
root =  tk.Tk()
san = tk.Canvas(width=1100, height=900, bg="lightblue", bd=2)
san.pack()
# create bigg box with window
train=[
san.create_rectangle(200, 300, 390, 510, outline="black", fill= "#07ceb3"),
san.create_rectangle(195, 295, 395, 298, outline="black", fill="darkgreen"),
san.create_rectangle(230, 320, 280, 380, fill="#6fc0f0"),
san.create_rectangle(310, 320, 360, 380, fill="#6fc0f0"),
san.create_rectangle(230, 400, 360, 450, outline="white", fill="#84cfd4"),
san.create_text(295, 410, text="Chennai <==> Karaikal", font=("Times New Roman", 10), fill="black"),
san.create_text(295, 430, text= "10458", font=("Times New Roman", 16), fill="black"),
san.create_rectangle(190, 305, 199, 505, fill="#555151"),
san.create_rectangle(180, 305, 189, 505, fill="#555151"),
san.create_rectangle(5, 300, 189, 510, fill="#F3CDA1"),
san.create_rectangle(30, 305, 160, 325),
san.create_text(93, 315, text="Chennai <==> Karaikal", font=("Times New Roman", 10), fill="black"),
san.create_rectangle(5, 340, 50, 400, fill="#6fc0f0"),
san.create_rectangle(60, 350, 150, 512, fill= "#141212"),
san.create_rectangle(65, 520, 145, 530, fill="black"),
san.create_rectangle(70, 535, 140, 545, fill="black"),
san.create_rectangle(65, 510, 145, 520),
san.create_rectangle(70, 520, 140, 545),

san.create_rectangle(390, 350, 650, 450, fill= "#07ceb3"),
san.create_rectangle(650, 355, 655, 445),
san.create_rectangle(655, 368, 660, 435),

san.create_rectangle(400, 350, 475, 400, fill="#f8bb76"),
san.create_rectangle(485, 350, 560, 400, fill="#f8bb76"),
san.create_rectangle(570, 350, 643, 400, fill="#f8bb76"),

san.create_rectangle(450, 330, 490, 350),
san.create_rectangle(455, 315, 485, 330),
san.create_rectangle(600, 290, 620, 350),

san.create_oval(240, 460, 340, 560), 
san.create_oval(405, 460, 505, 560),
san.create_oval(530, 460, 630, 560),

san.create_rectangle(241, 510, 341, 510, outline="lightblue"),
san.create_rectangle(239, 511, 632, 562, outline="lightblue", fill= "lightblue"),

san.create_line(390, 510, 405, 510),  
san.create_line(505, 510, 530, 510),
san.create_line(630, 510, 650, 510),
san.create_line(650, 450, 650, 510), 


san.create_oval(245, 465, 335, 560, fill="#484B48"),
san.create_oval(410, 465, 500, 560, fill="#484B48"),
san.create_oval(535, 465, 625, 560, fill="#484B48")
]

def move1():
    for i in train:
        san.move(i,5,0)
    san.after(10,move1)
#move1()
root.mainloop()
