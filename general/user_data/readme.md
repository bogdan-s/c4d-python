### Query all User Data with their CURRENT values

```python
import c4d
from c4d import gui
for id, descriptionBC in op.GetUserDataContainer():
    print("User Data ID: " + str(id))
    print("User Data Value: " + str(op[id]))
    print("User Data Name: " + descriptionBC[c4d.DESC_NAME])
```

```python
# result
User Data ID: ((700, 5, 0), (1, 15, 0))
User Data Value: 0
User Data Name: FKIK
User Data ID: ((700, 5, 0), (2, 15, 0))
User Data Value: 0
User Data Name: Bendy
User Data ID: ((700, 5, 0), (3, 19, 0))
User Data Value: 0.0
```
### Query a User Data will ALL their values

```python
# Source: https://plugincafe.maxon.net/topic/11407/how-to-get-to-the-str-value-in-a-userdata-integer-cycle/
import c4d
# user data parameter with the ID 1
ID = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER,0), c4d.DescLevel(1))
# get all user data parameter descriptions
for id, bc in op.GetUserDataContainer():
    # check for ID 1
    if id == ID:
        # print parameter name
        print("Parameter Name: " + bc.GetString(c4d.DESC_NAME))
        # get cycle settings
        cycleBC = bc.GetContainer(c4d.DESC_CYCLE)
        # print cycle data
        for element in cycleBC:
            print("Option: " + str(element[0]))
            print("Label: " + str(element[1]))
```

```python
# Result
# User Data
Parameter Name: FKIK
Option: 0
Label: FK
Option: 1
Label: IK

```

### Add User Data
```python
def AddLongDataType(obj) :
    if obj is None: return
  
    bc = c4d.GetCustomDatatypeDefault(c4d.DTYPE_LONG) # Create default container
    bc[c4d.DESC_NAME] = "Test"                        # Rename the entry
  
    element = obj.AddUserData(bc)     # Add userdata container
    
    for i in range(0, element.GetDepth()) :
        print element[i].id                  # element[i] is a DescLevel object
        print element[i].dtype
    
    # element[0] is for c4d.ID_USERDATA
    # element[1] is for our user data
    
    print "Added user data : ", element[1].id
    
    obj[element] = 30                 # Assign a value
    c4d.EventAdd()                    # Update
```

```python
#source: https://plugincafe.maxon.net/topic/11467/access-custom-user-data-by-name-not-by-id
def createIntSliderUserData(obj, value, sliderText=""):
    """
    Create a slider of integer on the given object.
    :param value: int => default value of the slider
    :param sliderText: the name of the slider
    """
    
    bc = c4d.GetCustomDatatypeDefault(c4d.DTYPE_LONG)
    bc[c4d.DESC_CUSTOMGUI] = c4d.CUSTOMGUI_LONGSLIDER
    bc[c4d.DESC_NAME] = sliderText
    bc[c4d.DESC_MIN] = 10
    bc[c4d.DESC_MAX] = 100
    description = obj.AddUserData(bc)
    if description is None:
        raise RuntimeError("Failed to creates a UserData.")
    
    obj[description] = value
    return description
```
### Remove User Data
```python
def RemoveLongDataType(obj) :
    for element, bc in obj.GetUserDataContainer() :
        if element[1].dtype == c4d.DTYPE_LONG:
            if obj.RemoveUserData(element) :
                print "Removed user data : ", element[1].id
            
            # To remove the data we could also call:
            # obj.RemoveUserData(element[1].id)
            # obj.RemoveUserData([c4d.ID_USERDATA, element[1].id])
    c4d.EventAdd()                    # Update
```

### Access User Data By Its Name
```python
source: https://plugincafe.maxon.net/topic/11467/access-custom-user-data-by-name-not-by-id/2
def IsUserDataPresentByName(obj, name):
    """
    Check if an user data parameter is already named like that on the passed obj
    :param obj: Any object that can holds User Data
    :param name: the name to looking for
    """
    
    if op is None:
        raise TypeError("obj is none.")
    
    if not name or not isinstance(name, str):
        raise TypeError("name is not valid.")
    
    # Iterate over all users data description
    for userDataId, bc in obj.GetUserDataContainer():
        
        # Retrieves the current name we iterates
        currentName = bc.GetString(c4d.DESC_NAME)
        
        # If the name is the same return True
        if currentName == name:
            return True
        
    # If we ended the loop without returning that means we didn't found our description
    return False
```

