I am very lazy. So lazy that the process of exporting files from Maya and then importing them to Unreal Engine seemed like a task that needed automating.

Introducing MMU (Mmm-Oooh)! A tool with the goal of simplifying this process with a single UI which runs in Unreal Engine, allowing you to import Maya sets as FBX files without needing Maya open.

**This script is very early in development, and so is likely to break! Please post any bugs in the [issues](https://github.com/cstuart1310/MMU/issues) page**

## Installation:
Run the following command in a command prompt (CMD from the start menu). Make sure to change the path depending on your UE version and installation location
Default install location (UE 5.3)
> C:\Program Files\Epic Games\UE_5.3\Engine\Binaries\ThirdParty\Python3\Win64>python.exe -m pip install pyside2

[Download](https://github.com/cstuart1310/MMU/archive/refs/heads/MMU_revamped.zip) the repository as a Zip, place it in a location of your choice.

## Usage:
Paste the following command into your command box within UE, making sure that it is set to "Python" and not "CMD" or "Python (REPL)":
> C:\yourPathToThisPlugin\MayaToUnreal\mayaToUnreal\mayaMakeUnrealInterface.py
For example, based on my installation I would run:
> D:\Coding\Python\VFX\Maya\MayaToUnreal\mayaToUnreal\mayaMakeUnrealInterface.py
Then ensure the values within the input boxes are correct, and click import. This will then export the children of a set named "exportSet"
