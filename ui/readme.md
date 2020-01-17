### UI Dialog through Plugin Template

```python
import c4d
from c4d import bitmaps, documents, gui, plugins, threading, utils
# PLUGIN_ID Should be unique in ALL plug-in ecosystem.
# Get yours on this website https://developers.maxon.net/?page_id=3224
PLUGIN_ID   = 18113289  # Just test ID. Not for production. 
class MyDialog(c4d.gui.GeDialog):
    def CreateLayout(self):
        return True
    
    def Command(self, id, msg):
        return True
    
    def CoreMessage(self, id, data):
        return True
class MyMenuPlugin(plugins.CommandData):
    dialog = None
    def Execute(self, doc):
    # create the dialog
       if self.dialog is None:
          self.dialog = MyDialog()
       return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID, defaultw=200, defaulth=150, xpos=-1, ypos=-1)
    def RestoreLayout(self, sec_ref):
    # manage the dialog
       if self.dialog is None:
          self.dialog = MyDialog()
       return self.dialog.Restore(pluginid=PLUGIN_ID, secret=sec_ref)
if __name__ == "__main__":
    okyn = plugins.RegisterCommandPlugin(PLUGIN_ID, "UI Name",0, None, "UI Name", MyMenuPlugin())
    if (okyn):
        print "UI Name Plugin Initialized"
 ```
 
 ### UI Dialog through Script
```python
import c4d
from c4d import bitmaps, documents, gui, plugins, threading, utils
# PLUGIN_ID Should be unique in ALL plug-in ecosystem.
# Get yours on this website https://developers.maxon.net/?page_id=3224
PLUGIN_ID   = 18113289  # Just test ID. Not for production. 
class MyDialog(c4d.gui.GeDialog):
    def CreateLayout(self):
        return True
    
    def Command(self, id, msg):
        return True
    
    def CoreMessage(self, id, data):
        return True
if __name__ == "__main__":
    dlg = MyDialog()
    dlg.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID)
```
