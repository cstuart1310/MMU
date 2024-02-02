print("\n"*30)#Spacing because I cant be bothered to keep clearing the log
import maya.cmds as cmds
import maya.mel as mel #evaluating FBX exporter because afaik it doesn't have cmds integration
import os

# Get a list of all the deformer sets in the scene:

#print(setList)
outDir="out/"
charName="charName_exp" #key used to identify what's relevant

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
setList=cmds.listSets( allSets=True, ets=True, o=charName) #all sets in scene including irrelevant stuff



# for currentSet in setList: #Can't use the set keyword as its' a thing in python
    
#     # print("\nCurrent Set:",currentSet)
#     # print("Parent:",cmds.listRelatives(currentSet,parent=True))#Shows parent of current set
    
#     # print("Children:",cmds.listRelatives(charName,children=True))#Shows array of children of current set

cmds.select(charName)#Selects the current set
outName=sceneDir+"/"+shotNo+"_"+charName+"_"+charName+".fbx" #scene_shot_character_joint 
print("Out path:",outName)
#cmds.FBXExport('-file', outName)

fbxCommand='file -force -options "" -typ "FBX export" -pr -es "'+outName+'";'
print(fbxCommand)
mel.eval(fbxCommand)