import sys
import hou
import os
print('Starting up pipeline')

if r"C:\Users\Asus\Desktop\WSPython2020" not in sys.path:
    sys.path.append(r'C:\Users\Asus\Desktop\WSPython2020') #import QT lib
    sys.path.append(r'C:\Users\Asus\Desktop\WSPython2020\Pipeline') #import path to project

from ui import my_window as mw

win = mw.MyWindow()
win.show()


print('Done Pipeline config')