#Callum Stuart - https://linkedin.callumstuart.com https://github.com/cstuart1310 https://showreel.callumstuart.com

print("\n"*30)#Spacing because I cant be bothered to keep clearing the log
import maya.cmds as cmds
import maya.mel as mel #evaluating FBX exporter because afaik it doesn't have cmds integration
import maya.standalone #runs maya headlessly
import os
import sys #arg reading

outPathFile="D:\Coding\Python\VFX\Maya\MayaToUnreal\mayaToUnreal\outPaths.txt"

def initMaya():
    maya.standalone.initialize(name='python')#Starts a maya standalone instance (Essentially headless maya)
    cmds.file(sceneFile, open=True, force=True)#Opens the given scene file

def getSets():
    # Get all sets from the outliner
    mayaSets=cmds.ls(type='objectSet')
    return mayaSets


def getOutName(exportAsIndividual,parent,child):#generates out path for FBX
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

    if exportAsIndividual==True:
        outName=sceneDir+"/"+sceneNo+"_"+shotNo+"_"+parent+"_"+child+".fbx" #scene_shot_character_joint
    elif exportAsIndividual==False:
        outName=sceneDir+"/"+sceneNo+"_"+shotNo+"_"+parent+".fbx" #scene_shot_character_joint

    return outName

def chooseSet(mayaSets):
        # Print the sets
    print("Sets:")
    for setIndex, mayaSet in enumerate(mayaSets):
        print(setIndex,mayaSet)
    chosenSetIndex=input("Set to export:")
    return mayaSets[chosenSetIndex]

def writeOutputPath(outputPath):#Writes output path to txt so can be read by invoker (Easier to deal with than pipes)
    fbxFile=open(outPathFile,"a")
    fbxFile.write((outputPath+"\n"))
    fbxFile.close()


def exportSet(parent):
    children = cmds.sets(parent, q=True)#All children of set
    print("Children:",children)
    if children==None:#If children found is type None (Not to be confused with finding no children)
        cmds.error("No children found. Check that a set is selected and that it has children.")
    else:#If children are found
        for child in children:#Loops through each child in the set (Grandchildren are selected when their parent is)
            if exportAsIndividual==True:#One FBX per child (Grandchildren merged with parents)
                cmds.select(child,add=False)#Adds the child to the selection
            elif exportAsIndividual==False:#One FBX per set (Set's children, grandchildren etc all in one FBX)
                cmds.select(child,add=True)#Replaces the selection with the children
            outName=getOutName(exportAsIndividual,parent,child)#Generates path for FBX to write to
            print("Out path:",outName)
            fbxCommand='file -force -options "" -typ "FBX export" -pr -es "'+outName+'";'#exports using default FBX export settings
            print("Output command:",fbxCommand)
            cmds.loadPlugin("fbxmaya.mll")#Ensures the FBX plugin is loaded (May not due to maya standalone)
            mel.eval(fbxCommand)#Runs the command within MEL as there is no CMDS integration
            writeOutputPath(outName)


#main
exportAsIndividual=sys.argv[2] #Whether or not to export each child as a single FBX each, or export all children as one FBX

#converts commandline string to bool
if exportAsIndividual=="single":
    exportAsIndividual=False
elif exportAsIndividual=="individual":
    exportAsIndividual=True

sceneFile = sys.argv[1] #Gets scene path from argument
open(outPathFile,"w").close()#Clears file on new run
initMaya()
mayaSets=getSets()
chosenSet="exportSet"#chooseSet(mayaSets)
exportSet(chosenSet)


# Close the instance to prevent memory leak
maya.standalone.uninitialize()

