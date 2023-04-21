from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel, QPushButton
from PyQt5 import uic
import sys

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        # load file
        uic.loadUi("gui.ui",self)

        self.title = self.findChild(QLabel, "title")
        self.selectFile = self.findChild(QPushButton, "selectFile")
        self.filePath = self.findChild(QLabel, "filePath")
        self.selectFolder = self.findChild(QPushButton, "selectFolder")
        self.folderPath = self.findChild(QLabel, "folderPath")
        self.generateBtn = self.findChild(QPushButton, "generateBtn")
        # show app
        self.show()


# Initialice App
app = QApplication(sys.argv)
UIWindow = GUI()
app.exec_()