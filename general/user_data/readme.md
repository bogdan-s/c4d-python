### Query all User Data with their current values

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
