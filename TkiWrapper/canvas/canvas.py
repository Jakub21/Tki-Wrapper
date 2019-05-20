import tkinter as tk
from PIL import Image, ImageTk
from TkiWrapper.canvas.point import Point
from TkiWrapper.namespace import Namespace

class Canvas:
    def __init__(self, view):
        self.view = view
        # Core properties
        self.canvas = tk.Canvas(view.frame, highlightthickness=0)
        self.canvas.config(
            yscrollincrement='1', xscrollincrement='1',
            scrollregion=self.canvas.bbox(tk.ALL)
        )
        self.elements = []
        self.nonPersistent = []
        # Initialize geometry values
        self.SIZE = Point(100, 100)
        self.ANCHOR = Point(0, 0)
        self.SCALE = Point(1, 1)
        # Flags
        self.FOREGROUND = '#FFF'
        self.SCALE_METHOD = 'RATIO'
        self.ANCHOR_CONTENT = 'CENTER'
        self.ANCHOR_IMAGE = 'CENTER'
        self.STROKE_WIDTH = 3
        self.MAX_IMAGES = 1
        # Interactive features
        self.canvas.bind('<Motion>', self.updateMousePos)
        self.mouse = Point(0, 0)

    #----------------------------------------------------------------
    # General

    def update(self):
        self.updateTransposition()
        self.canvas.delete('all')
        for obj in self.elements:
            obj.draw()
        for obj in self.nonPersistent:
            obj.draw()
        self.nonPersistent = []

    #----------------------------------------------------------------
    # Setting flags and canvas configuration

    def setSize(self, size):
        self.SIZE = Point(*size)

    def strokeWidth(self, width):
        self.STROKE_WIDTH = width

    def setScalingMethod(self, method):
        if method.upper() not in ['NOSCALING', 'FILL', 'RATIO', 'RATIOFILL']:
            raise Exception(f'Invalid scaling method {method}')
        self.SCALE_METHOD = method.upper()

    def setScalingAnchor(self, mode):
        if mode.upper() not in ['CENTER', 'UPPERLEFT']:
            raise Exception(f'Invalid canvas anchor mode {mode}')
        self.ANCHOR_CONTENT = mode.upper()

    def setImageMode(self, mode):
        if mode.upper() not in ['CENTER', 'UPPERLEFT']:
            raise Exception(f'Invalid image anchoring mode {mode}')
        self.ANCHOR_IMAGE = mode.upper()

    def setForeground(self, color):
        self.FOREGROUND = color

    def setBackground(self, color):
        self.canvas.config(bg=color)

    #----------------------------------------------------------------
    # Managing draw elements

    def add(self, element):
        '''Adds element to draw'''
        element.reInit(self)
        self.elements.append(element)

    def addNonPrs(self, element):
        '''Adds non persistent element. Element will be deleted immediatelly
        after it is drawn'''
        element.reInit(self)
        self.nonPersistent.append(element)

    def empty(self):
        '''Empties elements list'''
        self.elements = []

    #----------------------------------------------------------------
    # Various getters

    def _getSize(self):
        '''Returns real canvas size'''
        return Point(self.canvas.winfo_width(), self.canvas.winfo_height())

    def imgSize(self, cnvSize, imgSize):
        '''Returns size in PX to which image has to be resized
        to fit in desired canvas coordinate rectangle'''
        x = imgSize.x * cnvSize.x / self.SCALE.x
        y = imgSize.y * cnvSize.y / self.SCALE.y
        return Point(x, y) # NOTE

    #----------------------------------------------------------------
    # Interactive features

    def updateMousePos(self, evt):
        pt = Point(evt.x, evt.y)
        pt.transpose(self.ANCHOR, self.SCALE, reversed=True)
        self.mouse = pt

    def getMouse(self):
        return self.mouse.clone()

    #----------------------------------------------------------------
    # Content Scaling

    def updateTransposition(self):
        if self.SCALE_METHOD == 'NOSCALING':
            self.ANCHOR, self.SCALE = Point(0, 0), Point(1, 1)
        elif self.SCALE_METHOD == 'FILL':
            self.ANCHOR, self.SCALE = self.trpFill()
        elif self.SCALE_METHOD == 'RATIO':
            self.ANCHOR, self.SCALE = self.trpRatio()
        elif self.SCALE_METHOD == 'RATIOFILL':
            self.ANCHOR, self.SCALE = self.trpRatioFill()

    def trpFill(self):
        canvas = self._getSize()
        scale = Point(canvas.x/self.SIZE.x, canvas.y/self.SIZE.y)
        return scale, Point(0, 0)

    def trpRatio(self):
        cnvSize = self._getSize()
        scale = self._calcScale(min)
        anchor = self._getAnchor(cnvSize, scale)
        return anchor, scale

    def trpRatioFill(self):
        cnvSize = self._getSize()
        scale = self._calcScale(max)
        anchor = self._getAnchor(cnvSize, scale)
        return anchor, scale

    def _calcScale(self, comprator):
        '''Helper method for _scaleRatioFill and _scaleRatio'''
        cnvSize = self._getSize()
        aspect = self.SIZE.x / self.SIZE.y
        xxScale = cnvSize.x / self.SIZE.x
        yxScale = cnvSize.y / self.SIZE.x
        xyScale = cnvSize.x / self.SIZE.y
        yyScale = cnvSize.y / self.SIZE.y
        xScale = comprator(yyScale, xyScale/aspect)
        yScale = comprator(xxScale, yxScale*aspect)
        return Point(xScale, yScale)

    def _getAnchor(self, cnvSize, scale):
        if self.ANCHOR_CONTENT == 'UPPERLEFT' or self.SCALE_METHOD == 'FILL':
            return Point(0, 0)
        if self.ANCHOR_CONTENT == 'CENTER':
            x = (cnvSize.x - scale.x * self.SIZE.x) / 2
            y = (cnvSize.y - scale.y * self.SIZE.y) / 2
            return Point(x, y)

    def distScale(self, distance, reversed=False):
        '''Calculates approx distance.
        If scale.y and scale.x differ much this method may cause problems'''
        if reversed: return distance * self.SCALE.x
        else: return distance / self.SCALE.x
