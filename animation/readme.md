### General

* First of all, you need the DescID(s) of the animated User Data parameter(s). This can be constructed quite easily, note the ID given from the User Data Manager, I'll call UDID here. The UDID is stored in the second level of a DescID, with the first level marking it as a User Data, for example like so:
* id = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA), c4d.DescLevel( UDID )) # replace UDID with ID of User Data
* The keyframes (CKey) are stored in curves (CCurve), which themselves are stored in tracks (CTrack). You can get hold of the CTrack with FindCTrack() (for any entity, not only a selected object) and the above constructed DescID. Via GetCurve() you get the CCurve and from this finally the CKey with for example GetKey(). Or you can directly move them in time with MoveKey().
* Note, time is handled as BaseTime.
* Two methods to create a keyframe 
  * The hack method of selecting it and using the "Auto Keyframe command" 
  * Or The more verbose way. More flexibility. 
* http://www.plugincafe.com/forum/forum_posts.asp?TID=10986
* https://www.c4dcafe.com/ipb/forums/topic/94605-enable-disable-gui/
* http://www.plugincafe.com/forum/forum_posts.asp?TID=12759 
* DESCIDS:  https://www.cineversity.com/wiki/Python%3A_DescIDs_and_Animation/ 

### Access Animation
```python
# Access animation 

tracks = obj.GetCTracks() # Animatable paramaters
curves = tracks.GetCurve()
key_index_list = tracks.GetKeyCount()
key = curves.GetKey(idx) 

# Create animation 

# Create Tracks
# Track for Object Enabled Boolean
enabled = c4d.CTrack(op, c4d.DescID(c4d.ID_BASEOBJECT_GENERATOR_FLAG))
op.InsertTrackSorted(enabled)
# Track for Light Brightness Real
track = c4d.CTrack(op,c4d.DescID(c4d.LIGHT_BRIGHTNESS))
op.InsertTrackSorted(track)

#Creating Position X, Y, Z tracks
trackX = c4d.CTrack(op,
                    c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION,c4d.DTYPE_VECTOR,0),
                               c4d.DescLevel(c4d.VECTOR_X,c4d.DTYPE_REAL,0)))
trackY = c4d.CTrack(op,
                    c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION,c4d.DTYPE_VECTOR,0),
                               c4d.DescLevel(c4d.VECTOR_Y,c4d.DTYPE_REAL,0)))
trackZ = c4d.CTrack(op,
                    c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION,c4d.DTYPE_VECTOR,0),
                               c4d.DescLevel(c4d.VECTOR_Z,c4d.DTYPE_REAL,0)))
op.InsertTrackSorted(trackX)
op.InsertTrackSorted(trackY)
op.InsertTrackSorted(trackZ)

# Modify animation 



DescID > DescLevel
```

### Adding Keys
```python
#Adding Keys
'''
Once you have the necessary tracks, adding keys is relatively simple.
All the keys are applied to an F-Curve, which is a CCurve object in Python.
So first you have to get the CCurve, and then you can use AddKey or InsertKey to add keys to the curve.
Note that you can use the CTrack method FillKey to fill a key with the default values for the track, setting the appropriate interpolation. Also, you should use SetValue when setting a float value, and SetGeData when setting any other data type.
'''

#Get the curve
curve = track.GetCurve()
 
#Add keys using AddKey
#Creates the key at the proper time
#Then you modify the key
keyDict = curve.AddKey(c4d.BaseTime(0))
#keyDict is a dict with key=CKey and int=index
myKey = keyDict["key"]
#Use FillKey to fill the key with default values (interpolation)
trk.FillKey(doc,op,myKey)
#Use SetValue or SetGeData to set the key value
myKey.SetValue(curve,1)
#myKey.SetGeData(curve,1)
     
#Add keys using InsertKey
#Define the key first
key = c4d.CKey()
#Use FillKey to fill the key with default values (interpolation)
trk.FillKey(doc,op,key)
key.SetTime(curve,c4d.BaseTime(1))
key.SetValue(curve,.5)
#key.SetGeData(curve,1)
#Then insert it
curve.InsertKey(key)
```

### Setting Keyframe Selection
```python
# Setting the Keyframe Selection

# Put the "Position" desclevel in a variable for convenience
pos = c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DA_VECTOR)
# Set Keyframe selection on each vector X,Y,Z
op.SetKeyframeSelection(c4d.DescID(pos,c4d.DescLevel(c4d.VECTOR_X, c4d.DA_REAL, c4d.DA_VECTOR)), True)
op.SetKeyframeSelection(c4d.DescID(pos,c4d.DescLevel(c4d.VECTOR_Y, c4d.DA_REAL, c4d.DA_VECTOR)), True)
op.SetKeyframeSelection(c4d.DescID(pos,c4d.DescLevel(c4d.VECTOR_Z, c4d.DA_REAL, c4d.DA_VECTOR)), True)
# Update the C4D Interface
c4d.EventAdd()
```

### Finding A Track
```python
# Finding a Track

# Track for Light Brightness Real
dBrightness = c4d.DescID(c4d.LIGHT_BRIGHTNESS) #assign the DescID to a var for convenience
tBrightness = op.FindCTrack(dBrightness) #find the track
if not tBrightness:                      #if track isn't found, create it
    tBrightness = c4d.CTrack(op,dBrightness)
    op.InsertTrackSorted(tBrightness)
```

```python
t = doc.GetTime().Get()
frame = t * fps
```

