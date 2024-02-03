#Callum Stuart - https://linkedin.callumstuart.com https://github.com/cstuart1310 https://showreel.callumstuart.com
#Takes a selected set, then exports it and its' children as individual FBX files

print("\n"*30)#Spacing because I cant be bothered to keep clearing the log
import maya.cmds as cmds
import maya.mel as mel #evaluating FBX exporter because afaik it doesn't have cmds integration
import os

# Get a list of all the deformer sets in the scene:


parentSet=cmds.ls(sl=True,long=True)[0] #gets currently selected set

sceneFullPath= cmds.file(q=True, sn=True) #Gets file name as string
sceneDir = os.path.dirname(sceneFullPath)
sceneNo=(sceneFullPath.split("_")[0]).split("/")[-1]
shotNo=sceneFullPath.split("_")[1]
versionNo=(sceneFullPath.split("_")[2]).replace(".mb","")

print("Scene dir:",sceneDir)
print("Scene No:",sceneNo)
print("Shot No:",shotNo)
print("versionNo:",versionNo)

print("Exporting:")
setList=cmds.listSets( allSets=True, ets=True, o=parentSet) #all sets in scene including irrelevant stuff

children = cmds.sets(parentSet, q=True)
print(children)
for childSet in children:
    cmds.select(childSet)#Selects the current set
    outName=sceneDir+"/"+sceneNo+"_"+shotNo+"_"+parentSet+"_"+childSet+".fbx" #scene_shot_character_joint
    print("Out path:",outName)

    fbxCommand='file -force -options "" -typ "FBX export" -pr -es "'+outName+'";'
    print(fbxCommand)
    mel.eval(fbxCommand)
