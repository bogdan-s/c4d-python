# Ben Traje
# Simple search and filter dialog

import c4d
from c4d import bitmaps, documents, gui, plugins, threading, utils

search_static_text = 101010
search_edit_text = 202020
search_button = 303030
search_result_grp = 404040
word_list = ['spotty', 'green', 'mash', 'ultra', 'cord', 'sudden', 'colorful', 'shivering', 'gainful', 'religion', 'deadpan', 'religion', 'inflame', 'evasive', 'mushy', 'stupid', 'nonstop', 'good-bye','eatable', 'kneel', 'paint']

filtered_word_list = []

class MyDialog(c4d.gui.GeDialog):
    def CreateLayout(self):
        self.GroupBegin(id=303030, flags=0, cols=2)
        self.AddStaticText(id=search_static_text, flags=c4d.BFH_LEFT, initw=80, inith=0, name="Search", borderstyle=0)
        self.AddEditText(id=search_edit_text, flags=c4d.BFH_LEFT, initw=150, inith=0, editflags=0)
        self.GroupEnd

        self.GroupBegin(id=search_result_grp, flags=0, cols=1)
        for word in word_list:
            self.AddStaticText(id=909090, flags=c4d.BFH_LEFT, initw=0, inith=0, name=word, borderstyle=0)
        self.GroupEnd

        return True

    def Command(self, id, msg):

        if id == search_edit_text:
            search_string = self.GetString(id=search_edit_text)

            filtered_word_list = []

            for word in word_list:
                if search_string in word:
                    filtered_word_list.append(word)


            self.LayoutFlushGroup(search_result_grp)
            for word in filtered_word_list:
                self.AddStaticText(id=909090, flags=c4d.BFH_LEFT, initw=0, inith=0, name=word, borderstyle=0)
            self.LayoutChanged(search_result_grp)

        return True

    def CoreMessage(self, id, data):
        return True
if __name__ == "__main__":
    dlg = MyDialog()
    dlg.Open(dlgtype=c4d.DLG_TYPE_ASYNC)
