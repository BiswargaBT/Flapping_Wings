import mujoco

model = mujoco.MjModel.from_xml_path('/Users/biswargabidittamuli/InsectsCADModels/SeparatedInsects/AnoplophoraMalaciaca/am.urdf')
mujoco.mj_saveLastXML('/Users/biswargabidittamuli/InsectsCADModels/SeparatedInsects/AnoplophoraMalaciaca/output.xml', model)

print("Done! output.xml saved.")
