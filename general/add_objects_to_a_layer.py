# Adds selected objects to a layer or an existing layer if the layer already exist
# I'm still figuring out on how to merge the if not and else portion as they seem to be redundant. 

import c4d
from c4d import gui

root = doc.GetLayerObjectRoot()
layers_list = root.GetChildren() 
reference_layer = c4d.documents.LayerObject()
new_layer_name = "reference"
layer_settings = {'solo': False, 'view': True, 'render': False, 'manager': True, 'locked': False, 'generators': True, 'deformers': False, 'expressions': True, 'animation': False}

if not layers_list: 
    reference_layer = c4d.documents.LayerObject()
    reference_layer.SetName(new_layer_name)
    reference_layer.SetLayerData(doc, layer_settings)
    reference_layer.InsertUnder(root) 

else: 
    for layer in layers_list:
        name =layer.GetName()
    
        if name == new_layer_name:
            reference_layer = layer
    
        else:
            reference_layer = c4d.documents.LayerObject()
            reference_layer.SetName(new_layer_name)
            reference_layer.SetLayerData(doc, layer_settings)
            reference_layer.InsertUnder(root) 
    
obj_list = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)

for obj in obj_list:
    obj.SetLayerObject(reference_layer)
    
c4d.EventAdd()

