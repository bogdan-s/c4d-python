# Ref: https://plugincafe.maxon.net/topic/12163/creating-class-for-buttons-returns-none

import c4d

class ColorButton(object):

    def __init__(self):
        self.width = None
        self.height = None
        self.color = None
        self.color = None
        self.btn_id = 3000


    def create(self, dlg, w, h, color, btn_id):

        self.width = w
        self.height = h
        self.color = color

        bmp_color = c4d.bitmaps.BaseBitmap()
        bmp_color.Init(w, h)

        for y in xrange(w):
            for x in xrange(h):
                bmp_color.SetPixel(x, y, color[0], color[1], color[2])

        bcBitmapButton = c4d.BaseContainer()
        bcBitmapButton[c4d.BITMAPBUTTON_BUTTON] = True

        bmp_btn = dlg.AddCustomGui(btn_id, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_CENTER | c4d.BFV_CENTER, w, h, bcBitmapButton)

        bmp_btn.SetImage(bmp_color, True)

class MyDialog(c4d.gui.GeDialog):

    def CreateLayout(self):
        # Creating a red button through class
        # This part causes the error

        red_button = ColorButton()
        red_button.create(self, w=50,h=50,color=(255,0,0), btn_id=6000)
                
        return True
    
dlg = MyDialog()
dlg.Open(dlgtype=c4d.DLG_TYPE_ASYNC)
