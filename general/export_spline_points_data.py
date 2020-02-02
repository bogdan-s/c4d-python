# I'm converting a C4D rig to a Blender rig.
# Unfortunately, the spline/curve objects are not accepted through FBX import. It is represented as a null. 
# I'm recreating the spline/curve controls from json data
# This script export the spline points data to jsona


import c4d
import json

def recurse_hierarchy(op):
    obj_list = []
    while op:
        obj_list.append(op)
        obj_list+= recurse_hierarchy(op.GetDown())
        op = op.GetNext()

    return obj_list


def truncate(num):

    if num > 0 and num < 0.001:
        new_num = 0.0
    elif num <0 and num > -0.001:
        new_num = 0.0
    else:
        new_num = num

    num_str = str(new_num)
    num = num_str.split(".")
    num_real = num[0]
    num_dec  = num[1][:4]

    new_num_str = "{}.{}".format(num_real, num_dec)
    new_num = float(new_num_str)

    return new_num


def main():
    all_objects = recurse_hierarchy(doc.GetFirstObject())

    spline_control = {}

    for obj in all_objects:
        name = obj.GetName()
        world_matrix = obj.GetMg()
        world_pos = obj.GetMg().off

        print obj.GetMg().off
        print truncate(world_pos[0])

        #raw_points = obj.GetAllPoints()
        raw_points = [point * world_matrix for point in obj.GetAllPoints() ]

        #for p in raw_points: print (p * world_pos)

        point_list = []

        for idx, p in enumerate(raw_points):

            pos0 = truncate(p[0])
            pos1 = truncate(p[1])
            pos2 = truncate(p[2])
            #point_list[idx] = (pos0, pos1, pos2)
            point_list.append( (pos0, pos1, pos2) )

        spline_control.update (
            {name: {"point_list": point_list,
                    "world_pos": (truncate(world_pos[0]), truncate(world_pos[1]), truncate(world_pos[2]))
                    }
             }
            )

    for key in spline_control:
        print key

    with open("D:\croc_controls.json", "w") as write_file:
        json.dump(spline_control, write_file, indent=4)


# Execute main()
if __name__=='__main__':
    main()
