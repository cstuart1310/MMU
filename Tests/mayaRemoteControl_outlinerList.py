import maya.standalone
maya.standalone.initialize(name='python')

import maya.cmds as cmds

def print_outliner_items(scene_file):
    # Open the Maya scene file
    cmds.file(scene_file, open=True, force=True)

    # Get all items from the outliner
    outliner_items = cmds.ls(assemblies=True, long=True)

    # Print the outliner items
    print("Outliner Items:")
    for item in outliner_items:
        print(item)

    # Quit Maya standalone mode
    maya.standalone.uninitialize()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python maya_batch_script.py <scene_file>")
        sys.exit(1)

    scene_file = sys.argv[1]

    # Redirect Maya startup log to a file
    log_file = "maya_batch_log.txt"
    maya.standalone.initialize(name='python', standalone=True, plugin=True, script=True, verbose=False, outputLog=log_file)

    print_outliner_items(scene_file)

    # Close the log file
    maya.standalone.uninitialize()
