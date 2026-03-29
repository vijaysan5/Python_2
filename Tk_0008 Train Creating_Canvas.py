"""import tkinter as tk
root = tk.Tk()
san_v = tk.Canvas(width=900, height=500, bg="lightpink", bd=3)
san_v.pack()
san_v.create_rectangle(500, 200, 250, 50, outline="black", fill="darkgreen")
san_v.create_arc(900, 100, 300, 300)
san_v.create_oval(10, 50, 200, 300, outline="black", fill= "darkblue")
san_v.create_text(380, 230, text="Yazhrose", font=("Forte", 25), fill="red")

root.mainloop()"""

# Train :

import tkinter as tk
root =  tk.Tk()
san = tk.Canvas(width=1100, height=900, bg="lightblue", bd=2)
san.pack()
# create bigg box with window
san.create_rectangle(200, 300, 390, 510, outline="black")
san.create_rectangle(195, 295, 395, 298, outline="black", fill="darkgreen")
san.create_rectangle(230, 320, 280, 380, outline="black")
san.create_rectangle(310, 320, 360, 380)
# create eng. box and eng. front
san.create_rectangle(390, 350, 650, 450)
san.create_rectangle(650, 355, 655, 445)
san.create_rectangle(655, 368, 660, 435)
 # create eng. box >>> on (2)
san.create_rectangle(450, 330, 490, 350)
san.create_rectangle(455, 315, 485, 330)
san.create_rectangle(600, 290, 620, 350)
# create wheel outline
san.create_oval(240, 460, 340, 560) # big box wheel
san.create_oval(405, 460, 505, 560)
san.create_oval(530, 460, 630, 560)
# Wheel outline >>> bluring
san.create_rectangle(241, 510, 341, 510, outline="lightblue")
san.create_rectangle(239, 511, 632, 562, outline="lightblue", fill= "lightblue")

san.create_line(390, 510, 405, 510)  # bot line >>> join wheel
san.create_line(505, 510, 530, 510)
san.create_line(630, 510, 650, 510)
san.create_line(650, 450, 650, 510)  # eng box line

# create Wheel 
san.create_oval(245, 465, 335, 560)
san.create_oval(410, 465, 500, 560)
san.create_oval(535, 465, 625, 560)

root.mainloop()
