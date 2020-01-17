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
