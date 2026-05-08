# pyQT install >>> Pip install PyQt5 (or) python -m pip install PyQt5

import sys
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QApplication,
)

class Sanwind(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyQT Program . . .  *_*")
        self.setGeometry(200, 200, 400, 200)

        self.label = QLabel("Enter Your Name :")
        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Enter here...")

        self.label_1 = QLabel("Enter Your DOB :")
        self.textbox_1 = QLineEdit()
        self.textbox_1.setPlaceholderText("DD/MM/YYYY")

        self.label_2 = QLabel("Enter Your Qualification :")
        self.textbox_2 = QLineEdit()
        self.textbox_2.setPlaceholderText("(_Optional_)")

        self.button = QPushButton("Submit   *_*")
        
        self.button.clicked.connect(self.show_mbox)

        Layout = QVBoxLayout()

        Layout.addWidget(self.label)
        Layout.addWidget(self.textbox)
        Layout.addWidget(self.label_1)
        Layout.addWidget(self.textbox_1)
        Layout.addWidget(self.label_2)
        Layout.addWidget(self.textbox_2)
        Layout.addWidget(self.button)

        self.setLayout(Layout)


    def show_mbox(self):
        Name = self.textbox.text()
        Dob = self.textbox_1.text()
        Qualification = self.textbox_2.text()

        if Name == "":
            QMessageBox.warning(self, "Warning Message!", "Please Enter Your Name...")
        elif Dob == "":
            QMessageBox.warning(self, "Warning Message!", "Enter Your Date of Birth...")
        else:
            QMessageBox.information(self, "PyQT > Welcome", f"Hello! {Name, Qualification} => Welcome to pyQT...")


Application = QApplication(sys.argv)

show = Sanwind()

show.show()

sys.exit(Application.exec_())
