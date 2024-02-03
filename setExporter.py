#Callum Stuart - https://linkedin.callumstuart.com https://github.com/cstuart1310 https://showreel.callumstuart.com
#Takes a selected set, then exports it and its' children as individual FBX files

print("\n"*30)#Spacing because I cant be bothered to keep clearing the log
import maya.cmds as cmds
import maya.mel as mel #evaluating FBX exporter because afaik it doesn't have cmds integration
import os

# Get a list of all the deformer sets in the scene:


parent=cmds.ls(sl=True,long=True)[0] #gets currently selected item

exportAsIndividual=False #Whether or not to export each child as a single FBX each, or export all children as one FBX

#Based on assumption of sceneNo_shotNo_versionNo
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
setList=cmds.listSets(allSets=True, ets=True, o=parent) #all sets in scene including irrelevant stuff

children = cmds.sets(parent, q=True)
print("Children:",children)
if children==None:#If children found is type None (Not to be confused with finding no children)
    cmds.error("No children found. Check that a set is selected and that it has children.")
else:#If children are found
    for child in children:#Loops through each child in the set (Grandchildren are selected when their parent is)
        
        if exportAsIndividual==True:#One FBX per child (Grandchildren merged with parents)
            cmds.select(child,add=False)#Adds the child to the selection
            outName=sceneDir+"/"+sceneNo+"_"+shotNo+"_"+parent+"_"+child+".fbx" #scene_shot_character_joint
        elif exportAsIndividual==False:#One FBX per set (Set's children, grandchildren etc all in one FBX)
            cmds.select(child,add=True)
            outName=sceneDir+"/"+sceneNo+"_"+shotNo+"_"+parent+".fbx" #scene_shot_character_joint

        
        print("Out path:",outName)
        fbxCommand='file -force -options "" -typ "FBX export" -pr -es "'+outName+'";'#exports using default FBX export settings
        mel.eval(fbxCommand)#Runs the command within MEL as there is no CMDS integration
