# MAYA MAKE UNREAL

*Questions? Comments? Job opportunities? Contact me: https://linkedin.callumstuart.com*

I am very lazy. So lazy that the process of exporting files from Maya and then importing them to Unreal Engine seemed like a task that needed automating.

Introducing MMU (Mmm-Oooh)! A tool with the goal of simplifying this process with a single UI which runs in Unreal Engine, allowing you to import Maya sets as FBX files without needing Maya open.

**This script is very early in development, and so is likely to break! Please post any bugs in the [issues](https://github.com/cstuart1310/MMU/issues) page**

## Installation:
Run the following command in a command prompt (CMD from the start menu). Make sure to change the path depending on your UE version and installation location
Default install location (UE 5.3)
> "C:\Program Files\Epic Games\UE_5.3\Engine\Binaries\ThirdParty\Python3\Win64\python.exe" -m pip install pyside2

[Download](https://github.com/cstuart1310/MMU/releases/tag/v0.01) the repository as a Zip, place it in a location of your choice.

Open your Unreal Project, then go to:
Edit -> Project Settings -> Plugins - Python
In the startup scripts section, add a new array element (Press the plus button). In the new text box, enter:
> C:\yourPathToThisPlugin\windowAdder.py



## Usage:
Now when you open the Unreal project you installed the plugin to, there should be an "MMU" option at the top. Click this, then "Maya-Make-Unreal" to launch the UI.
Once in the UI, ensure the inputted values are correct for the Maya bin path, location of the plugin's files, and the scene path. If they are all correct, click import. This will then import all geometry from the set named "exportSet" from the scene.
