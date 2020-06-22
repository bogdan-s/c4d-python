### General Commands
* Get All Objects
* Get All Objects by Type
* Get Selected Object 
  * method 1: `doc.GetActiveObject()`
  * method 2: `op`
* Get Object by Full Name: `doc.SearchObject("object_name")`
* Get Object by Partial Name
* Get Object from Python Tag: `op.GetObject()`
* Get Tag from Selected Object: `op.GetTag(objectID)`
* Get Material
* Get Objects Position/Rotation/Scale (either in Global or Local Space): [Matrix Fundamentals](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/manuals/data_algorithms/classic_api/matrix.html)
* Get Tag
* Select by Same Layer
* Query Parameter:
  - The easiest way to query the parameter is to either drag it into the `console` and hit `enter` or drag it directly to the `script manager`. Be it noted that you need to modify it to a proper object, if you query it using the script manager. You can see a better illustration in the [official documentatioin](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/manuals/introduction/python_console.html)
      ```python
      # Dragging into the console
      Cube[c4d.PRIM_CUBE_LEN,c4d.VECTOR_X] # Result 200.0

      # Dragging into the script manager and modify
      Cube = doc.SearchObject("Cube")
      Cube[c4d.PRIM_CUBE_LEN,c4d.VECTOR_X] # Result 200.0
      ```
- Set Parameter
  - Method 1: Like quering, you can just the drag the parameter but this time add a = sign and the corresponding value.
  - `Cube[c4d.PRIM_CUBE_LEN,c4d.VECTOR_X] = 300`
  - Method 2:
      ```python
      bc = op.GetDataInstance() # Get object

      # Note: c4d.BaseContainer.GetDataInstance() returns the original container, NOT A COPY. 
      # Modifying this container will directly modify the object’s parameters.
      # If you want to get a copy, use c4d.BaseObject.GetData()

      bc.SetVector(c4d.PRIM_CUBE_LEN, c4d.Vector(500, 100, 20)) # Set Parameter
      ```
* All capital commands/attribute in C4D requires `c4d` as a prefix. For instance, `[ID_BASELIST_NAME]` should be `[c4d.ID_BASELIST_NAME]` for it to work
* Get Current Frame `c4d.documents.GetActiveDocument().GetTime().GetFrame(doc.GetFps())`
* Empirical evidence would suggest that you should be calling c4d.threading.GeIsMainThread() before attempting to access the thread via c4d.threading.GeGetCurrentThread().
* And scripts in Script Manager are actually a very simplified version of CommandData plugins, in a way that these are basically one command per script.
* The thing is, opposite to a script and instead of implementing CommandData.Execute() you can also implement GetSubContainer() and ExecuteSubID(). By this you can have several commands in one single CommandData plugin, which can then be assigned with different keyboard shortcuts each, either in code or in Customize Commands manager
* Quick documentation: Print help(Cube). This will return all available commands for the cube object
*	For Tags it’s T[tagname] and similarly for Objects is O[object] Onull, Ocube, Osphere etc you can also call shader types with X[shader] Xgradient, Xlayer
*	Capital letters most likely represent global parameters. Refrain in using it as a variable.
* Special defined variables: `doc` (refers to the active document) and `op` (refers to the active object).
* It's explicit equivalent is `doc = c4d.documents.GetActiveDocument()` and `op = doc.GetActiveObject()`
*	Computers like radians, but it is easier for user to manipulate in degrees.
* Just use a utility conversion such as `c4d.utils.DegToRad(d)`
*	DESCID is like an address to all the attribute in the attribute manager
*	GetMg() retrieve the global matrix
*	One disadvantage of the CallCommand() in Cinema 4D is the way it records separate Undo steps for each call to the function. This makes it impossible to have a single Undo for the whole script as the separate steps are recorded to the Undo stack individually.
*	When you get to more complicated scripts, a “call command” is basically breaking the codeflow. You can’t control the undo steps that it makes, and you are never really sure what exactly happens behind the “call command”.
* GetBit Active to test if it is selected
* C4D Base Container is a generic class that holds settings. Every object in cinema has a base container.

* Object and Tag types
 *[] bracket operator in a case of a BaseList2D is an alias for Set/GetParameter.
 *[] bracket operator in a case of BaseContainer is an alias for SetData / GetData, see __setitem__ and __getitem__.
-	Easing in the utils.rangemapper using spline. Thanks Andy Needham!
- nes emulation plugin mario
-	Anim Selector: https://www.highend3d.com/maya/script/animselector-the-fast-picker-for-maya
-	In tags or XPresso nodes, changing the actual object tree is forbidden and may crash C4D (see documentation for Remove() and InsertUnderLast()).
-	Almost all of them are methods. GetTime()
-	“…CINEMA 4D R16Commandline.exe” -render “…TestComp_3Dmap.c4d” -frame 0 0
-	The Timer will not be executed during a dragging operation. It blocks the main thread. Not even messages and events are processed during that time. So, a thread that calls SpecialEventAdd() wouldn’t allow this either.
-	You can use asynchronous dialogs whenever you want, just not in scripts. Scripts only live while they’re being executed, so asynchronous dialogs can’t work.
- Description based GUI's are mostly used with tag and object creation plugins.
- You've got it backwards Scott - ResEdit only works with the dialog resource syntax for plugins. It doesn't work with the description resource syntax for tags & objects.
- In general parameters of objects (or tags, materials,...) are specified in so called Descriptions (also here). With User Data it's a bit special, as you first need to obtain the User Data containers, which store the Descriptions, via GetUserDataContainer().
- nes emulation plugin mario


```python
import c4d  
data = c4d.gui.FontDialog()  
  
for k, v in data:  
  print k, v  
  
font = c4d.FontData()  
font.SetFont(font)
```
