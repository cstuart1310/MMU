#Callum Stuart - https://linkedin.callumstuart.com https://github.com/cstuart1310 https://showreel.callumstuart.com
import unreal
import os

# Menu parameters


# Menu entry parameters
CUSTOM_TYPE = custom_type=unreal.Name("")

pluginDir=(os.path.realpath(__file__)).replace("windowAdder.py","")#Gets the plugin folder's path
buttonScript = pluginDir+"mayaMakeUnrealInterface.py" #script that runs on button press


menus = unreal.ToolMenus.get()
main_menu = menus.find_menu("LevelEditor.MainMenu")
print(main_menu.get_name())
script_menu = main_menu.add_sub_menu(main_menu.get_name(), "File", "MMU", "MMU")
print(script_menu)
entry = unreal.ToolMenuEntry(
    name="Python.Tools",
    # If you pass a type that is not supported Unreal will let you know,
    type=unreal.MultiBlockType.MENU_ENTRY,
    # this will tell unreal to insert this entry into the First spot of the menu
    insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
)
entry.set_label("Maya-Make-Unreal")
# this is what gets executed on click
entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, CUSTOM_TYPE, string=(buttonScript))
# add our new entry to the new menu


script_menu.add_menu_entry("Scripts",entry)
# refresh the UI
menus.refresh_all_widgets()
