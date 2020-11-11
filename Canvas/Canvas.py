import tkinter as tk
from TkiWrapper.Widget import Widget
from TkiWrapper.Point import Point
from Canvas.Transpose import Transpose
from Canvas.Color import HexColor

class Canvas(Widget):
  def __init__(self, frame, sticky='LRH', **kwargs):
    super().__init__(frame, sticky)
    self.tk = tk.Canvas(frame.upperFrame, **kwargs)
    self.tk.config(
      yscrollincrement='1', xscrollincrement='1',
      scrollregion=self.tk.bbox(tk.ALL)
    )
    self.elems = []
    self.tempElems = []
    self.show()
    # Geometry
    self.transpose = Transpose(0, 0, 1, 1)
    self.transpose.setMode('contain')
    self.transpose.setElemSpaceBounds(Point(100, 100))
    self.transpose.setAnchorMode('center')
    # Interaction
    self.tk.bind('<Motion>', self.updateMousePos)
    self.mouse = Point(0, 0)
    # Interface flags
    self.COLOR_MODE = 'str'
    self.STROKE_WIDTH = 1
    self.COLOR_STROKE = HexColor('#000')
    self.COLOR_FILL = HexColor('#000')
    self.PERSISTENT = True

  def addElement(self, element):
    l = (self.elems if self.PERSISTENT else self.tempElems)
    l += [element]

  def setElemSpaceBounds(bounds):
    self.transpose.setElemSpaceBounds(bounds)

  def setTransposeMode(self, mode):
    self.transpose.setMode(mode)

  def setAnchorMode(self, mode):
    self.transpose.setMode(mode)

  def update(self):
    self.transpose.setRealSize(self.getRealSize())

  def background(self, color):
    self.tk.config(bg=color.getHex())

  def strokeClr(self, color):
    self.COLOR_STROKE = color

  def fillClr(self, color):
    self.COLOR_FILL = color

  def persistence(self, enable):
    self.PERSISTENT = enable

  def getRealSize(self):
    return Point(self.canvas.winfo_width(), self.canvas.winfo_height())

  def updateMousePos(self, evt):
    self.mouse = Point(0, 0) # TODO self.transpose.reversed(Point(evt.x, evt.y))
