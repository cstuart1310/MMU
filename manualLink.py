import maya.cmds as cmds
#.color, _color, .baseColor

cmds.hyperShade(shaderNetworksSelectMaterialNodes = 1)
shader = cmds.ls(sl=True)[0]

shaderType = cmds.nodeType(shader)

base=cmds.connectionInfo(shader+'.baseColor', sfd=True)
specRoughness=cmds.connectionInfo(shader+'.specularRoughness', sfd=True)
bump=cmds.connectionInfo(shader+'.normalCamera', sfd=True)

print("Shader Name:",shader)
print ("Shader Type:",shaderType)
print("Textures:",cmds.listConnections(shader))
print("Base:",base)
print("Spec Roughness:",specRoughness)
print("Bump:",bump)


cmds.connectAttr(base,'outPhongE.color', force=True)
cmds.connectAttr(specRoughness,'outPhongE.roughness', force=True)
cmds.connectAttr(bump,'outPhongE.normalCamera', force=True)
