# Random Notes

- Empirical evidence would suggest that you should be calling c4d.threading.GeIsMainThread() before attempting to access the thread via c4d.threading.GeGetCurrentThread().
- And scripts in Script Manager are actually a very simplified version of CommandData plugins, in a way that these are basically one command per script.
- The thing is, opposite to a script and instead of implementing CommandData.Execute() you can also implement GetSubContainer() and ExecuteSubID(). By this you can have several commands in one single CommandData plugin, which can then be assigned with different keyboard shortcuts each, either in code or in Customize Commands manager
- All capital commands/attribute in C4D requires “c4d.” as a prefix. For instance, [ID_BASELIST_NAME] should be [c4d.ID_BASELIST_NAME] for it to work
-	Check attributes: Drag any object attribute to the console. Hit enter and it will return current attribute. For instance, Cube[c4d.ID_BASEOBJECT_REL_SCALE,c4d.VECTOR_X] will return 1.0 by default
-	Quick documentation: Print help(Cube). This will return all available commands for the cube object
-	For Tags it’s T[tagname] and similarly for Objects is O[object] Onull, Ocube, Osphere etc you can also call shader types with X[shader] Xgradient, Xlayer
-	Capital letters most likely represent global parameters. Refrain in using it as a variable.
-	Square brackets in the attribute documentation are optional
-	Special defined variables: Doc (refers to the active document) and Op (refers to the active object)
-	Computers like radians, but it is easier for user to manipulate in degrees. Hence, convert degree to radians. Command is under the utils
-	n to split the lines
-	DESCID is like an address to all the attribute in the attribute manager
-	GetMg() retrieve the global matrix
-	One disadvantage of the CallCommand() in Cinema 4D is the way it records separate Undo steps for each call to the function. This makes it impossible to have a single Undo for the whole script as the separate steps are recorded to the Undo stack individually.
-	When you get to more complicated scripts, a “call command” is basically breaking the codeflow. You can’t control the undo steps that it makes, and you are never really sure what exactly happens behind the “call command”.
-	When looking through the Cinema 4D Python documentation we find the c4d.documents module that has all the functionality to access our scene. The function GetActiveDocument() function returns the currently active scene as a BaseDocument object.
-	Now that we know how to access the scene we are left with finding out how to get a list of the selected objects in the scene. Looking at BaseDocument we see that it has a GetActiveObjects() method that returns a list of BaseObject objects.
- nes emulation plugin mario
-	op.GetName-
-	Almost all of them are methods. GetTime()
-	Object and Tag types
-	[] bracket operator in a case of a BaseList2D is an alias for Set/GetParameter.
-	[] bracket operator in a case of BaseContainer is an alias for SetData / GetData, see __setitem__ and __getitem__.
-	Easing in the utils.rangemapper using spline. Thanks Andy Needham!
-	Anim Selector: https://www.highend3d.com/maya/script/animselector-the-fast-picker-for-maya
-	In tags or XPresso nodes, changing the actual object tree is forbidden and may crash C4D (see documentation for Remove() and InsertUnderLast()).
-	Assertion Error. Insert them separately. If you have multiple insert object in the same control
-	GetBit Active to test if it is selected
-	C4D Base Container is a generic class that holds settings. Every object in cinema has a base container.
-	“…CINEMA 4D R16Commandline.exe” -render “…TestComp_3Dmap.c4d” -frame 0 0
-	The Timer will not be executed during a dragging operation. It blocks the main thread. Not even
-	messages and events are processed during that time. So, a thread that calls SpecialEventAdd()
-	wouldn’t allow this either.
-	You can use asynchronous dialogs whenever you want, just not in scripts. Scripts only live while they’re being executed, so asynchronous dialogs can’t work.
- Description based GUI's are mostly used with tag and object creation plugins.
- You've got it backwards Scott - ResEdit only works with the dialog resource syntax for plugins. It doesn't work with the description resource syntax for tags & objects.
- In general parameters of objects (or tags, materials,...) are specified in so called Descriptions (also here). With User Data it's a bit special, as you first need to obtain the User Data containers, which store the Descriptions, via GetUserDataContainer().



