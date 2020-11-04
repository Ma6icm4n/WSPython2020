import sys

if r"C:\Users\Asus\Desktop\WSPython2020" not in sys.path:
    sys.path.append(r"C:\Users\Asus\Desktop\WSPython2020") #import QT lib
    sys.path.append(r"C:\Users\Asus\Desktop\WSPython2020\pipeline") #import path to project

from Qt import QtWidgets, QtCompat, QtGui
from pipeline.ui import my_window as mw
from pipeline.engines import engine


app = QtWidgets.QApplication(sys.argv)

win = mw.MyWindow()
win.show()

sys.exit(app.exec_())