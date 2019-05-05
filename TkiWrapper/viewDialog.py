from TkiWrapper.viewBase import ViewBase

class Dialog(ViewBase):
    def __init__(self, root):
        super().__init__(root)
        self.endProtocol = None

    def dialogEnd(self):
        if self.endProtocol is not None:
            self.endProtocol()

    def setEndProtocol(self, func):
        self.endProtocol = func
