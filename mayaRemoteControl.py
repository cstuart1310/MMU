import maya.standalone
import maya.cmds as cmds

def getSets(sceneFile):#Gets the list of sets from the scene file
    # Open the Maya scene file
    cmds.file(sceneFile, open=True, force=True)

    # Get all sets from the outliner
    mayaSets=cmds.ls(type='objectSet')
    # Quit Maya standalone mode
    maya.standalone.uninitialize()
    

def chooseSet(mayaSets):
        # Print the sets
    print("Sets:")
    for setIndex, mayaSet in enumerate(mayaSets):
        print(setIndex,mayaSet)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python maya_batch_script.py <sceneFile>")
        sys.exit(1)

    sceneFile = sys.argv[1]

    # Redirect Maya startup log to a file
    maya.standalone.initialize(name='python')
    getSets(sceneFile)

    # Close the instance to prevent memory leak
    maya.standalone.uninitialize()
