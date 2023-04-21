from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel, QPushButton, QFileDialog
from PyQt5 import uic
import sys
from utils import  generateReportFile
from generatePdf import generatePdf

def readFile(path):
    with open(path, "r") as f:
        rows= f.readlines()
        return rows

class GUI(QMainWindow):

    
    def __init__(self):
        super(GUI, self).__init__()
        # load file
        uic.loadUi("gui.ui",self)

        self.title = self.findChild(QLabel, "title")
        self.select_file = self.findChild(QPushButton, "selectFile")
        self.file_path = self.findChild(QLabel, "filePath")
        self.select_folder = self.findChild(QPushButton, "selectFolder")
        self.folder_path = self.findChild(QLabel, "folderPath")
        self.generate_btn = self.findChild(QPushButton, "generateBtn")
        self.loaded_file_path = ''
        self.loaded_folder_path = ''

        #set actions to widgets
        self.select_file.clicked.connect(self.select_file_handler)
        self.select_folder.clicked.connect(self.select_folder_handler)
        self.generate_btn.clicked.connect(self.generate_btn_handler)
        # show 
        self.show()

    def select_file_handler(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] != '':
            self.loaded_file_path = filename[0]
            self.file_path.setText(self.loaded_file_path)

    def select_folder_handler(self):
        filename = QFileDialog.getExistingDirectory(self, 'Seleccionar Carpeta')
        if filename != '':
            self.loaded_folder_path = filename
            self.folder_path.setText(self.loaded_folder_path)

    def generate_btn_handler(self):
        rows = readFile(self.loaded_file_path)
        
        for row in rows:
            (file_name, order_information, transaction_information) = generateReportFile(row)
            generatePdf(self.loaded_folder_path,file_name, order_information, transaction_information)

        
# Initialice App
app = QApplication(sys.argv)
UIWindow = GUI()
app.exec_()