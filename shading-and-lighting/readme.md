### Materials are stored at two levels: object and data. This distinction is useful when you ‘duplicate linked’ Alt+ D an object.

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
```

