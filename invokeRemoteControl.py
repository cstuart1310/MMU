import subprocess
import os

mayaBinDir=r"C:\Program Files\Autodesk\Maya2024\bin"

pwd=os.getcwd()
print(pwd)
scenePath=r"C:\Users\Callum\Documents\GitHub\MMU\sc004_sh001_v1.mb"
mayaCommand=mayaBinDir+"\mayapy mayaRemoteControl.py "+scenePath

subprocess.Popen(mayaCommand)