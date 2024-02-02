import maya.cmds as cmds

# Get a list of all the deformer sets in the scene:
setList=cmds.listSets( allSets=True, ets=True )
#print(setList)

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