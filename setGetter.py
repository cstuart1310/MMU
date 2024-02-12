import maya.cmds as cmds
import maya.standalone #runs maya headlessly
import sys#args
import os#paths

def getSets(scenePath):
    print("""
 __________________
< Maya Make Unreal >
 ------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
          

Launching headless Maya instance to read sets.
          
A lot of text is going to show in this window, all of it can be safely ignored.
""")
    print("Reading sets from",scenePath)
    print("_"*20)#nice spacer
    maya.standalone.initialize(name='python')#Starts a maya standalone instance (Essentially headless maya)
    cmds.file(scenePath, open=True, force=True)#Opens the given scene file
    mayaSets=cmds.ls(type='objectSet')# Get all sets from the outliner
    print(mayaSets)
    maya.standalone.uninitialize()
    return mayaSets

def writeSets(sets):
    setFile=open(setFilePath,"w")
    for setName in sets:
      setFile.write(setName+"\n")

scenePath=sys.argv[1]
setFilePath=(os.path.realpath(__file__)).replace("setGetter.py","sets.txt")
sets=getSets(scenePath)
writeSets(sets)