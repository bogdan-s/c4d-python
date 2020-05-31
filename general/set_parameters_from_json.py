# Description: Adds a dynamic tag to a selected object with the json settings
# Ref https://plugincafe.maxon.net/topic/11917/setting-parameters-from-json-file

import c4d

# This default parameter sets the dynamics tag to a collider tag.
# Assume this is from an external JSON file hence all strings and integers
default_param = {
    "collider_body": {
        "alt": "Standard",
        "shift": "Standard",  
        "param": {
            "RIGID_BODY_DYNAMIC": 1, 
            "RIGID_BODY_RESTITUTION": 1,
            "RIGID_BODY_FRICTION": 1,
        }
    }
}

def main():
    
    tag_type = 180000102
    tag_name = "collider_body"

    tag = op.MakeTag(tag_type)
    doc.AddUndo(c4d.UNDOTYPE_NEW, tag)

    param_dict = default_param[tag_name]['param']

    for key, value in param_dict.items():
        keyId = getattr(c4d, key, None)
        if keyId is None:
            return False
        tag[keyId] = value
        
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()
