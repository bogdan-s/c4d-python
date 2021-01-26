import c4d
import json

# Exports a dictionary of materials with their corresponding object assignments

def main():
        
    material_list = doc.GetMaterials()
    file = "D:\material_obj_list.json"
    
    data_dict = {}

    for material in material_list:
        mat_assign_list = material[c4d.ID_MATERIALASSIGNMENTS]
        obj_count = mat_assign_list.GetObjectCount()
        obj_list = []
        
        if mat_assign_list:
            for i in range(obj_count):
                
                tag = mat_assign_list.ObjectFromIndex(doc,i)      #Gets the tag that's on the object
                obj = tag.GetObject().GetName() 
                obj_list.append(obj)                
        
        data_dict[material.GetName()] = obj_list
        
        
    with open(file, "w") as file:
        json.dump(data_dict, file, indent=4)

# Execute main()
if __name__=='__main__':
    main()
