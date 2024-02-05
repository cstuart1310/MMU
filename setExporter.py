#Callum Stuart - https://linkedin.callumstuart.com https://github.com/cstuart1310 https://showreel.callumstuart.com

print("\n"*30)#Spacing because I cant be bothered to keep clearing the log
import maya.cmds as cmds
import maya.mel as mel #evaluating FBX exporter because afaik it doesn't have cmds integration
import maya.standalone #runs maya headlessly
import os
import sys #arg reading

outPathFile=(os.path.realpath(__file__)).replace("setExporter.py","outPaths.txt")

def initMaya():
    print("""
 __________________
< Maya Make Unreal >
 ------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
          

Launching headless Maya instance to export sets.
          
A lot of text is going to show in this window, all of it can be safely ignored.
""")
    print("_"*20)#nice spacer
    maya.standalone.initialize(name='python')#Starts a maya standalone instance (Essentially headless maya)
    cmds.file(scenePath, open=True, force=True)#Opens the given scene file

def getSets():
    # Get all sets from the outliner
    mayaSets=cmds.ls(type='objectSet')
    return mayaSets


def getOutName(exportAsIndividual,parent,child):#generates out path for FBX
    #Based on assumption of sceneNo_shotNo_versionNo
    sceneFullPath= cmds.file(q=True, sn=True) #Gets file name as string
    sceneDir = os.path.dirname(sceneFullPath)
    sceneName=sceneFullPath.split("/")[-1]#Scene file name (Removes path)

    if exportAsIndividual==True:
        outName=sceneDir+"/"+sceneName+"_"+parent+"_"+child+".fbx"#SceneName_parentSet_childSet
    elif exportAsIndividual==False:
        outName=sceneDir+"/"+sceneName+"_"+parent+".fbx"#SceneName_parentSet

    return outName

def chooseSet(mayaSets):
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
    elif children!=None:#If multiple children are found
        cmds.loadPlugin("fbxmaya.mll")#Ensures the FBX plugin is loaded (May not due to maya standalone)

        if exportAsIndividual==True:#Export one FBX per child
            for child in children:
                cmds.select(child,add=False)
                outName=getOutName(exportAsIndividual,parent,child)#Generates path for FBX to write to
                fbxCommand='file -force -options "" -typ "FBX export" -pr -es "'+outName+'";'#exports using default FBX export settings        
                mel.eval(fbxCommand)#Runs the command within MEL as there is no CMDS integration
                writeOutputPath(outName)

        elif exportAsIndividual==False:#Export one FBX per scene
            for child in children:
                cmds.select(child,add=True)
            outName=getOutName(exportAsIndividual,parent,child)#Generates path for FBX to write to
            fbxCommand='file -force -options "" -typ "FBX export" -pr -es "'+outName+'";'#exports using default FBX export settings        
            mel.eval(fbxCommand)#Runs the command within MEL as there is no CMDS integration
            writeOutputPath(outName)


#main
            
#command line args
scenePath = sys.argv[1] #Gets scene path from argument
exportAsIndividual=sys.argv[2] #Whether or not to export each child as a single FBX each, or export all children as one FBX


#converts commandline string to bool
if exportAsIndividual=="single":
    exportAsIndividual=False
elif exportAsIndividual=="individual":
    exportAsIndividual=True

open(outPathFile,"w").close()#Clears file on new run
initMaya()
mayaSets=getSets()
chosenSet="exportSet"#chooseSet(mayaSets)
exportSet(chosenSet)


# Close the instance to prevent memory leak
maya.standalone.uninitialize()

