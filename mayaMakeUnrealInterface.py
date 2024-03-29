#Callum Stuart - https://linkedin.callumstuart.com https://github.com/cstuart1310 https://showreel.callumstuart.com
#This script runs within the UE interpreter. It begins a subprocess which runs setExporter.py from the Mayapy interpreter. Once setExporter is done, this script imports the fbx into UE

import subprocess #Call the setExporter from within the mayaPy interpreter
import os #File removing
import sys #Reading command-line arguments
import unreal
from PySide2 import *
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *




#-----File import/exporting-----
def beginSetExporter(mayaBinDir,pluginDir,scenePath,exportAsIndividual):
    mayaCommand=mayaBinDir+"\mayapy "+pluginDir+"\setExporter.py "+scenePath+" "+exportAsIndividual #Command to be run
    print("Mayapy command:",mayaCommand)
    subprocess.call(mayaCommand)#runs the command and waits until done. Printed output from subprocess is piped to invoker
    readImportPaths()

def readImportPaths():#Reads paths of FBXs to import which were written by the setExporter
    outPathFile=open(pluginDir+"outPaths.txt","r")#Opens the file
    print("Reading exported FBX paths from",outPathFile)
    for outPath in outPathFile.readlines():#Loops through each line in txt
        outPath=outPath.replace("/","\\")
        outPath=outPath.replace("\n","")#Removes newlines (This line fixed a bug that took me 25 mins to troubleshoot)
        importFilebox(outPath) #Imports the file from the path
    

def importFilebox(importPath):
    print("Importing:",importPath)
    
    # Create a new import task
    import_task = unreal.AssetImportTask()
    import_task.filename = importPath
    import_task.destination_path = "/Game/MMU_Imports"  # Path that imports are stored in

    # Set the options for the import task
    import_task.automated = False #Allows the user to adjust import settings per FBX
    import_task.replace_existing = True #Overwrites existing dupes, means files can be updated easilly
    import_task.save = True

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])    #Execute the import task
    print("Imported file",importPath)
    os.remove(importPath) #Deletes the FBX produced by the exporter, as it is now saved within the UE project.
    print("Deleted file",importPath,"\n")

def openFileDialog(window, lineEdit,chooseFolder):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileDialog = QFileDialog()

    if chooseFolder==True:
        folderPath = fileDialog.getExistingDirectory(window, "Open Folder", lineEdit.text(), options=options)
        print("Folder Path:", folderPath)
        if folderPath != "":
            lineEdit.setText(folderPath)
    else:
        filePath, _ = fileDialog.getOpenFileName(window, "Open File", lineEdit.text(), "All Files (*);;Text Files (*.txt)", options=options)
        print("File Path:", filePath)
        if filePath != "":
            lineEdit.setText(filePath)

#-----UI-----

def initUI():#Launches the UI
    loader = QUiLoader()
    if not QApplication.instance():#If an instance does not exist
        app = QApplication(sys.argv)#Launch a new Qapplication
    else:#If an instance does exist
        app = QApplication.instance()#Launch a new instance
    uiPath=pluginDir+"\MMU_UE_UI.ui"
    window = loader.load(uiPath, None)#Loads UI from file

    #UI setup
    window.lineEdit_pluginPath.setText(pluginDir)#Sets the text in the plugin path to the gotten value
    print(pluginDir+"MMU_logo.png")
    window.setWindowIcon(QIcon(pluginDir+"MMU_logo.png"))

    #buttons
    window.pushButton_import.clicked.connect(lambda: getInputData(window))#When import button is pressed, run getImportData
    window.pushButton_cancel.clicked.connect(lambda: window.close())#When cancel button is pressed, close the window

    #File path buttons
    window.toolButton_scenePath.clicked.connect(lambda: openFileDialog(window,window.lineEdit_scenePath,False))
    window.toolButton_pluginPath.clicked.connect(lambda: openFileDialog(window,window.lineEdit_pluginPath,True))
    window.toolButton_binPath.clicked.connect(lambda: openFileDialog(window,window.lineEdit_binPath,True))
    loadPastValues(window)#Attempts to restore last successfully used values
    window.show()
    app.exec_()

def loadPastValues(window):#Reads past successful values from file and places them into text boxes
    pastValueFile=(pluginDir+"lastValues.txt")
    if os.path.isfile(pastValueFile):#If there is a past value file
        pastValueFile = open(pastValueFile,"r")
        pastValues=pastValueFile.readlines()
        #Doesn't set plugin path bcs plugin path must be correct for rest to work
        window.lineEdit_binPath.setText(pastValues[1].replace("\n",""))
        window.lineEdit_scenePath.setText(pastValues[2].replace("\n",""))

def writePastValues(pluginDir,mayaBinDir,scenePath):#Saves values to text file
    pastValueFile=open((pluginDir+"lastValues.txt"),"w")#Opens/creates the file, overwriting existing data
    pastValueFile.write(pluginDir+"\n")
    pastValueFile.write(mayaBinDir+"\n")
    pastValueFile.write(scenePath+"\n")
    pastValueFile.close()#Closes file and saves changes
    print("Saved paths to txt")

def getInputData(window):#Gets data from input boxes and then passes it to the maya parts of the script
    print("Getting data from input boxes")
    mayaBinDir=window.lineEdit_binPath.text()
    pluginDir=window.lineEdit_pluginPath.text()
    scenePath=window.lineEdit_scenePath.text()

    print("Maya Bin Dir:",mayaBinDir)
    print("Plugin Dir",pluginDir)
    print("Scene Path:",scenePath)

    #Converts radio button status to a string for passing to setExporter for exportAsIndividual argument
    if window.radioButton_exportAsIndividualTrue.isChecked():
        exportAsIndividual="individual"
    elif window.radioButton_exportAsIndividualFalse.isChecked():
        exportAsIndividual="single"
    window.close()
    beginSetExporter(mayaBinDir,pluginDir,scenePath,exportAsIndividual)
    writePastValues(pluginDir,mayaBinDir,scenePath)#If setExporter doesn't crash, saves successful values
    

#-----main-----
pluginDir=(os.path.realpath(__file__)).replace("mayaMakeUnrealInterface.py","")#Gets the plugin folder's path


initUI()

