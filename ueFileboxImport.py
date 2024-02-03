import unreal

def import_fbx(file_path):
    # Get the current editor level
    level = unreal.EditorLevelLibrary.get_editor_world()
    
    # Create a new import task
    import_task = unreal.AssetImportTask()
    import_task.filename = file_path
    import_task.destination_path = "/Game/ImportedMeshes"  # Set your desired destination path
    
    # Set the options for the import task
    import_task.automated = True
    import_task.replace_existing = True
    import_task.save = True

    # Execute the import task
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])
# Set the FBX file path
fbx_file_path = r"C:\Users\CallyWally\Documents\CS-MR-2TB\Modelling\MMU\scenes\sceneNo_shotNo_exportSet_setBrain.fbx"

# Call the import function
import_fbx(fbx_file_path)
