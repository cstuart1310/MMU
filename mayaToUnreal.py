import maya.cmds as cmds
import maya.mel as mel

newShaderType="phongE"

oldShaders=["standardSurface"]#Current shader type that you want to convert
ignoredMats=["standardSurface1"]
maps=["baseColor","diffuseRoughness","metalness","specularRoughness","normalCamera"]#Maps to grab files from and re-link to the new material

def getShaders():#Gets the list of current shaders to convert
    
    shaders=cmds.ls(exactType="standardSurface")
    print(shaders)
    return shaders


#Start
print("\n"*5,"----------------")
print("""

MMU

Callum Stuart
""")

oldShaders=getShaders()

for oldShader in oldShaders:
    if oldShader not in ignoredMats:#Mostly done to ignore standardsurface1 but can be used to filter whatever
        newShaderName=oldShader+"_"+newShaderType#Change this last variable to whatever you want for the suffix of the new material
        newShader = cmds.shadingNode(newShaderType, name=newShaderName, asShader=True)
        print("Created:",newShader)
        for map in maps:
            try:
                texture=cmds.listConnections(oldShader+"."+map)[0]
                print(map+":"+texture)

                if map=="normalCamera":
                    cmds.connectAttr(texture+".outNormal",newShaderName+'.normalCamera', force=True)    
                else:
                    cmds.connectAttr(texture+".outColor",newShaderName+'.color', force=True)
        
            except TypeError:#Errors if the map dont exist
                print("Map",map," doesn't exist (probably)")
        print("Finished with",oldShader,"\n----------------")
