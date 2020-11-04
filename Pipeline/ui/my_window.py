import sys, os # classic import

sys.path.append(r'C:\Users\Asus\Desktop\WSPython2020\lib') #import QT from the top folder

from Qt import QtWidgets, QtCompat 
from pipeline.engines import engine

ui_path = os.path.join(os.path.dirname(__file__), "my_window.ui") #relative path to the my_window.ui Qt window

class MyWindow(QtWidgets.QMainWindow):

    nameEngine = engine.get_current() #get the current engine used
    
    def __init__(self):
        super(MyWindow, self).__init__()
        print(ui_path)
        QtCompat.loadUi(ui_path, self)
        self.open_button.clicked.connect(self.open)

    def open(self, path):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\Asus\\Documents")#use Qt to open dialog box to choose a file
        file = self.nameEngine.open(filename[0])#open this file in the corresponding DCC




