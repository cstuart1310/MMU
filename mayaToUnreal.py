import maya.cmds as cmds
import maya.mel as mel

newShaderType="phongE"

oldShaders=["standardSurface"]

maps=["baseColor","diffuseRoughness","metalness","specularRoughness","normalCamera"]

def getShaders():
    
    shaders=cmds.ls(exactType="standardSurface")
    print(shaders)
    return shaders


oldShaders=getShaders()

for oldShader in oldShaders:

    newShaderName=oldShader+"_"+newShaderType
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
        except TypeError:
            print("Map",map," doesn't exist (probably)")