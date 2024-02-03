#This script runs within the UE interpreter. It begins a subprocess which runs setExporter.py from the Mayapy interpreter. Once setExporter is done, it imports the fi

import subprocess
import os
import unreal #built into the UE python interpreter


def beginSetExporter():
    mayaBinDir=r"C:\Program Files\Autodesk\Maya2023\bin"#Dir containing mayapy
    pluginDir=r"D:\Coding\Python\VFX\Maya\MayaToUnreal\mayaToUnreal"
    pwd=os.getcwd()#Dir containing MMU scripts so they can be called
    scenePath=r"C:\Users\CallyWally\Documents\CS-MR-2TB\Modelling\MMU\scenes\sceneNo_shotNo_versionNo.mb" #scene to be opened
    mayaCommand=mayaBinDir+"\mayapy "+pluginDir+"\setExporter.py "+scenePath #Command to be run
    print(mayaCommand)
    mayaProcess = subprocess.call(mayaCommand)#runs the command and waits until done. Printed output from subprocess is piped to invoker
    #output, outBad = mayaProcess.communicate() #captures the printed output
    
    # for line in output:
    #     if "Out path:" in line:
    #         importPath=line.replace("Out path","")
    #         importFilebox(importPath)



def importFilebox(importPath):
    # Get the current editor level
    level = unreal.EditorLevelLibrary.get_editor_world()

    # Create a new import task
    import_task = unreal.AssetImportTask()
    import_task.filename = r"C:\Users\CallyWally\Documents\CS-MR-2TB\Modelling\MMU\scenes\sceneNo_shotNo_exportSet_setBrain.fbx"
    import_task.destination_path = "/Game/ImportedMeshes"  # Set your desired destination path

    # Set the options for the import task
    import_task.automated = True
    import_task.replace_existing = True
    import_task.save = True

    # Execute the import task
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

#main
beginSetExporter()
importFilebox("")