# written by m_adam
# https://plugincafe.maxon.net/topic/11694/highlighted-command-text-icon-when-it-is-executed/6

import c4d
from c4d import gui, plugins, bitmaps, utils, documents

PLUGIN_ID   = 1010203

class MyMenuPlugin(plugins.CommandData):

    def Execute(self, doc):
        self.state = not self.state

        return True

    def GetState(self, doc):
        # Previously you were almost safe but in case of self.state is something different than True or False you returned nothing
        if not self.state:
            return c4d.CMD_ENABLED
        else:
            return c4d.CMD_VALUE | c4d.CMD_ENABLED

    @property
    def state(self):
        doc = c4d.documents.GetActiveDocument()
        bd = doc.GetActiveBaseDraw()
        displayFilter = bd.GetDisplayFilter()

        if displayFilter & c4d.DISPLAYFILTER_HYPERNURBS:
            return bd[c4d.BASEDRAW_DISPLAYFILTER_HYPERNURBS]

        return False
    
    @state.setter
    def state(self, value):
        # Checks if the value is a boolean
        if not isinstance(value, bool):
            raise TypeError("value is not a bool.")

        doc = c4d.documents.GetActiveDocument()
        bd = doc.GetActiveBaseDraw()
        displayFilter = bd.GetDisplayFilter()

        if displayFilter & c4d.DISPLAYFILTER_HYPERNURBS:
            bd[c4d.BASEDRAW_DISPLAYFILTER_HYPERNURBS] = False
            print "Switched Off Subdivision Surface Display Filter"
        else:
            bd[c4d.BASEDRAW_DISPLAYFILTER_HYPERNURBS] = True
            print "Switched On Subdivision Surface Display Filter"

        bd.Message(c4d.MSG_CHANGE)
        c4d.EventAdd()
        c4d.StatusClear()

if __name__ == "__main__":
    status = plugins.RegisterCommandPlugin(PLUGIN_ID, "bt_Visibility",0, None, "bt_Visibility", MyMenuPlugin())
    if (status):
        print "Visibility plug-in successfully initialized"
