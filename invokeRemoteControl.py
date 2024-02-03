import subprocess
import os

mayaBinDir=r"C:\Program Files\Autodesk\Maya2024\bin"#Dir containing mayapy

pwd=os.getcwd()#Dir containing MMU scripts so they can be called
scenePath=r"C:\Users\Callum\Documents\GitHub\MMU\sc004_sh001_v1.mb" #scene to be opened
mayaCommand=mayaBinDir+"\mayapy setExporter.py "+scenePath #Command to be run

subprocess.Popen(mayaCommand)#runs the command