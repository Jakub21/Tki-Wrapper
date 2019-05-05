from tkinter import N, S, E, W
from TkiWrapper.viewBase import ViewBase

class View(ViewBase):
    def __init__(self, root):
        super().__init__(root)
        self.showMode = 0 # 0 to show self, dialog key to show dialog

    #----------------------------------------------------------------
    # Display

    def show(self):
        if self.showMode == 0:
            for k, dlg in self.dialogs.items():
                dlg.hide()
            super().show()
            if not self.isSpecial: self.root.dialogMode(False)
        else:
            self.dialogs[self.showMode].show()
            if not self.isSpecial: self.root.dialogMode(True)

    #----------------------------------------------------------------
    # Dialogs

    def showDialog(self, key):
        self.showMode = key
        self.show()

    def dialogEnd(self):
        if self.showMode != 0:self.dialogs[self.showMode].dialogEnd()
        self.showMode = 0
        self.show()

    def addDialog(self, dlgView, key):
        self.dialogs[key] = dlgView
