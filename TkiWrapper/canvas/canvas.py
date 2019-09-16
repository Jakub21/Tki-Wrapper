import tkinter as tk
from tkinter import ttk
from TkiWrapper.widgets.widget import Widget
from TkiWrapper.canvas.point import Point
from TkiWrapper.canvas.color import Color
from TkiWrapper.namespace import Namespace

class Canvas(Widget):
  def __init__(self, view, key, size, sticky='LRH'):
    super().__init__(view, key)
    self.sticky = sticky
    self.canvas = tk.Canvas(view.holder, highlightthickness=0)
    self.widget = self.canvas # alias for compatibility with class Widget
    self.place()
    self.canvas.config(
      yscrollincrement='1', xscrollincrement='1',
      scrollregion=self.canvas.bbox(tk.ALL)
    )
    self.elements = Namespace(
      persistent = [],
      nonpers = [],
    )
    # Initialize geometry values
    self.SIZE = Point(*size)
    self.ANCHOR = Point(0, 0)
    self.SCALE = Point(1, 1)
    # Flags
    self.COLOR_MODE = 'STR'
    self.STROKE_WIDTH = 1
    self.STROKE = Color('STR', '#000')
    self.FILL = Color('STR', '#000')
    self.ANCHOR_IMAGES = 'CENTER'
    self.ANCHOR_MASTER = 'CENTER'
    self.SCALE_METHOD = 'RATIO'
    self.PERSISTENT = True
    # Interactive
    self.canvas.bind('<Motion>', self.updateMousePos)
    self.mouse = Point(0, 0)

  def update(self):
    self.updateTransposition()
    self.canvas.delete('all')
    for obj in self.elements.persistent:
      obj.draw()
    self.elements.oldNonPers = self.elements.nonpers
    self.elements.nonpers = []
    for obj in self.elements.oldNonPers:
      obj.draw()

  # Flag and draw methods

  def colorMode(self, mode):
    self.COLOR_MODE = mode

  def background(self, *args):
    self.canvas.config(bg=Color(self.COLOR_MODE, *args).get())

  def strokeWidth(self, width):
    self.STROKE_WIDTH = width

  def stroke(self, *args):
    if list(args) == [None]: self.STROKE = Color(None)
    else: self.STROKE = Color(self.COLOR_MODE, *args)

  def fill(self, *args):
    if list(args) == [None]: self.FILL = Color(None)
    else: self.FILL = Color(self.COLOR_MODE, *args)

  def persistent(self, state):
    self.PERSISTENT = state

  # Internal methods

  def add(self, element):
    if self.PERSISTENT: self.elements.persistent.append(element)
    else: self.elements.nonpers.append(element)

  def updateMousePos(self, evt):
    pt = Point(evt.x, evt.y)
    pt.transpose(self.ANCHOR, self.SCALE, reversed=True)
    self.mouse = pt

  # Geometry scaling and anchoring methods

  def updateTransposition(self):
    scalingMethods = {
      'NOSCALING': self._transposNoScaling,
      'FILL': self._transposFill,
      'RATIO': self._transposRatio,
      'RATIOFILL': self._transposRatioFill,
    }
    self.ANCHOR, self.SCALE = scalingMethods[self.SCALE_METHOD]()

  def _transposNoScaling(self):
    return (Point(0, 0), Point(1, 1))

  def _transposFill(self):
    cnvSize = self._getSize()
    scale = Point(canvas.x/self.SIZE.x, canvas.y/self.SIZE.y)
    return Point(0, 0), scale

  def _transposRatio(self):
    cnvSize = self._getSize()
    scale = self._calcScale(min)
    anchor = self._getAnchor(cnvSize, scale)
    return anchor, scale

  def _transposRatioFill(self):
    cnvSize = self._getSize()
    scale = self._calcScale(max)
    anchor = self._getAnchor(cnvSize, scale)
    return anchor, scale

  def _getSize(self):
    '''Returns real canvas size'''
    return Point(self.canvas.winfo_width(), self.canvas.winfo_height())

  def _calcScale(self, comprator):
    '''Helper method for _scaleRatio and _scaleRatioFill'''
    cnvSize = self._getSize()
    xScale = cnvSize.x / self.SIZE.x
    yScale = cnvSize.y / self.SIZE.y
    scale = comprator(xScale, yScale)
    return Point(scale, scale)

  def _getAnchor(self, cnvSize, scale):
    if self.ANCHOR_MASTER == 'UPPERLEFT' or self.SCALE_METHOD == 'FILL':
      x, y = 0, 0
    elif self.ANCHOR_MASTER == 'CENTER':
      x = (cnvSize.x - scale.x * self.SIZE.x) / 2
      y = (cnvSize.y - scale.y * self.SIZE.y) / 2
    return Point(x, y)
