# FBX import in Blender does not support hierarchical grouping when a geometry is skinned
# The output file of this script is used for another script in Blender

import c4d
import json

file = "D:\layer_list.json"

def get_all_objects(op, filter, output):
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

all_obj = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(c4d.Opolygon), [])

data_dict = {}

for obj in all_obj:
    data_dict[obj.GetName()] = obj.GetLayerObject(doc).GetName()

with open(file, "w") as write_file:
    json.dump(data_dict, write_file, indent=4)
    
