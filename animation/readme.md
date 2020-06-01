### General

* First of all, you need the DescID(s) of the animated User Data parameter(s). This can be constructed quite easily, note the ID given from the User Data Manager, I'll call UDID here. The UDID is stored in the second level of a DescID, with the first level marking it as a User Data, for example like so:
* id = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA), c4d.DescLevel( UDID )) # replace UDID with ID of User Data
* The keyframes (CKey) are stored in curves (CCurve), which themselves are stored in tracks (CTrack). You can get hold of the CTrack with FindCTrack() (for any entity, not only a selected object) and the above constructed DescID. Via GetCurve() you get the CCurve and from this finally the CKey with for example GetKey(). Or you can directly move them in time with MoveKey().
* Note, time is handled as BaseTime.

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
Once you have the necessary tracks, adding keys is relatively simple. All the keys are applied to an F-Curve, which is a CCurve object in Python. So first you have to get the CCurve, and then you can use AddKey or InsertKey to add keys to the curve. Note that you can use the CTrack method FillKey to fill a key with the default values for the track, setting the appropriate interpolation. Also, you should use SetValue when setting a float value, and SetGeData when setting any other data type.
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


