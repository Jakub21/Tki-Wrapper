import tkinter as tk
from TkiWrapper.canvas.point import Point
from TkiWrapper.canvas.color import Color
from TkiWrapper.config import conf

class Element:
  '''Class used to store data of elements that are to be drawn on canvas
  Object oriented approach is helpful in organizing parameters
  and making parameters easily updatable'''
  def __init__(self, canvas):
    self.copyCanvasData(canvas)

  def copyCanvasData(self, canvas):
    '''Detached from constructor so its easily accessible lower in inheritance
      when creating from classmethods'''
    self.cnv = canvas
    self.cnv.add(self)
    self.stroke = canvas.STROKE.clone()
    self.fill = canvas.FILL.clone()
    self.strokeWidth = canvas.STROKE_WIDTH

  def remove(self):
    self.cnv.elements.persistent = [e for e in self.cnv.elements.persistent \
      if e is not self]
    self.cnv.elements.nonpers = [e for e in self.cnv.elements.nonpers \
      if e is not self]

  def trp(self, pt):
    '''Transposes point according to current attributes of parent canvas'''
    return pt.transposedClone(self.cnv.ANCHOR, self.cnv.SCALE)
