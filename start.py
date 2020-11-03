import sys

if r"C:\Users\Asus\Desktop\WSPython2020" not in sys.path:
    sys.path.append(r"C:\Users\Asus\Desktop\WSPython2020") #import QT lib
    sys.path.append(r"C:\Users\Asus\Desktop\WSPython2020\Pipeline") #import path to project

from Qt import QtWidgets, QtCompat, QtGui
from Pipeline.ui import my_window as mw
from Pipeline.engines import engine


app = QtWidgets.QApplication(sys.argv)

win = mw.MyWindow()
win.show()

sys.exit(app.exec_())