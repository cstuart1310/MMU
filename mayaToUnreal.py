import maya.cmds as cmds
import maya.mel as mel
def getShaders():
    shaders=cmds.ls(exactType="standardSurface")
    print(shaders)


getShaders()