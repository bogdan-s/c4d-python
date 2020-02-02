Materials are stored at two levels: object and data. This distinction is useful when you ‘duplicate linked’ Alt+ D an object.

- If the link is ‘OBJECT’: each duplicate can have its own material in the material slot
- If the link is ‘DATA’: all duplicates will share the same material

```python
import bpy
ob = bpy.context.active_object

# Get material
mat = bpy.data.materials.get("Material")
if mat is None:
    # create material
    mat = bpy.data.materials.new(name="Material")

# Assign it to object
if ob.data.materials:
    # assign to 1st material slot
    ob.data.materials[0] = mat
else:
    # no slots
    ob.data.materials.append(mat)
```

```python
# ACCESS
all_mat = bpy.data.materials
mat = bpy.data.materials.get("material_name")
mat_list_obj = obj.data.materials
active_mat = obj.active_material

# CREATE 
mat = bpy.data.materials.new("new_material") 

# ASSIGN
obj.data.materials[0] = mat # Assuming there is an existing material slot
obj.data.materials.append(mat) # if there are no available slot

# MODIFY VANILLA PARAMETERS 
# Parameters where the "Use Nodes" is disabled 
mat.diffuse_color = (0.5,0.5,0.5,1) # the 4th number is alpha. 
mat.metallic = 1 


# MODIFY NODE PARAMETERS 
# Parameters where the "Use Nodes" is enabled, which is what you'll be mostly likely working on '''

    # Access nodes  
mat.use_nodes = True # If not already enabled. 
node_tree = mat.node_tree
node_list = node_tree.nodes 
diffuse = node_list.get("Diffuse BSDF")

    # Create Nodes
    # Check https://docs.blender.org/api/current/bpy.types.ShaderNode.html for the list of shader nodes'''
tex_node = node_tree.nodes.new("ShaderNodeTexImage")
diffuse_node = nodes.new('ShaderNodeBsdfDiffuse')
diffuse_node.location = (100,100)


    # Connect Nodes
node_tree.links.new(node_A.inputs['InputName'], node_B.outputs['OutputName']
port_name_list = [input.name for input in Node_A.inputs]

bsdf = mat.node_tree.nodes["Principled BSDF"]
tex_node = mat.node_tree.nodes.new('ShaderNodeTexImage')
tex_node.image = bpy.data.images.load("C:\\path\\to\\im.jpg")
mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_node.outputs['Color'])

# Modify Nodes
node.inputs['Metallic'].default_value = 1.0
```

```python
# Alternative
import bpy
ob = bpy.context.active_object

# Get material
mat = bpy.data.materials.get("Material")
if mat is None:
    # create material
    mat = bpy.data.materials.new(name="Material")

# Assign it to object
if ob.data.materials:
    # assign to 1st material slot
    ob.data.materials[0] = mat
else:
    # no slots
    ob.data.materials.append(mat)
```

