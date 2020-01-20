# You can get the layer attached with the object with the obj.GetLayerObject()
# But there is no direct way to do the reverse (i.e. get objects attached in the layer)
# Here is a script that does that. 
# Recursive function was retrieved on https://developers.maxon.net/?p=26


import c4d

def recurse_hierarchy(op):
    count = 0
    obj_dict = {}
    while op:
        obj_dict[op.GetName()] = op.GetLayerObject(doc).GetName()
        op = op.GetNext()
    return obj_dict

if __name__=='__main__':
    obj_dict = recurse_hierarchy(doc.GetFirstObject())
    print obj_dict
