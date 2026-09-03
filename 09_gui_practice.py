import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QCheckBox,
    QRadioButton, QButtonGroup, QLineEdit, QWidget, QHBoxLayout,
    QVBoxLayout, QGridLayout
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zameer's GUI Practice")
        self.setGeometry(700, 300, 1000, 1000)

        label = QLabel(self)
        label.setGeometry(10, 10, 641, 360)
        pixemap = QPixmap("../resources/img.jpg")
        label.setPixmap(pixemap)
        label.setScaledContents(True)

        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(15, 20, 100, 50)
        self.button.clicked.connect(self.on_click)

        self.checkbox = QCheckBox("Do you like coding?", self)
        self.checkbox.setGeometry(150, 150, 300, 150)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master card", self)
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio1)
        self.button_group.addButton(self.radio2)
        self.radio1.toggled.connect(self.radio_selected)
        self.radio2.toggled.connect(self.radio_selected)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter Your Name")
        self.line_edit.setGeometry(20, 40, 200, 40)

    def on_click(self):
        print("Button Clicked!")

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like coding!")
        else:
            print("You don't like coding")

    def radio_selected(self):
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
