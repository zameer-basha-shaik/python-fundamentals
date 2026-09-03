# Connecting to an API
"""
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        print(content["name"])


    else:
        print("Data can't be retrieved:",response.status_code)


pokemon_name = 'pikachu'
get_pokemon_info(pokemon_name)

"""
#PyQt5 Introduction, labels, images
"""
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zameer's first GUI")
        self.setGeometry(700, 300, 1000, 1000)

        label = QLabel(self)
        # label.setFont(QFont("Arial", 40))
        label.setGeometry(10, 10, 641, 360)
        # label.setStyleSheet("color: purple;"
        #                     "background-color: white;"
        #                     "font-weight: bold;"
        #                     "text-decoration: underline;")
        image_path = Path(__file__).resolve().parent.parent / "resources" / "img.jpg"
        pixemap = QPixmap(str(image_path))
        label.setPixmap(pixemap)
        label.setScaledContents(True)
        label.setGeometry( (self.width() - label.width())//2,
                          (self.height() - label.height())//2,
                          label.width(), label.height()
        )

        #label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
"""
#PyQt5 layouts
"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zameer's first GUI")
        self.setGeometry(700, 300, 1000, 1000)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        labe1 = QLabel("#1")
        labe2 = QLabel("#2")
        labe3 = QLabel("#3")
        labe4 = QLabel("#4")
        labe5 = QLabel("#5")

        labe1.setStyleSheet("background-color: red;")
        labe2.setStyleSheet("background-color: yellow;")
        labe3.setStyleSheet("background-color: green;")
        labe4.setStyleSheet("background-color: blue;")
        labe5.setStyleSheet("background-color: purple;")

        layout = QGridLayout()

        layout.addWidget(labe1,0,0)

        layout.addWidget(labe2,0,1)

        layout.addWidget(labe3,1,0)

        layout.addWidget(labe4,1,1)

        layout.addWidget(labe5,2,0)

        central_widget.setLayout(layout)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

"""
"""
#PyQt5 Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Buttons")
        self.setGeometry(500, 300, 700, 400)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(15, 20, 100, 50)
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150, 300,200, 100)
        self.label.setStyleSheet("font-size: 50px;"
                                 "color: yellow;")

    def on_click(self):

        print("Button Clicked!")
        self.label.setText("Clicked!")
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
"""
#PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Buttons")
        self.setGeometry(500, 300, 700, 400)
        self.checkbox = QCheckBox("Do you like coding?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setGeometry(150, 150, 300, 150)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # print(state)
        if state == Qt.Checked:
            print("You like coding!")
        else:
            print("You don't like coding")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

"""
"""
#PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Buttons")
        self.setGeometry(500, 300, 700, 600)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master card", self)
        self.radio3 = QRadioButton("Credit card", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
                
        

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(10,0,150,50)
        self.radio2.setGeometry(10,100,200,50)
        self.radio3.setGeometry(10,200,250,50)
        self.radio4.setGeometry(10,300,200,50)
        self.radio5.setGeometry(10,400,250,50)

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px;"
                           "font-family: Arial"
                           "}")
        self.radio1.toggled.connect(self.raido_selected)
        self.radio2.toggled.connect(self.raido_selected)
        self.radio3.toggled.connect(self.raido_selected)
        self.radio4.toggled.connect(self.raido_selected)
        self.radio5.toggled.connect(self.raido_selected)

    def raido_selected(self):
        button_selected = self.sender()

        if button_selected.isChecked():
            print(f"You Selected: {button_selected.text()}")
                        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

"""
"""
#PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Buttons")
        self.setGeometry(500, 300, 600, 600)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
                
        

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(20, 40, 200, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.button.setGeometry(40, 80, 100, 50)
        self.setStyleSheet("font-size: 20px;")
        self.line_edit.setPlaceholderText("Enter Your Name")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}")
            

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


"""

#PyQt5 setStyleSheet

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Buttons")
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()
    
    def initUI(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 30px
            }
            QPushButton#button1:hover{
                background-color: red;
            }
            QPushButton#button2:hover{
                            background-color: blue;
                        }
            QPushButton#button3:hover{
                            background-color: yellow;
                        }
        
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

