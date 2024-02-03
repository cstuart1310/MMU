import maya.standalone
import maya.cmds as cmds

def printSets(sceneFile):
    # Open the Maya scene file
    cmds.file(sceneFile, open=True, force=True)

    # Get all items from the outliner
    outliner_items = cmds.ls(assemblies=True, long=True)
    mayaSets=cmds.ls(type='objectSet')
    # Print the outliner items
    print("Sets:")
    for mayaSet in mayaSets:
        print(mayaSet)

    # Quit Maya standalone mode
    maya.standalone.uninitialize()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python maya_batch_script.py <sceneFile>")
        sys.exit(1)

    sceneFile = sys.argv[1]

    # Redirect Maya startup log to a file
    log_file = "maya_batch_log.txt"
    maya.standalone.initialize(name='python')

    printSets(sceneFile)

    # Close the log file
    maya.standalone.uninitialize()
