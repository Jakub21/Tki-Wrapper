from TkiWrapper.canvas.element import Element
from TkiWrapper.canvas.point import Point
import tkinter as tk

class Rect(Element):
  def __init__(self, canvas, ptA, ptB):
    super().__init__(canvas)
    self.ptA = Point(*ptA)
    self.ptB = Point(*ptB)

  def draw(self):
    ptA = self.trp(self.ptA)
    ptB = self.trp(self.ptB)
    self.cnv.canvas.create_rectangle(*ptA.get(), *ptB.get(), fill=self.fill.get(),
      outline=self.stroke.get(), width=self.strokeWidth)
