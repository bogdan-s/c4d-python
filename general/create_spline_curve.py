# Creates Spline/Curve
# Used in creating controls for auto-rig system. 
# Ben Traje
import c4d

def main():

    shapePoints =  [c4d.Vector(33.124, 0, -19.001), c4d.Vector(33.124, 0, 16.781), c4d.Vector(-0.002, 0, 20.158),
                  c4d.Vector(-33.109, 0, 16.781), c4d.Vector(-33.109, 0, -19.001), c4d.Vector(-17.587, 0, -38.107),
                  c4d.Vector(-0.002, 0, -49.473), c4d.Vector(17.544, 0, -38.146)]
                  
    numPoints = len(shapePoints)

    spline = c4d.BaseObject(c4d.Ospline)
    spline[c4d.SPLINEOBJECT_CLOSED]= True
    spline[c4d.SPLINEOBJECT_TYPE] = 3
    spline.ResizeObject(numPoints)

    idx = 0

    for p in shapePoints:
        spline.SetPoint(idx, p)
        idx += 1

    doc.InsertObject(spline)

    spline.Message(c4d.MSG_POINTS_CHANGED)    
    c4d.EventAdd()
    
# Execute main()
if __name__=='__main__':
    main()
