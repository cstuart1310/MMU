import maya.cmds as cmds

# Get a list of all the deformer sets in the scene:

#print(setList)
outDir="out/"
exportKey="charName" #key used to identify what's relevant

sceneName= cmds.file(q=True, sn=True) #Gets file name as string
sceneNo=(sceneName.split("_")[0]).split("/")[1]
shotNo=sceneName.split("_")[1]
versionNo=(sceneName.split("_")[2]).replace(".mb","")

print("Scene No:",sceneNo)
print("Shot No",shotNo)
print("versionNo",versionNo)

exportKey="charName"
sceneName= cmds.file(q=True, sn=True)
print("Exporting:")
print(setList)
for mayaSet in setList: #Can't use the set keyword as its' a thing in python
    if exportKey in mayaSet:#If the set is set to be exported
        print(mayaSet)
        cmds.select(mayaSet)#Selects the current set
        outName="out/"+sceneName+"_"+mayaSet+".fbx"
        #cmds.FBXExport('-file', outName)