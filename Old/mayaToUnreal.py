import maya.cmds as cmds
import maya.mel as mel

newShaderType="blinn"

#oldShaders=["standardSurface"]
oldShader="standardSurface"
ignoredMats=["standardSurface1"]

def getShaders():#Gets the list of current shaders to convert
    
    # for oldShader in oldShaders:
    shaders=cmds.ls(exactType=oldShader)

    print("Shaders found of type",oldShader,"\n",shaders)
    return shaders

def getTexture(map):
    try:
        try:
            texture=cmds.listConnections(oldShader+"."+map)[0]
            print(map+":"+texture)
            return texture
        
        except TypeError:#Errors if the map dont exist
            texture=cmds.listConnections(oldShader+"_"+map)[0]
            return texture
    except:
        print("Map",map," doesn't exist or isn't under the name shader.map or shader_map")
        return False


def setupNewShader(newShaderType,newShaderName):#Creates a new shader and a shader group (Maya makes the SG automatically but isn't happy about it so manually doing it here)
    newShader = cmds.shadingNode(newShaderType, name=newShaderName, asShader=True)
    sg = cmds.sets(name=newShaderName+"SG", empty=True, renderable=True, noSurfaceShader=True)
    cmds.connectAttr(newShaderName+".outColor", newShaderName+"SG.surfaceShader")
    print("Created:",newShader)
        
def convertFileTextures(shader):
    shaderGroup = cmds.listConnections(shader,type='shadingEngine')
    obj=cmds.hyperShade(objects=shader,add=True)[0]#selects the first object with the material
    cmds.convertSolidTx(shader, obj, fillTextureSeams=True,resolutionX=4096,resolutionY=4096,fileFormat="TIFF")


#Start
print("\n"*5,"----------------")
print("""

MMU

\|/          (__)    
     `\------(oo)
       ||    (__)
       ||w--||     \|/
   \|/

(Maya Make Unreal)


Callum Stuart
""")

oldShaders=getShaders()

for oldShader in oldShaders:
    if oldShader not in ignoredMats:#Mostly done to ignore standardsurface1 but can be used to filter whatever
        newShaderName=oldShader+"_"+newShaderType#Change this last variable to whatever you want for the suffix of the new material


        newShader=setupNewShader(newShaderType,newShaderName)
        

        try:
            base=cmds.connectionInfo(oldShader+'.baseColor', sfd=True)
            specRoughness=cmds.connectionInfo(oldShader+'.specularRoughness', sfd=True)
            bump=cmds.connectionInfo(oldShader+'.normalCamera', sfd=True)
            metalness=cmds.connectionInfo(oldShader+".metalness",sfd=True)
        except RuntimeError as e:
            print("Error getting connections or something")
            print(e)

        if metalness=='':
            metalness==(cmds.getAttr(oldShader+".metalness"))

        if specRoughness=='':
            specRoughness=(cmds.getAttr(oldShader+".specularRoughness"))
        try:
            cmds.connectAttr(base,newShaderName+'.color', force=True)
            print("specRoughness:",specRoughness)
            specRoughness=specRoughness.replace(".outColorR",".outColor")
            specRoughness=specRoughness.replace(".outAlpha",".outColor")

            cmds.connectAttr(specRoughness,newShaderName+'.specularColor', force=True)
            cmds.connectAttr(bump,newShaderName+'.normalCamera', force=True)
            cmds.connectAttr(metalness,newShaderName+',reflectivity',force=True)

        except Exception as e:
            print("Errored linking textures:")
            print(e)

        
        print("----------")

        print("Finished making new shader",oldShader)
        cmds.hyperShade(objects=oldShader)#Selects all objects with the old shader
        cmds.hyperShade(assign=newShaderName)#Assigns the new shader to all selected objects (Hopefully the same ones with the old shader)

