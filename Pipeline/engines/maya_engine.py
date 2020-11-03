from engines import engine
import maya.cmds as cmds

class MayaEngine(engine.Engine):
    def open(self, path):
        cmds.file(path, o=True)
        pass

    def save(self):
        cmds.file(rename="C:\Users\Asus\Desktop\test.ma")
        cmds.file(save=True, type="mayaAscii")
        pass


