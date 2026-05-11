import tkinter as tk
from tkinter import messagebox
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

root = tk.Tk()
root.title(" 'O' or 'X' ===> Game")
root.geometry("340x380")
Player = "X"
Board_Box = [""] * 9

def Win_Game():
    win_box = [(0,1,2), (3,4,5), (6,7,8),
               (0,3,6), (1,4,7), (2,5,8),
               (0,4,8), (2,4,6)]
    
    for a,b,c in win_box():
        if Board_Box[a] == Board_Box[b] == Board_Box[c] != "":
            return Board_Box[a]

    if "" not in Board_Box:
        return "Tie"
    
def click(i):
    global Player
    if Board_Box[i] == "":
        Board_Box[i] = Player
        buttons[i]["text"] = Player

        win = Win_Game()

        if win:
            messagebox.showinfo("Result..", "Match Draw!" if win == "Tie" else f'{win} is Win the Game')
            Reset_game()
            return
        
        Player = "O" if Player == "X" else "X"
        Play_Turn["text"] = f"{Player} ===> Turn"

def Reset_game():
    global Player, Board_Box
    Player = "X"
    Board_Box = [""] * 9

    for b in buttons:
        b["text"] = ""
    Play_Turn["text"] = "X ===> Turn"

buttons = []

for i in range(9):
    b = tk.Button(root, font=("Forte", 28), width=5, height=2, command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

Play_Turn = tk.Label(root, text="X ===> Turn", font=("Elephant", 12))
Play_Turn.grid(row=3, column=0, columnspan=3)

tk.Button(root, text="Restart", command=Reset_game)\
    .grid(row=4, column=0, columnspan=3)

class game_login(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Player Entry...")
        self.setGeometry(500, 200, 300, 200)

        QLabel("Enter your Name : ", self).move(10, 40)
        self.Name = QLineEdit(self)
        self.Name.move(120, 40)

        QLabel("Enter Your Age  :", self).move(10,70)
        self.Age = QLineEdit(self)
        self.Age.move(120, 70)
        
        buttons = QPushButton("Enter", self)
        buttons.move(100, 130)
        buttons.clicked.connect(self.check_age)

    def check_age(self):
        Name = self.Name.text()
        Age = self.Age.text()

        if not Age.isdigit() :
            QMessageBox.warning(self, "Warning Info", "Please Enter Your Age.")
            return
        
        if int(Age) >= 15 :
            QMessageBox.information(self, "Welcome Info", f'Hey {Name}! Welcome to the Game...')
            self.close()
            root.mainloop()

        else:
            QMessageBox.warning(self, "Warning Info", f'{Name}... Please Enter the Valid Age. (above 15)')

Application = QApplication(sys.argv)

Window = game_login()

Window.show()

sys.exit(Application.exec_())