```python
# Simple Copy of Tracks Nice!
# http://www.plugincafe.com/forum/forum_posts.asp?TID=11665&PID=48819#48819

import c4d

objectA = doc.SearchObject("objectA")
objectB = doc.SearchObject("objectB")
tracks = objectA.GetCTracks()
for track in tracks:
    clonedTrack = track.GetClone() 
    objectB.InsertTrackSorted(clonedTrack)
```

```python
'''
Hi,
this should help to identify a desclevel id and the corresponding dtype:
'''

import c4d

tracks = op.GetCTracks()
print tracks
for t in tracks:
    tr =  t.GetDescriptionID()
    print tr, "desc id"
    print tr[0],"first desc level"
    print tr[0].dtype
    print tr[0].id
    print tr[1],"second desc level"
    print tr[1].dtype
    print tr[1].id
```

```python
# the postion parameter description id, i.e. the animation type we
# are going to look for in our source object.
target_description = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, 
                                   c4d.DTYPE_VECTOR, 0) )

# get the position animation of object a
source_ctrack = my_baselist2d_a.FindCTrack(target_description)
# No position track found
if source_ctrack is None:
    return
    
# get the ccurve of our source ctrack
source_curve = source_ctrack.GetCurve()
# get the index of the last keyframe
lid = source_curve.GetKeyCount() - 1
# no keyframes
if lid < 0:
    return
# get the last CKey 
source_last_key = source_curve.GetKey(lid)
    
# get all animations of object b
target_ctracks = my_baselist2d_b.GetCTracks()

# loop over all tracks in our target
for ctrack in target_ctracks:
    # same thing as above, just shorter
    lid = ctrack.GetCurve().GetKeyCount() - 1
    if lid < 0:
        continue
    last_key = ctrack.GetCurve().GetKey(lid)
    # set the basetime of the last keyframe in the one of the tracks in
    # our target object to the basetime of the last keyframe in our source
    # objects position animation.
    last_key.SetTime(curve, source_last_key.GetTime()
```

```python
# Creating Keyframe 
# It only allows one parameter at one given time
# How to fetch the current values of the keyframe. 
'''
Hi,

you can define the tangents of a keyframe by using SetValueLeft(), SetValueRight(), SetTimeLeft() and SetTimeRight(). Together with SetInterpolation() this should do the trick.

Even if we are in the Python subforum, maybe the Overview and Manuals about Animation our C++ docs can also help with this topic.
'''

import c4d


def MakeKeyframe(obj, PSR, XYZ):

        doc = c4d.documents.GetActiveDocument()

        if PSR == "Position":
            DescLevel = c4d.ID_BASEOBJECT_REL_POSITION
        elif PSR == "Rotation":
            DescLevel = c4d.ID_BASEOBJECT_REL_ROTATION
        # elif here when scaling needed

        if XYZ == "X":
            SelectedVector = c4d.VECTOR_X
        elif XYZ == "Y":
            SelectedVector = c4d.VECTOR_Y
        else:
            SelectedVector = c4d.VECTOR_Z

        ActiveTrack = obj.FindCTrack (c4d.DescID(c4d.DescLevel(DescLevel,c4d.DTYPE_VECTOR,0), c4d.DescLevel(SelectedVector,c4d.DTYPE_REAL,0)))

        if not ActiveTrack:
            ActiveTrack = c4d.CTrack (obj, c4d.DescID(c4d.DescLevel(DescLevel,c4d.DTYPE_VECTOR,0), c4d.DescLevel(SelectedVector,c4d.DTYPE_REAL,0)))
            
            obj.InsertTrackSorted (ActiveTrack)

        Curve = ActiveTrack.GetCurve()
        CurrTime = doc.GetTime()
        CurrFrame = CurrTime.GetFrame(60)
        KeyDict = Curve.AddKey (c4d.BaseTime(CurrFrame, 60))
        ActiveTrack.FillKey (doc, obj, KeyDict["key"])

        c4d.EventAdd()

MakeKeyframe(op, PSR="Position", XYZ="Y")

```

```python
# Camera animation to Text file (CINEMA 4D)

import c4d
#Welcome to the world of Python
 
def Walker(obj):
    if not obj: return
 
    elif obj.GetDown():
        return obj.GetDown()
    while obj.GetUp() and not obj.GetNext():
        obj = obj.GetUp()
    return obj.GetNext()
 
def main():
    file = c4d.storage.SaveDialog(c4d.FILESELECTTYPE_ANYTHING, title='Save csv file as', force_suffix='csv')
    csv_file = open(file, 'w')
    obj = doc.GetFirstObject()
    while obj:
        if obj.GetType() == 5103:
            name = obj.GetName()
            obj_matrix = obj.GetMg()
            position = obj_matrix.off
            rotation_rad = c4d.utils.MatrixToHPB(obj_matrix,c4d.ROTATIONORDER_XYZGLOBAL)
            rotation_deg = c4d.Vector(c4d.utils.Deg(rotation_rad.x), c4d.utils.Deg(rotation_rad.y), c4d.utils.Deg(rotation_rad.z))
            line = '%s, %s, %s, %s, %s, %s'%(position.x,
                                                 position.y,
                                                 position.z,
                                                 rotation_deg.x,
                                                 rotation_deg.y,
                                                 rotation_deg.z)
            csv_file.write(line + '\n')
        obj = Walker(obj)
    csv_file.close()
 
 
if __name__=='__main__':
    main()
```

