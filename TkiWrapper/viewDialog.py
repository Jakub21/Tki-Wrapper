from TkiWrapper.viewBase import ViewBase

class Dialog(ViewBase):
    def __init__(self, root, positioner=None):
        super().__init__(root, positioner)
        self.endProtocol = None

    def dialogEnd(self):
        if self.endProtocol is not None:
            self.endProtocol()

    def setEndProtocol(self, func):
        self.endProtocol = func
