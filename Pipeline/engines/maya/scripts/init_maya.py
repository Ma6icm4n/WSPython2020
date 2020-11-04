import sys
import maya.cmds as cmds
import os
print('Starting up pipeline')
here = os.path.dirname(__file__)
deployment_root = here.split('/pipeline/')[0]


sys.path.append(r'C:\Users\Asus\Desktop\WSPython2020\lib') #import QT lib
sys.path.append(deployment_root) #import path to project

from pipeline.ui import my_window as mw

win = mw.MyWindow()
win.show()


print('Done Pipeline config')
