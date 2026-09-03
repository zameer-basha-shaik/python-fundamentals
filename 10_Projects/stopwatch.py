# Python PyQt5 Stopwatch 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stop_watch(QWidget):

    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00", self)
        self.star_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def start(self):
        pass
    



if __name__ == "__main__":

    app = QApplication(sys.argv)
    stopwatch = Stop_watch()
    stopwatch.show()
    sys.exit(app.exec_())