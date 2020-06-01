import c4d
from c4d import bitmaps, documents, gui, plugins, threading, utils

# PLUGIN_ID is optional 
class MyDialog(c4d.gui.GeDialog):
    def CreateLayout(self):
        return True
    
    def Command(self, id, msg):
        return True
        
    def Message(self, msg, result): 
        return c4d.gui.GeDialog.Message(self, msg, result)
    
    def CoreMessage(self, id, data):
        return True
if __name__ == "__main__":
    dlg = MyDialog()
    dlg.Open(dlgtype=c4d.DLG_TYPE_ASYNC)
