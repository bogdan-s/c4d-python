# Add Edit Slider Resets to Zero
import c4d
from c4d import bitmaps, documents, gui, plugins, threading, utils


class MyDialog(c4d.gui.GeDialog):

    def __init__(self):
        doc = c4d.documents.GetActiveDocument()
        self.finger_B_01_L_con = doc.SearchObject('finger_B_01_L_con')

    def CreateLayout(self):
        self.AddEditSlider(id=303030, flags=c4d.BFH_SCALEFIT, initw=80, inith=0)
        return True

    def InitValues(self):
        self.SetFloat(303030, 0.0, min=-45, max=45, step=0.01, min2=0.0, max2=0.0)
        return True


    def Message(self, msg, result):

        if msg.GetId() == c4d.BFM_ACTION:
            if self.GetFloat(303030) != 0:    
                rotation_current = self.finger_B_01_L_con.GetRelRot()[2]
                rotation_modify = c4d.utils.DegToRad(self.GetFloat(303030))
                rotation_new = rotation_current + rotation_modify
                
                print rotation_current
                print rotation_modify
                print rotation_new
                
                self.finger_B_01_L_con[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] = rotation_new
               
                c4d.DrawViews(c4d.DRAWFLAGS_ONLY_ACTIVE_VIEW | c4d.DRAWFLAGS_NO_THREAD | c4d.DRAWFLAGS_NO_REDUCTION | c4d.DRAWFLAGS_STATICBREAK)
                #c4d.EventAdd()
            
            # Set the AddEditSlider Back to Zero

        if msg.GetId() == c4d.BFM_INTERACTEND:
         
            self.InitValues()
            return True

        return c4d.gui.GeDialog.Message(self, msg, result)

    def Command (self, id, msg):
        
        return True
    
if __name__ == "__main__":
    dlg = MyDialog()
    dlg.Open(dlgtype=c4d.DLG_TYPE_ASYNC)
