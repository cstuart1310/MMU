#This script runs within the UE interpreter. It begins a subprocess which runs setExporter.py from the Mayapy interpreter. Once setExporter is done, this script imports the fbx into UE

import subprocess #Call the setExporter from within the mayaPy interpreter
import os #File removing
import sys #Reading command-line arguments
import unreal
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton



#-----File import/exporting-----
def beginSetExporter(mayaBinDir,pluginDir,scenePath):
    mayaCommand=mayaBinDir+"\mayapy "+pluginDir+"\setExporter.py "+scenePath #Command to be run
    print(mayaCommand)
    subprocess.call(mayaCommand)#runs the command and waits until done. Printed output from subprocess is piped to invoker
    readImportPaths()

def readImportPaths():#Reads paths of FBXs to import which were written by the setExporter
    print("Reading exports")
    outPathFile=open("D:\Coding\Python\VFX\Maya\MayaToUnreal\mayaToUnreal\outPaths.txt","r")#Opens the file
    for outPath in outPathFile.readlines():#Loops through each line
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
    os.remove(importPath) #Deletes the FBX produced by the exporter, as it is now saved within the UE project.


#-----UI-----
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

def initUI():
    if not QApplication.instance():#If an instance does not exist
        app = QApplication(sys.argv)#Launch a new Qapplication
    else:#If an instance does exist
        app = QApplication.instance()#Launch a new instance

    window = MainWindow()
    window.show()

    app.exec_()

#-----main-----
# mayaBinDir=sys.argv[1]#Dir containing mayapy interpreter
# pluginDir=sys.argv[2] #Path containing these scripts/shared data
# scenePath=sys.argv[3] #scene to be opened

mayaBinDir=r"C:\Program Files\Autodesk\Maya2023\bin"#Dir containing mayapy
pluginDir=r"D:\Coding\Python\VFX\Maya\MayaToUnreal\mayaToUnreal"
scenePath=r"C:\Users\CallyWally\Documents\CS-MR-2TB\Modelling\MMU\scenes\sceneNo_shotNo_versionNo.mb" #scene to be opened

