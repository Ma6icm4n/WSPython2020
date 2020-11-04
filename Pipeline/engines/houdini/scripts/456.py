import sys
import hou
import os
print('Starting up pipeline')

here = hou.getenv('HOUDINI_SCRIPT_PATH').split(';') [-1]
deployment_root =here.split('/pipeline/')[0]

print('Script root {}'.format(deployment_root))

sys.path.append(deployment_root) #import path to project
#sys.path.append(os.path.join(deployment_root, 'pipeline')
sys.path.append(r'C:\Users\Asus\Desktop\WSPython2020\lib') #import QT lib

from pipeline.ui import my_window as mw

win = mw.MyWindow()
win.show()


print('Done Pipeline config')