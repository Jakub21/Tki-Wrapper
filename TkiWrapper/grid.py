import tkinter as tk
from TkiWrapper.namespace import Namespace
class Grid:
    def __init__(self):
        self.pointer = Namespace(
            x = 0, y = 0,
            spanX = 1, spanY = 1,
        )
        self.defaults = Namespace(
            marginX = 0,
            marginY = 0,
            paddingX = 0,
            paddingY = 0,
        )
        self.colWrap = 1

    #----------------------------------------------------------------
    # Pointer auto-increment settings

    def setColWrap(self, width):
        '''Pointer auto increment only works if no element has spanY more than 1
        This may be repaired if project is not dumped'''
        self.colWrap = width

    #----------------------------------------------------------------
    # Widget pointer manipulation

    def resetPointer(self):
        self.pointer = Namespace(
            x = 0, y = 0,
            spanX = 1, spanY = 1,
        )

    def setPointer(self, x, y, spanX=1, spanY=1):
        self.pointer.x = x
        self.pointer.y = y
        self.pointer.spanX = spanX
        self.pointer.spanY = spanY

    def setSpan(self, spanX=1, spanY=1):
        self.pointer.spanX = spanX
        self.pointer.spanY = spanY

    def newLine(self):
        self.pointer.x = 0
        self.pointer.y += 1

    def shift(self, amount=1):
        self.pointer.x += amount
        if self.pointer.x >= self.colWrap:
            self.pointer.x = 0
            self.pointer.y += 1

    #----------------------------------------------------------------
    # Default margin settings

    def setMargin(self, x, y):
        self.defaults.marginX = x
        self.defaults.marginY = y

    def setPadding(self, x, y):
        self.defaults.paddingX = x
        self.defaults.paddingY = y

    #----------------------------------------------------------------
    # Class internal utilities

    def getParams(self, stretch=0, **kwargs):
        result = {
            'column': self.pointer.x,
            'row': self.pointer.y,
            'columnspan': self.pointer.spanX,
            'rowspan': self.pointer.spanY,
        }
        if stretch == 1:
            result['sticky'] = (tk.N, tk.W)
        if stretch == 2:
            result['sticky'] = (tk.N, tk.W, tk.S, tk.E)
        try: result['padx'] = kwargs['marginX']
        except KeyError: result['padx'] = self.defaults.marginX
        try: result['pady'] = kwargs['marginY']
        except KeyError: result['pady'] = self.defaults.marginY

        try: result['ipadx'] = kwargs['paddingX']
        except KeyError: result['ipadx'] = self.defaults.paddingX
        try: result['ipadx'] = kwargs['paddingX']
        except KeyError: result['ipadx'] = self.defaults.paddingX

        self.incrementPointer()
        return result

    def incrementPointer(self):
        self.pointer.x += self.pointer.spanX
        if self.pointer.x >= self.colWrap:
            self.pointer.x = 0
            self.pointer.y += 1
        self.pointer.spanX = 1
        self.pointer.spanY = 1
