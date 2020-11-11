import tkinter as tk
from tkinter import ttk
from TkiWrapper.Widget import Widget
from TkiWrapper.Point import Point
from PIL import ImageTk, Image as PilImage
from Namespace.Namespace import Namespace

try:
  import cv2 as cv
  CV2_AVAILABLE = True
except ImportError:
  CV2_AVAILABLE = False

class Image(Widget):
  def __init__(self, frame, img, fit='fit', fixedSize=None, sticky='LRH', **kwargs):
    super().__init__(frame, sticky)
    self.tk = tk.Canvas(frame.upperFrame, highlightthickness=0, bg='#000', **kwargs)
    if fit not in ['fit', 'fill', 'stretch']:
      raise ValueError('Invalid value of Image "fit" parameter')
    self.fit = fit
    if fixedSize is not None:
      fixedSize = Point(*fixedSize)
      self.tk.config(width=fixedSize.x, height=fixedSize.y)
      self.tk.grid_propagate(False)
    else: self.size = None
    self.fixedSize = fixedSize
    self.canvasSize = Point(100, 100)
    self.enableResize = True
    self.img = img
    self.sizeData = self.calcImageData()
    self.tk.bind('<Configure>', self.setCanvasSize)
    self.renderImage()
    self.show()

  def resizeImages(self, state):
    self.enableResize = state

  def setCanvasSize(self, event):
    self.canvasSize = Point(event.width, event.height)
    self.sizeData = self.calcImageData()
    self.renderImage()

  def setImage(self, img):
    if not self.checkAlive(): return
    self.img = img
    self.renderImage()

  def calcImageData(self):
    if not self.checkAlive(): return
    if self.fixedSize:
      size, anchor, pos = self.fixedSize, 'nw', Point(0, 0)
    else:
      if self.fit == 'stretch':
        size, anchor, pos = self.canvasSize, 'nw', Point(0, 0)
      else:
        xScale = self.canvasSize.x / self.img.width
        yScale = self.canvasSize.y / self.img.height
        if self.fit == 'fill': scale = max(xScale, yScale)
        elif self.fit == 'fit': scale = min(xScale, yScale)
        size = Point(self.img.width * scale, self.img.height * scale)
        size.toInts()
        pos = Point(self.canvasSize.x//2, self.canvasSize.y//2)
        anchor = 'center'
    return Namespace(targetSize=size, anchor=anchor, targetPos=pos)

  def renderImage(self):
    if not self.checkAlive(): return
    sd = self.sizeData
    if self.enableResize:
      image = self.img.resize(sd.targetSize.get())
    else:
      image = self.img
    self.tk.delete('all')
    self.tkImage = ImageTk.PhotoImage(image=image)
    self.tk.create_image(sd.targetPos.get(), image=self.tkImage, anchor=sd.anchor)


if CV2_AVAILABLE:
  cvSize = lambda i: i.shape[:2][::-1]
  class OcvImage(Widget):
    def __init__(self, frame, img, fit='fit', fixedSize=None, sticky='LRH', **kwargs):
      super().__init__(frame, sticky)
      self.tk = tk.Canvas(frame.upperFrame, highlightthickness=0, bg='#000', **kwargs)
      if fit not in ['fit', 'fill', 'stretch']:
        raise ValueError('Invalid value of Image "fit" parameter')
      self.fit = fit
      if fixedSize is not None:
        fixedSize = Point(*fixedSize)
        self.tk.config(width=fixedSize.x, height=fixedSize.y)
        self.tk.grid_propagate(False)
      else: self.size = None
      self.fixedSize = fixedSize
      self.canvasSize = Point(100, 100)
      self.enableResize = True
      self.img = img
      self.sizeData = self.calcImageData()
      self.item = self.tk.create_image((0,0), anchor=self.sizeData.anchor)
      self.tk.bind('<Configure>', self.setCanvasSize)
      self.renderImage()
      self.show()

    def resizeImages(self, state):
      self.enableResize = state

    def setCanvasSize(self, event):
      self.canvasSize = Point(event.width, event.height)
      self.sizeData = self.calcImageData()
      self.renderImage()

    def setImage(self, img):
      if not self.checkAlive(): return
      self.img = img
      self.renderImage()

    def calcImageData(self):
      if not self.checkAlive(): return
      try: prevTargetPos = self.sizeData.prevTargetPos
      except AttributeError: prevTargetPos = Point(0, 0)
      if self.fixedSize:
        size, anchor, pos = self.fixedSize, 'nw', Point(0, 0)
      else:
        if self.fit == 'stretch':
          size, anchor, pos = self.canvasSize, 'nw', Point(0, 0)
        else:
          imgSize = cvSize(self.img)
          xScale = self.canvasSize.x / imgSize[0]
          yScale = self.canvasSize.y / imgSize[1]
          if self.fit == 'fill': scale = max(xScale, yScale)
          elif self.fit == 'fit': scale = min(xScale, yScale)
          size = Point(imgSize[0] * scale, imgSize[1] * scale)
          size.toInts()
          pos = Point(self.canvasSize.x//2, self.canvasSize.y//2)
          anchor = 'center'
      return Namespace(targetSize=size, anchor=anchor, targetPos=pos, prevTargetPos=prevTargetPos)

    def renderImage(self):
      if not self.checkAlive(): return
      sd = self.sizeData
      if self.enableResize:
        image = cv.resize(self.img, sd.targetSize.get())
      else:
        image = self.img
      self.tkImage = ImageTk.PhotoImage(image=PilImage.fromarray(image))
      self.tk.move(self.item, *sd.targetPos.dist(sd.prevTargetPos).get())
      self.tk.itemconfig(self.item, image=self.tkImage, anchor=sd.anchor)
      sd.prevTargetPos = sd.targetPos
