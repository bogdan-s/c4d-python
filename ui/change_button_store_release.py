# Ben Traje
# Simple illustration on how to change button when it is clicked 

import c4d
from c4d import bitmaps, documents, gui, plugins, threading, utils

store_id     =  101010
release_id =  202020
flush_grp    =  303030

class MyDialog(c4d.gui.GeDialog):
    def CreateLayout(self):
        self.GroupBegin(id=flush_grp, flags=c4d.BFH_MASK, cols=1, rows=1, title="", groupflags=0, initw=0, inith=0)
        self.AddButton(id=store_id, flags=c4d.BFH_MASK, name="Store")
        self.GroupEnd()
        return True
    
    def Command(self, id, msg):
        if id == store_id:
            self.LayoutFlushGroup(flush_grp)   
            print "Stored"
            self.AddButton(id=release_id, flags=c4d.BFH_MASK, name="Release")
            self.LayoutChanged(flush_grp)
            
        if id == release_id:
            self.LayoutFlushGroup(flush_grp)   
            print "Released"
            self.AddButton(id=store_id, flags=c4d.BFH_MASK, name="Store")
            self.LayoutChanged(flush_grp)

        return True
    
    def CoreMessage(self, id, data):
        return True
if __name__ == "__main__":
    dlg = MyDialog()
    dlg.Open(dlgtype=c4d.DLG_TYPE_ASYNC)
