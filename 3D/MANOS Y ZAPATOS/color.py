import bpy

# Get the mesh object by name
obj = bpy.data.objects['hand.002']

# Create a new material or get an existing one
if len(obj.data.materials) == 0:
    mat = bpy.data.materials.new(name='MyMaterial')
else:
    mat = obj.data.materials[0]

# Set the diffuse color of the material
mat.diffuse_color = (0.69, 0.46, 0.31, 1.0) # This sets the color to orange with alpha 1.0

# Assign the material to the mesh object
obj.data.materials[0] = mat